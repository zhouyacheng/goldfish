from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from common.paginations import CustomPageNumberPagination
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from django.db.models import Q
from rest_framework.decorators import action
from .runner import TerraformRunner
from .serializers import *
from .models import Terraform,TerraformPlan,TerraformTask
from .tasks import execute_task


class TerraformViewSet(GenericViewSet):
    queryset = Terraform.objects.filter(is_deleted=0)
    serializer_class = TerraformModelSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request: Request,*args, **kwargs):
        # action = "task"
        serializer = TerraformCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user,updated_by=request.user)
            # instance: Terraform = serializer.instance
            # try:
            #     execute_task.delay(id=instance.pk, action=action)
            # except Exception as e:
            #     print(str(e))
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = TerraformMutationModelSerializer(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request: Request , *args, **kwargs):
        name = request.query_params.get("name")
        if name:
            query_set = self.queryset.filter(name__contains=name)
        else:
            query_set = self.queryset
        page = self.paginate_queryset(query_set)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request,*args, **kwargs):
        instance :Terraform = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TerraformPlanViewSet(GenericViewSet):
    queryset = TerraformPlan.objects.filter(is_deleted=0)
    serializer_class = TerraformPlanModelSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request: Request,*args, **kwargs):
        serializer = TerraformPlanCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user,updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = TerraformPlanMutationModelSerializer(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request: Request , *args, **kwargs):
        name = request.query_params.get("name")
        if name:
            query_set = self.queryset.filter(name__contains=name)
        else:
            query_set = self.queryset
        page = self.paginate_queryset(query_set)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request,*args, **kwargs):
        instance :TerraformPlan = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TerraformTaskViewSet(GenericViewSet):
    queryset = TerraformTask.objects.filter(is_deleted=0)
    serializer_class = TerraformTaskModelSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request: Request,*args, **kwargs):
        action = "task"
        terraform_id = request.query_params.get("terraform_id")
        if not terraform_id and int(terraform_id):
            return Response({"message": "url查询字符串terraform_id必须传递,且与上传的terraform任务id相关联"})
        instance = Terraform.objects.filter(pk=int(terraform_id)).first()
        if not instance:
            return Response({"message": "未查询到已注册过的Terraform任务信息"},status=status.HTTP_404_NOT_FOUND)
        task_instance = TerraformTask()
        task_instance.terraform = instance
        task_instance.user = instance.user
        task_instance.project = instance.project
        task_instance.save()
        try:
            execute_task.delay(id=int(terraform_id),task_id=task_instance.pk, action=action)
            return Response({"task_id": task_instance.pk, "message": "任务执行中..."},status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"message": str(e)})

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = TerraformTaskMutationModelSerializer(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request: Request , *args, **kwargs):
        name = request.query_params.get("name")
        if name:
            query_set = self.queryset.filter(name__contains=name)
        else:
            query_set = self.queryset
        page = self.paginate_queryset(query_set)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request,*args, **kwargs):
        action = "destroy"
        terraform_task_id = kwargs.get("pk")
        instance: TerraformTask = self.get_object()
        if not instance:
            return Response({"message": "未查询到已执行过的Terraform任务信息"},status=status.HTTP_404_NOT_FOUND)
        try:
            execute_task.delay(id=instance.terraform.pk,task_id=int(terraform_task_id), action=action)
            return Response({"task_id": terraform_task_id,"message": "资源删除中..."},status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"message": str(e)})


