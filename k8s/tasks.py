import logging
import yaml
from celery import shared_task
from .models import ReleaseTask,ReleaseTaskState,Stage,StageType,ReleaseTaskHistory,ReleaseTaskProgress
from .k8s_client import KubernetesYamlClient
from kubernetes.client import ApiClient
from kubernetes import config
from io import StringIO

@shared_task
def check_build_state(pk: int):
    # release_task = ReleaseTask.objects.filter(pk=pk,state=ReleaseTaskState.RUNNING).first()
    # release_task_history = ReleaseTaskHistory.objects.filter(task__project_id=release_task.project.pk,task_id=release_task.pk,state=ReleaseTaskState.RUNNING).first()
    # release_task_history = ReleaseTaskHistory.objects.filter(pk=pk,state=ReleaseTaskState.RUNNING).first()
    release_task_progress = ReleaseTaskProgress.objects.filter(pk=pk,state=ReleaseTaskState.RUNNING).first()
    release_task = ReleaseTask.objects.filter(pk=release_task_progress.task.pk,state=ReleaseTaskState.RUNNING).first()
    # stage = release_task_progress.stage
    kubeconfig_content = release_task_progress.kubeconfig_content
    context = release_task_progress.context
    config.load_kube_config(config_file=StringIO(kubeconfig_content),context=context)
    try:
        client = KubernetesYamlClient(ApiClient(), yaml.safe_load(release_task.render_template))
        status = client.get().status
        if status.succeeded and status.succeeded > 0:
            release_task.state = ReleaseTaskState.COMPLETED
            release_task.save()
            release_task_progress.state = ReleaseTaskState.COMPLETED
            release_task_progress.save()
        if status.failed and status.failed > 0:
            release_task.state = ReleaseTaskState.FAILED
            release_task.save()
            release_task_progress.state = ReleaseTaskState.FAILED
            release_task_progress.save()
    except Exception as e:
        print(e)
        logging.error(e)
        release_task.state = ReleaseTaskState.FAILED
        release_task.save()
        release_task_progress.state = ReleaseTaskState.FAILED
        release_task_progress.save()

@shared_task
def check_deploy_state(pk: int):
    # release_task = ReleaseTask.objects.filter(pk=pk, state=ReleaseTaskState.RUNNING).first()
    # release_task_history = ReleaseTaskHistory.objects.filter(task_id=release_task.pk,state=ReleaseTaskState.RUNNING).first()
    # release_task_history = ReleaseTaskHistory.objects.filter(pk=pk, state=ReleaseTaskState.RUNNING).first()
    release_task_progress = ReleaseTaskProgress.objects.filter(pk=pk, state=ReleaseTaskState.RUNNING).first()
    release_task = ReleaseTask.objects.filter(pk=release_task_progress.task.pk,state=ReleaseTaskState.RUNNING).first()
    # stage = release_task_progress.stage
    kubeconfig_content = release_task_progress.kubeconfig_content
    context = release_task_progress.context
    # config.load_kube_config()
    config.load_kube_config(config_file=StringIO(kubeconfig_content), context=context)
    try:
        client = KubernetesYamlClient(ApiClient(), yaml.safe_load(release_task.render_template))
        status = client.get().status
        if status.ready_replicas and status.replicas:
            if release_task.observed_generation is None or status.observed_generation > release_task.observed_generation:
                if status.ready_replicas >= status.replicas:
                    release_task.state = ReleaseTaskState.COMPLETED
                    release_task.observed_generation = status.observed_generation
                    release_task.save()
                    release_task_progress.state = ReleaseTaskState.COMPLETED
                    release_task_progress.observed_generation = status.observed_generation
                    release_task_progress.save()
    except Exception as e:
        print(e)
        logging.error(e)
        release_task.state = ReleaseTaskState.FAILED
        release_task.save()
        release_task_progress.state = ReleaseTaskState.FAILED
        release_task_progress.save()

@shared_task
def check_all_release_task_state():
    # todo 应使用ReleaseTaskHistory来查询正在运行的任务
    # for instance in ReleaseTaskHistory.objects.filter(state=ReleaseTaskState.RUNNING):
    for instance in ReleaseTaskProgress.objects.filter(state=ReleaseTaskState.RUNNING):
        if not instance:
            message = "没有正在运行中的任务"
            print(message)
            return message
        if instance.stage_type == StageType.BUILD:
            check_build_state.delay(instance.pk)
        if instance.stage_type == StageType.DEPLOY:
            check_deploy_state.delay(instance.pk)


@shared_task
def check_release_task_state(pk: int):
    pass