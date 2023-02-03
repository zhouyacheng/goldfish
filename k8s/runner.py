import logging

# import threading
from io import StringIO

import munch
import pykube
from jinja2 import Environment, FileSystemLoader
from django.conf import settings
from kubernetes import config
from kubernetes.client import ApiClient
from .k8s_client import KubernetesYamlClient
import yaml
from .models import (
    ReleaseTaskState,
    ReleaseTask,
    Stage,
    StageType,
    ProjectResource,
    ProjectEnv,
    ReleaseTaskHistory,
    ReleaseTaskProgress,
    EnvSnapshot,
    ResourceSnapshot,
    Configmap,
    Service,
    CustomResourceDefinition,
    CustomResource,
)


class KubernetesRunner(object):
    templdate_dir = settings.TEMPLATE_DIR
    env = Environment(loader=FileSystemLoader(searchpath=templdate_dir))

    # def __init__(self, release_task: ReleaseTask, stage: Stage = None):
    def __init__(self, release_task: ReleaseTask):
        self.release_task = release_task
        # self.stage = stage
        # self.next = (
        #     Stage.objects.order_by("seq")
        #     .filter(seq__gt=self.release_task.current.seq,pipeline=self.release_task.project.pipeline)
        #     .first()
        # )
        # self.event = threading.Event()

    @property
    def next(self):
        return (
            ReleaseTaskProgress.objects.filter(task=self.release_task)
            .order_by("seq")
            .filter(seq__gt=self.release_task.current.seq)
            .first()
        )

    def _lookup(self, stage: ReleaseTaskProgress):
        if stage:
            return self._lookup_stage(stage)
        else:
            return self._lookup_current(stage)

    def _lookup_stage(self, stage: ReleaseTaskProgress):
        if stage.seq == self.release_task.current.seq:
            return stage
        if stage.id == self.next.id:
            if self.release_task.state in {ReleaseTaskState.COMPLETED}:
                return stage
        return

    def _lookup_current(self, stage: ReleaseTaskProgress):
        if stage.state in {ReleaseTaskState.PENDING, ReleaseTaskState.FAILED}:
            return stage
        if stage.state in {ReleaseTaskState.COMPLETED}:
            return self.next
        return

    def _render_build_template(self, stage: ReleaseTaskProgress):
        template = self.env.from_string(self.release_task.project.build_template)
        # res = ProjectResource.objects.filter(project=self.release_task.project,stage=stage).first()
        # env_list = ProjectEnv.objects.filter(project=self.release_task.project,stage=stage)
        res = ResourceSnapshot.objects.get(stage=stage)
        env_list = EnvSnapshot.objects.filter(stage=stage)
        namespace = stage.namespace
        image_version = self.release_task.version
        text = template.render(
            deploy_name="yc",
            namespace=namespace,
            image_name=f"registry.cn-beijing.aliyuncs.com/zyc1013/public:flask-hello-dockerv{image_version}",
            image_version=image_version,
            env=env_list,
            res=res,
            container_port=50001,
        )
        print(f"build_template text: {text}")
        self.release_task.render_template = text
        self.release_task.save()
        return yaml.safe_load(text)

    def _render_deploy_template(self, stage: ReleaseTaskProgress):
        template = self.env.from_string(self.release_task.project.deploy_template)
        # res = ProjectResource.objects.filter(project=self.release_task.project, stage=stage).first()
        # env_list = ProjectEnv.objects.filter(project=self.release_task.project, stage=stage)
        res = ResourceSnapshot.objects.get(stage=stage)
        env_list = EnvSnapshot.objects.filter(stage=stage)
        namespace = stage.namespace
        image_version = self.release_task.version
        text = template.render(
            deploy_name="yc",
            namespace=namespace,
            image_name=f"registry.cn-beijing.aliyuncs.com/zyc1013/public:flask-hello-dockerv{image_version}",
            image_version=image_version,
            env=env_list,
            res=res,
            container_port=50001,
        )
        # print(f"deploy_template text: {text}")
        self.release_task.render_template = text
        self.release_task.save()
        return yaml.safe_load(text)

    def _render(self, stage: ReleaseTaskProgress):
        if stage.stage_type == StageType.BUILD:
            return self._render_build_template(stage)
        if stage.stage_type == StageType.DEPLOY:
            return self._render_deploy_template(stage)

    def _execute(self, stage: ReleaseTaskProgress):
        # self.event.clear()
        config.load_kube_config(
            config_file=StringIO(stage.kubeconfig_content), context=stage.context
        )
        client = KubernetesYamlClient(ApiClient(), self._render(stage))
        ret = client.ensure()
        if stage.stage_type == StageType.DEPLOY:
            self.release_task.observed_generation = ret.status.observed_generation
            self.release_task.save()
            stage.observed_generation = ret.status.observed_generation
            stage.render_template = self._render(stage)
        stage.save()
        # threading.Thread(target=self.listen).start()

    def execute(self, stage: ReleaseTaskProgress):
        if self.release_task.state in {
            ReleaseTaskState.RUNNING,
            ReleaseTaskState.CLOSED,
        }:
            raise Exception("running or close")
        stage = self._lookup(stage)
        if stage is None:
            raise Exception("没有可以执行的步骤")
        self.release_task.state = ReleaseTaskState.RUNNING
        # self.release_task.current_id = stage.seq
        self.release_task.save()
        stage.state = ReleaseTaskState.RUNNING
        stage.save()
        # history = ReleaseTaskHistory.objects.create(
        #     task=self.release_task,
        #     stage=stage,
        #     state=ReleaseTaskState.RUNNING,
        # )

        try:
            self._execute(stage)
        except Exception as e:
            print(e)
            self.release_task.state = ReleaseTaskState.FAILED
            self.release_task.save()
            stage.state = ReleaseTaskState.FAILED
            stage.save()
        return self.release_task

    @classmethod
    def make_snapshot(cls, task: ReleaseTask):
        for stage in task.project.pipeline.stage_set.all():
            item = ReleaseTaskProgress()
            item.task = task
            item.stage_type = stage.stage_type
            item.name = stage.name
            item.namespace = stage.namespace
            item.seq = stage.seq
            item.kubeconfig_content = stage.kubeconfig_content
            item.context = stage.context
            item.state = ReleaseTaskState.PENDING
            item.observed_generation = task.observed_generation
            item.created_by = task.created_by
            item.save()
            for env in ProjectEnv.objects.filter(project=task.project, stage=stage):
                cls.snapshot_env(item, env)
            res = ProjectResource.objects.get(project=task.project, stage=stage)
            cls.snapshot_resource(item, res)

    @classmethod
    def snapshot_env(cls, stage: ReleaseTaskProgress, origin: ProjectEnv):
        snapshot = EnvSnapshot()
        snapshot.stage = stage
        snapshot.name = origin.name
        snapshot.value = origin.value
        snapshot.save()

    @classmethod
    def snapshot_resource(cls, stage: ReleaseTaskProgress, origin: ProjectResource):
        snapshot = ResourceSnapshot()
        snapshot.stage = stage
        snapshot.limits_cpu = origin.limits_cpu
        snapshot.limits_memory = origin.limits_memory
        snapshot.requests_cpu = origin.requests_cpu
        snapshot.requests_memory = origin.requests_memory
        snapshot.replicas = origin.replicas
        snapshot.backoff_limit = origin.backoff_limit
        snapshot.active_deadline_seconds = origin.active_deadline_seconds
        snapshot.save()


    # def listen(self):
    #     config.load_kube_config()
    #     client = KubernetesYamlClient(ApiClient(), self.release_task.render_template)
    #     while not self.event.is_set():
    #         self.event.wait(10)
    #         try:
    #             status = client.get().status
    #             # print(status)
    #             if status.available_replicas == status.replicas:
    #                 self.release_task.state = ReleaseTaskState.COMPLETED
    #                 self.release_task.save()
    #                 return
    #             else:
    #                 self.release_task.state = ReleaseTaskState.FAILED
    #                 self.release_task.save()
    #                 return
    #         except Exception as e:
    #             print(e)
    #             return

