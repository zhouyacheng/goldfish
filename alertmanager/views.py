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
from .serializers import *
from .models import AlertManager,Project
from .tasks import send_message


class ProjectViewSet(GenericViewSet):
    queryset = Project.objects.filter(is_deleted=0)
    serializer_class = ProjectModelSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request: Request,*args, **kwargs):
        serializer = ProjectCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user,updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = ProjectMutationModelSerializer(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request: Request , *args, **kwargs):
        pipeline = request.query_params.get("pipeline")
        if pipeline:
            query_set = self.queryset.filter(name__contains=pipeline)
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
        instance :Project = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlertManagerViewSet(GenericViewSet):
    queryset = AlertManager.objects.filter(is_deleted=0)
    serializer_class = AlertManagerModelSerializer
    permission_classes = [IsAuthenticated]


    @action(methods=["POST"],detail=False ,url_path="receive")
    def resolve_request(self, request: Request,*args, **kwargs):
        project_name = request.data.get("project")
        project_instance = Project.objects.filter(name=project_name).first()
        if not project_instance:
            return Response({"message": f"不存在对应的 {project_name},请到对应页面添加或修改项目名"})
        resolve_data = {
            "project" : project_instance.pk,
            "receiver" : request.data.get("receiver"),
            "job" : request.data.get("commonLabels").get("job"),
            "fingerprint" : request.data.get("alerts")[0].get("fingerprint"),
            "status" : request.data.get("status"),
            "alertname" : request.data.get("commonLabels").get("alertname"),
            "instance" : request.data.get("commonLabels").get("instance"),
            "description" : request.data.get("commonAnnotations").get("description"),
            "summary" : request.data.get("commonAnnotations").get("summary"),
            "severity" : request.data.get("commonLabels").get("severity"),
            "groupkey" : request.data.get("groupKey"),
        }
        kwargs["resolve_data"] = resolve_data
        return self.create(request, *args, **kwargs)

    def create(self, request: Request,*args, **kwargs):
        # serializer = AlertManagerCreationModelSerializer(data=request.data)
        serializer = AlertManagerCreationModelSerializer(data=kwargs["resolve_data"])
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user,updated_by=request.user)
            instance: AlertManager = serializer.instance
            if instance.severity == "critical":
                message = f"instance: {instance.instance}, status: {instance.status}, alertname: {instance.alertname}, description: {instance.description}"
                send_message.delay(request.user.first_name, message)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = AlertManagerMutationModelSerializer(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request: Request , *args, **kwargs):
        pipeline = request.query_params.get("pipeline")
        if pipeline:
            query_set = self.queryset.filter(name__contains=pipeline)
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
        instance :AlertManager = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


