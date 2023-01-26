from django.urls import re_path

from iac.cosumers import TaskConsumer,AsyncTaskConsumer

websocket_urlpatterns = [
    # re_path(r"ws/iac/task/(?P<task_id>\d+)/",TaskConsumer.as_asgi()),
    re_path(r"ws/iac/task/(?P<task_id>\d+)/",AsyncTaskConsumer.as_asgi()),
]