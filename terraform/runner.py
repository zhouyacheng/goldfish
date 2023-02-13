import os
import shutil
import sys
import subprocess
import zipfile
import tarfile
from rest_framework.exceptions import APIException
from .models import TerraformPlan,TerraformTask,Terraform
from django.conf import settings


class TerraformRunnerException(APIException):
    status_code = 400

class TerraformRunner(object):
    MEDIA_ROOT = settings.MEDIA_ROOT
    TERRAFORM_WORK_DIR = settings.TERRAFORM_WORK_DIR

    def __init__(self ,id: int, task_id: int,action: str="plan"):
        self.id = id
        self.task_id = task_id
        self.instance: Terraform = Terraform.objects.filter(pk=id).first()
        self.action = action
        if self.action == "plan":
            self.model = TerraformPlan
        else:
            self.model = TerraformTask
        self.task_instance: TerraformPlan|TerraformTask = self.model.objects.get(pk=task_id)
        self.work_dir = self.TERRAFORM_WORK_DIR.joinpath(self.action, str(self.task_instance.pk))
        if self.action == "destroy":
            self.work_dir = self.TERRAFORM_WORK_DIR.joinpath("task", str(self.task_id))
        if not self.work_dir.exists():
            self.work_dir.mkdir(parents=True)


    def execute(self):

        # print(f"self.work_dir: {self.work_dir}/{self.instance.name}")
        if self.action == "plan":
            self.command = f"cd {self.work_dir}/{self.instance.name} && /usr/local/Cellar/terraform/1.0.11/bin/terraform plan"
        elif self.action == "task":
            self.command = f"cd {self.work_dir}/{self.instance.name} && /usr/local/Cellar/terraform/1.0.11/bin/terraform apply -auto-approve"
        elif self.action == "destroy":
            self.command = f"cd {self.work_dir}/{self.instance.name} && /usr/local/Cellar/terraform/1.0.11/bin/terraform destroy -auto-approve"
            ret = self.exec_command(self.command)
            self.task_instance.destroy_error_code = ret[0]
            self.task_instance.destroy_error_message = ret[1]
            self.task_instance.destroy_result = ret[1]
            self.task_instance.save()
            return self.task_instance
        self.prepare()
        self.init_terraform_workdir()
        ret = self.exec_command(self.command)
        # print(ret[0])
        # print(ret[1])
        self.task_instance.error_code = ret[0]
        self.task_instance.error_message = ret[1]
        self.task_instance.result = ret[1]
        self.task_instance.save()
        return self.task_instance
        # self.clean_up_workdir()


    def init_terraform_workdir(self):
        http_proxy = os.environ.get("http_proxy")
        https_proxy = os.environ.get("https_proxy")
        if https_proxy and http_proxy:
            proxy = f"export https_proxy={https_proxy} http_proxy={http_proxy}"
            init_command = f"cd {self.work_dir}/{self.instance.name} && {proxy} && /usr/local/Cellar/terraform/1.0.11/bin/terraform init"
        else:
            init_command = f"cd {self.work_dir}/{self.instance.name} && export https_proxy=http://127.0.0.1:8234 http_proxy=http://127.0.0.1:8234 && /usr/local/Cellar/terraform/1.0.11/bin/terraform init"
        # print(f"init_command: {init_command}")
        ret = self.exec_command(init_command)

        self.task_instance.init_error_code = ret[0]
        self.task_instance.init_error_message = ret[1]
        self.task_instance.init_result = ret[1]
        self.task_instance.save()

    def prepare(self):
        archive_dir = self.MEDIA_ROOT.joinpath(self.instance.store.name)
        # print(f"archive_dir: {archive_dir}")
        if zipfile.is_zipfile(archive_dir):
            with zipfile.ZipFile(archive_dir, "r") as f:
                for name in f.namelist():
                    if name.startswith("/") or ".." in name:
                        raise APIException(detail="非法文件名")
                f.extractall(self.work_dir)
        elif tarfile.is_tarfile(archive_dir):
            with tarfile.open(archive_dir, "r") as f:
                for name in f.getnames():
                    if name.startswith("/") or ".." in name:
                        raise APIException(detail="非法文件名")
                f.extractall(self.work_dir)
        else:
            raise TerraformRunnerException(code=100002,
                                  detail="上传文件必须为压缩文件,压缩文件的后缀为.zip和.tar.gz")

    def save(self):
        pass


    def exec_command(self,command: str):
        # message = "An error occurred while running the task"
        try:
            ret = subprocess.getstatusoutput(command)
            if ret[0] != 0:
                print(ret[1])
                sys.exit(ret[0])
            return ret
        except Exception as e:
            print(str(e))

    def clean_up_workdir(self):
        shutil.rmtree(self.work_dir)



    # "/usr/local/Cellar/terraform/1.0.11/bin/terraform destroy -auto-approve"