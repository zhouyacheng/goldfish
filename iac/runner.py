from .models import Task,MissionState,MissionState,TaskEvent,Stats,TaskState
import ansible_runner
from django.conf import settings
from rest_framework.exceptions import APIException
import zipfile
import tarfile
import shutil
from pathlib import Path
import requests
import socket
from datetime import datetime
from typing import Dict,Optional


mission_state_dict = {
    "runner_on_failed": MissionState.FAILED,
    "runner_on_ok": MissionState.OK,
    "runner_on_skipped": MissionState.SKIPPED,
    "runner_on_unreachable": MissionState.UNREACHABLE,
}

playbook_events_set = {"playbook_on_stats"}
playbook_status_set = {"ok","changed","dark","failures","ignored","processed","rescued","skipped"}


def extract_host(host: str):
    try:
        r = socket.gethostbyname(host)
        return r
    except Exception:
        return None
class BaseEventHandler(object):
    def __init__(self, task: Task):
        self.task = task

    def __call__(self, event,*args, **kwargs):
        if hasattr(self,"on_any"):
            self.on_any(event)
        if event.get("stdout") and hasattr(self,"on_output"):
            self.on_output(event["stdout"])
        if hasattr(self,event["event"]):
            return getattr(self,event["event"])(event["event_data"])
        return True

class ModelEventHandler(BaseEventHandler):
    def _save_event(self,data:dict, state: MissionState):
        host = data.get("remote_addr", data.get("host"))
        ip = host
        if host:
            ip = extract_host(host)
        TaskEvent.objects.create(
            task=self.task,
            state=state,
            play=data.get("play"),
            mission=data.get("task"),
            host=host,
            ip=ip,
            start=datetime.fromisoformat(data.get("start")),
            end=datetime.fromisoformat(data.get("end")),
            duration=data.get("duration"),
            changed=data.get("res").get("changed"),
            detail=data.get("res"),
            play_pattern=data.get("play_pattern"),
            counter=0,
        ).save()

    def runner_on_failed(self,data:dict):
        self._save_event(data,MissionState.FAILED)
        return True

    def runner_on_ok(self,data:dict):
        self._save_event(data,MissionState.OK)
        return True

    def runner_on_skipped(self,data:dict):
        self._save_event(data,MissionState.SKIPPED)
        return True

    def runner_on_unreachable(self,data:dict):
        self._save_event(data,MissionState.UNREACHABLE)
        return True

    def playbook_on_stats(self,data:dict):
        _data = {k: v for k, v in data.items() if k in playbook_status_set}
        state_dict: Dict[str:Stats] = {}
        for k, v in _data.items():
            if v and isinstance(v, dict):
                for host, state in v.items():
                    state_instance: Stats = state_dict.get(host, Stats(task=self.task, host=host,ip=extract_host(host)))
                    setattr(state_instance, k, state)
                    state_dict[host] = state_instance
        for state in state_dict.values():
            state.save()
        return True

    def on_output(self,output:str):
        if output:
            if self.task.output:
                self.task.output = f"{self.task.output}\n{output}"
            else:
                self.task.output = output
            self.task.save()

class TaskRunnerException(APIException):
    status_code = 400

