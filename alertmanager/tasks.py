from celery import shared_task
from libs.yuntongxun.sms import CCP
from codebox import constant

@shared_task
def send_message(mobile: int, message: str):
    try:
        ccp = CCP()
        ret = ccp.send_template_sms(mobile, [message, constant.SMS_EXPIRE_TIME // 60], constant.SMS_TEMPLATE_ID)
        print(ret)
    except Exception as e:
        print(str(e))