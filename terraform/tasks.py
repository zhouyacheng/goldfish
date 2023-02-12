from celery import shared_task
from .models import Terraform
from .runner import TerraformRunner


@shared_task
def execute_task(id: int,action: str="plan"):
    TerraformRunner(id=id,action=action).execute()