class TaskRunner(object):
    def __init__(self, instance: Task):
        self.instance = instance
        self.work_dir = settings.IAC_WORK_DIR.joinpath(str(self.instance.pk))
        self.private_data_dir = self.work_dir / self.instance.release.repository.name
        # self.work_dir = settings.MEDIA_ROOT.joinpath(instance.repository.extract[0],instance.repository.extract[1].split(".")[0])
        print(f"self.work_dir: {self.work_dir}")
        if not self.work_dir.exists():
            self.work_dir.mkdir(parents=True)
        self.prepare()


    def clear_workdir(self):
        shutil.rmtree(self.work_dir)

    def prepare(self):
        # repository_store = settings.MEDIA_ROOT.joinpath(self.instance.repository.store.name)
        archive_url = self.instance.release.archive_url
        local_archive_url = self.work_dir / archive_url.split("/")[-1]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }

        response = requests.get(archive_url, headers=headers,stream=True)
        if response.status_code != 200:
            return
        else:
            with open(local_archive_url, 'wb') as f:
                f.write(response.raw.read())

        if zipfile.is_zipfile(local_archive_url):
            with zipfile.ZipFile(local_archive_url,"r") as f:
                for name in f.namelist():
                    if name.startswith("/") or ".." in name:
                        raise APIException(detail="非法文件名")
                f.extractall(self.work_dir)
        elif tarfile.is_tarfile(local_archive_url):
            with tarfile.open(local_archive_url,"r") as f:
                for name in f.getnames():
                    if name.startswith("/") or ".." in name:
                        raise TaskRunnerException(detail="非法文件名")
                f.extractall(self.work_dir)
        else:
            raise TaskRunnerException(code=100002,detail="上传文件必须为压缩文件,压缩文件的后缀为.zip和.tar.gz")

        if self.instance.inventories:
            inventory_dir = Path(self.private_data_dir / "inventory")
            inventory_dir.mkdir(parents=True,exist_ok=True)
            with open(inventory_dir / "hosts","w",encoding="utf8") as f:
                f.write(self.instance.inventories)

    def extract_host(self,host:str):
        try:
            r = socket.gethostbyname(host)
            return r
        except Exception:
            return None

    # def on_event(self,event):
    #     _event = event.get("event")
    #     if _event in mission_state_dict.keys():
    #         host = event["event_data"].get("remote_addr",event["event_data"].get("host"))
    #         ip = host
    #         if host:
    #             ip = self.extract_host(host)
    #         TaskEvent.objects.create(
    #             task=self.instance,
    #             state=mission_state_dict[_event],
    #             play=event.get("event_data").get("play"),
    #             mission=event.get("event_data").get("task"),
    #             host=host,
    #             ip=ip,
    #             start=datetime.fromisoformat(event.get("event_data").get("start")),
    #             end=datetime.fromisoformat(event.get("event_data").get("end")),
    #             duration=event.get("event_data").get("duration"),
    #             changed=event.get("event_data").get("res").get("changed"),
    #             detail=event.get("event_data").get("res"),
    #             play_pattern=event.get("event_data").get("play_pattern"),
    #             counter=event.get("counter"),
    #         ).save()
    #     if _event in playbook_events_set:
    #         data = { k:v for k,v in event["event_data"].items() if k in playbook_status_set}
    #         state_dict: Dict[str:Stats] = {}
    #         for k,v in data.items():
    #             if v and isinstance(v, dict):
    #                 for host, state in v.items():
    #                     state_instance: Stats = state_dict.get(host,Stats(task=self.instance,host=host,ip=self.extract_host(host)))
    #                     # state_instance.k = state
    #                     setattr(state_instance,k,state)
    #                     print(k,state)
    #                     state_dict[host] = state_instance
    #         for state in state_dict.values():
    #             state.save()
    #     output = event.get("stdout")
    #     if output:
    #         if self.instance.output:
    #             self.instance.output = f"{self.instance.output}\n{output}"
    #         else:
    #             self.instance.output = output
    #         self.instance.save()
    #     return True

    def execute(self):
        if self.instance.release.is_deleted == 1:
            raise TaskRunnerException(detail="仓库不存在或已被删除")
        print("*" * 50)
        print(self.instance.to_runner_kwargs())
        ansible_runner.run(
            private_data_dir=self.private_data_dir,
            # private_data_dir=self.work_dir.joinpath("helloworld"),
            **self.instance.to_runner_kwargs(),
            finished_callback=self.on_finished_callback,
            status_handler=self.on_status_change,
            event_handler=ModelEventHandler(self.instance),
        )
        return

    def on_status_change(self, status_data, runner_config):
        # print("on_status_change")
        # print(status_data,type(status_data))
        # print(runner_config,type(runner_config))
        match status_data.get("status"):
            case "running" | "starting":
                self.instance.state = TaskState.RUNNING
            case "successful":
                self.instance.state = TaskState.COMPLETED
            case "canceled":
                self.instance.state = TaskState.CANCELED
            case "timeout":
                self.instance.state = TaskState.TIMEOUT
            case "failed":
                self.instance.state = TaskState.FAILED
            case _:
                self.instance.state = TaskState.UNKNOW
        self.instance.save()


    def on_finished_callback(self, runner_obj):
        # print("on_finished_callback")
        # print(runner_obj,type(runner_obj))
        # self.instance.output = runner_obj.stdout.read()
        self.instance.save()
        # self.clear_workdir()
        # print(self.events)