class KubernetesBaseRunner(object):
    def __init__(self, instance, force: bool=False):
        self.instance = instance
        self.force = force
        self.tmp_template = None
        if self.instance.is_template == 1:
            self.tmp_template = self.render()
            self.instance.render_template = self.tmp_template
        else:
            self.tmp_template = self.instance.template


    def render(self):
        # todo 渲染configmap模板
        pass

    def execute(self, method: str=""):
        config.load_kube_config()
        client = KubernetesYamlClient(ApiClient(), self.instance.template)
        try:
            ret = client.resource_ensure(method=method)
            if not self.instance.name:
                self.instance.name = ret.metadata.name
            self.instance.save()
            return self.instance
        except Exception as e:
            raise Exception(str(e))


class KubernetesCustomResourceRunner(object):
    def __init__(self, instance: CustomResource, force: bool=False):
        self.instance = instance
        self.force = force
        self.tmp_template = None
        if self.instance.is_template == 1:
            self.tmp_template = self.render()
            self.instance.render_template = self.tmp_template
        else:
            self.tmp_template = self.instance.template


    def render(self):
        # todo 渲染configmap模板
        pass

    def execute(self, method: str=""):
        yaml_obj = yaml.safe_load(self.instance.template)
        name = yaml_obj.get("metadata").get("name")
        if not self.instance.name:
            self.instance.name = name
            self.instance.save()
        crd_instance = CustomResourceDefinition.objects.filter(pk=self.instance.crd_id).first()
        try:
            config.load_kube_config()
            client = KubernetesYamlClient(ApiClient(), self.instance.template, is_cr=True)
            ret = client.custom_resource_ensure(crd_instance,method=method,name=name)
            return self.instance
        except Exception as e:
            raise Exception(str(e))

