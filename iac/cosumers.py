import logging
import time
import json
from channels.generic.websocket import WebsocketConsumer,JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from iac.models import Task,TaskState
from iac.serializer import TaskModelSerializer
from threading import Event
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.auth import UserLazyObject

# "ws://localhost:8000/ws/iac/task/5/"
class TaskConsumer(JsonWebsocketConsumer):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._event = Event()
        self.task_id = None
        self.group_name = None

    def encode_task(self,task: Task):
        return TaskModelSerializer(task).data

    def get_task_instance(self) -> Task:
        return Task.objects.filter(pk=self.task_id).first()

    @classmethod
    def get_channel_group_name(cls,task_id):
        return f"iac_task_{task_id}"

    def connect(self,*args,**kwargs):
        logging.warning("client connect")
        logging.warning(self.scope)
        _task_id = self.scope["url_route"]["kwargs"].get("task_id",-1)
        if not _task_id or int(_task_id) < 0:
            return
        self.task_id = int(_task_id)
        logging.warning(f"task_id : {self.task_id}")
        self.group_name = self.get_channel_group_name(self.task_id)
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        self.accept()
        # while not self._event.is_set():
        #     task_instance = self.get_task_instance()
        #     if not task_instance:
        #         self._event.set()
        #         return
        #     data = self.encode_task(task_instance).get("output")
        #     # self.send(json.dumps(data))
        #     self.send_json(data)
        #     logging.warning(data)
        #     # if task_instance.state not in {TaskState.PENDING, TaskState.RUNNING,TaskState.FAILED,TaskState.COMPLETED}:
        #     if task_instance.state not in {TaskState.PENDING, TaskState.RUNNING}:
        #         logging.warning(f"task_instance.state: {task_instance.state}")
        #         self.close()
        #         self._event.set()
        #         return
        #
        #     self._event.wait(10)
            # time.sleep(10)

    def disconnect(self, code):
        logging.warning(f"client disconnect with {code}")
        # self._event.set()
        # self.close()
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)

    def receive_json(self, text_data :str =None, bytes_data=None):
        # logging.info(f"receive data {text_data} {type(text_data)} {bytes_data} {type(bytes_data)}")
        # self.send(text_data.upper())
        logging.warning(f"receive data {text_data} {type(text_data)}")
        self.send(text_data.upper())


    def on_task_changed(self,data):
        # logging.warning(data)
        task_instance = self.get_task_instance()
        if not task_instance:
            self.close()
            return
        data = self.encode_task(task_instance).get("output")
        # self.send(json.dumps(data))
        self.send_json(data)
        # if task_instance.state not in {TaskState.PENDING, TaskState.RUNNING,TaskState.FAILED,TaskState.COMPLETED}:
        if task_instance.state not in {TaskState.PENDING, TaskState.RUNNING}:
            logging.warning(f"task_instance.state: {task_instance.state}")
            self.close()
            return


class AsyncTaskConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._event = Event()
        self.task_id = None
        self.group_name = None

    @database_sync_to_async
    def encode_task(self,task: Task):
        return TaskModelSerializer(task).data

    @database_sync_to_async
    def get_task_instance(self) -> Task:
        return Task.objects.filter(pk=self.task_id).first()

    async def get_channel_group_name(self,task_id):
        return f"iac_task_{task_id}"

    async def connect(self):
        logging.warning("client connect")
        logging.warning(self.scope)

        self.task_id = int(self.scope["url_route"]["kwargs"].get("task_id"))
        logging.warning(f"task_id : {self.task_id}")
        self.group_name = await self.get_channel_group_name(self.task_id)
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()
        # while not self._event.is_set():
        #     task_instance = self.get_task_instance()
        #     if not task_instance:
        #         self._event.set()
        #         return
        #     data = self.encode_task(task_instance).get("output")
        #     # self.send(json.dumps(data))
        #     self.send_json(data)
        #     logging.warning(data)
        #     # if task_instance.state not in {TaskState.PENDING, TaskState.RUNNING,TaskState.FAILED,TaskState.COMPLETED}:
        #     if task_instance.state not in {TaskState.PENDING, TaskState.RUNNING}:
        #         logging.warning(f"task_instance.state: {task_instance.state}")
        #         self.close()
        #         self._event.set()
        #         return
        #
        #     self._event.wait(10)
            # time.sleep(10)

    async def disconnect(self, code):
        logging.warning(f"client disconnect with {code}")
        # self._event.set()
        # self.close()
        await self.channel_layer.group_discard(self.group_name,self.channel_name)

    # def receive_json(self, text_data :str =None, bytes_data=None):
    #     # logging.info(f"receive data {text_data} {type(text_data)} {bytes_data} {type(bytes_data)}")
    #     # self.send(text_data.upper())
    #     logging.warning(f"receive data {text_data} {type(text_data)}")
    #     self.send(text_data.upper())


    async def on_task_changed(self,data):
        # logging.warning(data)
        task_instance = await self.get_task_instance()
        if task_instance:
            data = await self.encode_task(task_instance)
            await self.send_json(data)
            # if task_instance.state not in {TaskState.PENDING, TaskState.RUNNING,TaskState.FAILED,TaskState.COMPLETED}:
            if task_instance.state not in {TaskState.PENDING, TaskState.RUNNING}:
                logging.warning(f"task_instance.state: {task_instance.state}")
                await self.close()
                return

