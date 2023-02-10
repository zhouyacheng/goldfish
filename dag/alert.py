import os
import requests

from abc import ABCMeta, abstractmethod

class Alert(metaclass=ABCMeta):
    # todo
    # 后续用工厂模式封装
    @abstractmethod
    def execute(self):
        pass

class DingdingAlert(Alert):
    def __init__(
        self,
        task_id: str,
        dingding_robot_url: str,
        message_type: str,
        message: str,
        at_all: bool,
    ):
        self.task_id = task_id
        self.dingding_robot_url = dingding_robot_url
        self.message_type = message_type
        self.message = message
        self.at_all = at_all
        self.task_id = task_id
        self.times = 3

    def execute(self):
        alert_object = False if not self.at_all else True
        try:
            for i in range(self.times):
                self.request_headers = {"Content-Type": "application/json"}
                self.request_body = {
                    "at": {"atMobiles": [], "atUserIds": [], "isAtAll": alert_object},
                    "msgtype": self.message_type,
                    "text": {
                        "content": self.message,
                    },
                }
                res = requests.post(
                    url=self.dingding_robot_url,
                    headers=self.request_headers,
                    json=self.request_body,
                )
                if res.status_code == 200:
                    break
        except Exception as e:
            self.request_body = {
                "at": {"atMobiles": [], "atUserIds": [], "isAtAll": alert_object},
                "msgtype": self.message_type,
                "text": {"content": str(e)},
            }
            print(e)
            requests.post(
                url=self.dingding_robot_url,
                headers=self.request_headers,
                json=self.request_body,
            )


class WechatAlert(Alert):
    def __init__(
        self,
        task_id: str,
        wechat_robot_url: str,
        message_type: str,
        message: str,
        at_all: bool,
    ):
        self.task_id = task_id
        self.wechat_robot_url = wechat_robot_url
        self.message_type = message_type
        self.message = message
        self.at_all = at_all
        self.task_id = task_id
        self.times = 3

    def execute(self):
        alert_object = "" if not self.at_all else "@all"
        try:
            for i in range(self.times):
                self.request_headers = {"Content-Type": "text/plain"}
                self.request_body = {
                    "msgtype": self.message_type,
                    "text": {
                        "content": self.message,
                        "mentioned_mobile_list": [alert_object],
                    },
                }
                res = requests.post(
                    url=self.wechat_robot_url,
                    headers=self.request_headers,
                    json=self.request_body,
                )
                if res.status_code == 200:
                    break
        except Exception as e:
            self.request_body = {
                "msgtype": self.message_type,
                "text": {"content": str(e), "mentioned_mobile_list": [alert_object]},
            }
            print(e)
            requests.post(
                url=self.wechat_robot_url,
                headers=self.request_headers,
                json=self.request_body,
            )


def failure_callback(context):
    print("failure_callback")
    message = (
        "AIRFLOW TASK FAILURE TIPS:\n"
        "DAG:    {}\n"
        "TASKS:  {}\n"
        "Reason: {}\n".format(
            context["task_instance"].dag_id,
            context["task_instance"].task_id,
            context["exception"],
        )
    )
    WechatAlert(
        task_id="failure_callback",
        wechat_robot_url=os.environ.get("wechat_robot_url"),
        message_type="text",
        message=message,
        at_all=True,
    ).execute()
    DingdingAlert(
        task_id="failure_callback",
        dingding_robot_url=os.environ.get("dingding_robot_url"),
        message_type="text",
        message=message,
        at_all=True,
    ).execute()


def success_callback(context):
    message = (
        "AIRFLOW TASK SUCCESS TIPS:\n"
        "DAG:    {}\n"
        "TASKS:  {}\n".format(
            context["task_instance"].dag_id, context["task_instance"].task_id
        )
    )
    WechatAlert(
        task_id="success_callback",
        wechat_robot_url=os.environ.get("wechat_robot_url"),
        message_type="text",
        message=message,
        at_all=False,
    ).execute()
    DingdingAlert(
        task_id="success_callback",
        dingding_robot_url=os.environ.get("dingding_robot_url"),
        message_type="text",
        message=message,
        at_all=False,
    ).execute()


def retry_callback(context):
    message = (
        "AIRFLOW TASK RETRY TIPS:\n"
        "DAG:    {}\n"
        "TASKS:  {}\n"
        "Reason: {}\n".format(
            context["task_instance"].dag_id,
            context["task_instance"].task_id,
            context["exception"],
        )
    )
    WechatAlert(
        task_id="retry_callback",
        wechat_robot_url=os.environ.get("wechat_robot_url"),
        message_type="text",
        message=message,
        at_all=False,
    ).execute()
    DingdingAlert(
        task_id="retry_callback",
        dingding_robot_url=os.environ.get("dingding_robot_url"),
        message_type="text",
        message=message,
        at_all=False,
    ).execute()