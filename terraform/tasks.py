from celery import shared_task
from .models import Terraform,TerraformPlan,TerraformTask
from .runner import TerraformRunner


@shared_task
def execute_task(id: int, task_id: int=None,action: str="plan"):
    instance = TerraformRunner(id=id, task_id=task_id,action=action).execute()
    return instance