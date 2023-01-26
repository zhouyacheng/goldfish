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
from .models import Project,ProjectEnv,Stage,ProjectResource,ReleaseTaskState,ReleaseTask,Pipeline,ReleaseTaskProgress
from .runner import KubernetesRunner


class PipelineViewSet(GenericViewSet):
    queryset = Pipeline.objects.filter(is_deleted=0)
    serializer_class = PipelineModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request,*args, **kwargs):
        serializer = PipelineCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user,updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = PipelineMutationModelSerializer(instance=instance,data=request.data)
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
        instance :Pipeline = self.get_object()
        if Project.objects.filter(pipeline=instance).count() > 0:
            return Response(status=status.HTTP_423_LOCKED)
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(methods=["PUT"],detail=True,url_path="reorder")
    def stage_reorder(self, request: Request,*args, **kwargs):
        serializer = StageOrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            stages = serializer.validated_data["stages"]
            for index, data in enumerate(stages):
                stage = Stage.objects.filter(seq=data).first()
                stage.seq = index + 1
                stage.save()
                return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_200_OK)

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

    def delete(self, request: Request,*args, **kwargs):
        instance :Project = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self,request: Request):
        kw = request.query_params.get("kw")
        if kw:
            q = Q(name__icontains=kw)
            queryset = self.get_queryset().filter(q)
        else:
            queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)



class ProjectEnvViewSet(GenericViewSet):
    queryset = ProjectEnv.objects.filter(is_deleted=0)
    serializer_class = ProjectEnvModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request,*args, **kwargs):
        serializer = ProjectEnvCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user,updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance: ProjectEnv = self.get_object()
        serializer = ProjectEnvMutationModelSerializer(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save(updated_by=request.user,method="update")
            return Response(self.get_serializer(instance=instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request,*args, **kwargs):
        instance :ProjectEnv = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save(method="delete")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self,request: Request , *args, **kwargs):
        kw = request.query_params.get("kw")
        if kw:
            q = Q(name__icontains=kw) | Q(value__icontains=kw)
            queryset = self.get_queryset().filter(q)
        else:
            queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)



class ProjectResourceViewSet(GenericViewSet):
    queryset = ProjectResource.objects.filter(is_deleted=0)
    serializer_class = ProjectResourceModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request,*args, **kwargs):
        serializer = ProjectResourceCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user,updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = ProjectResourceMutationModelSerializer(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, *args, **kwargs):
        instance :ProjectResource = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["GET"],detail=False,url_path="(?P<project_id>\d+)/(?P<stage_id>\d+)")
    def get_by_project_and_stage(self,request: Request , *args, **kwargs):
        project_id = kwargs.get("project_id")
        stage_id = kwargs.get("stage_id")
        if not project_id or not stage_id:
            return Response(data={"message": "urlpath does not receive project_id and stage_id"},status=status.HTTP_400_BAD_REQUEST)
        q = Q(project_id=project_id) & Q(stage_id=stage_id)
        instance = self.get_queryset().filter(q).first()
        return Response(self.get_serializer(instance).data,status=status.HTTP_200_OK)

class StageViewSet(GenericViewSet):
    queryset = Stage.objects.filter(is_deleted=0)
    serializer_class = StageModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request,*args, **kwargs):
        serializer = StageCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            seq = 0
            latest_seq = Stage.objects.filter(pipeline__pk=serializer.validated_data["pipeline"].pk).order_by("-seq").first()
            if latest_seq:
                seq = latest_seq.seq
            seq += 1
            serializer.save(created_by=request.user,updated_by=request.user,seq=seq)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = StageMutationModelSerializer(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request: Request , *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request,*args, **kwargs):
        instance :Stage = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReleaseTaskViewSet(GenericViewSet):
    queryset = ReleaseTask.objects.filter(is_deleted=0)
    serializer_class = ReleaseTaskModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request,*args, **kwargs):
        serializer = ReleaseTaskCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            active_release_task_cnt = ReleaseTask.objects.filter(Q(project=serializer.validated_data.get("project")) & ~Q(state=ReleaseTaskState.CLOSED)).count()
            if active_release_task_cnt > 0:
                return Response({"message": "该流水线已有正在运行的任务,不可重复创建"},status=status.HTTP_409_CONFLICT)
            stage = Stage.objects.filter(pipeline=serializer.validated_data.get("project").pipeline).order_by("seq").first()
            serializer.save(created_by=request.user,updated_by=request.user,current=stage)
            KubernetesRunner.make_snapshot(serializer.instance)
            return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def update(self, request: Request,*args, **kwargs):
        instance: ReleaseTask = self.get_object()
        # stage = Stage.objects.filter(pk=request.query_params.get("stage")).first()
        stage = ReleaseTaskProgress.objects.filter(pk=request.query_params.get("pk")).first()
        try:
            release_task = KubernetesRunner(instance).execute(stage)
            return Response(self.get_serializer(release_task).data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request: Request,*args, **kwargs):
    #     instance: ReleaseTask = self.get_object()
    #     if instance.state == ReleaseTaskState.CLOSED:
    #         return Response({"message": "closed"},status=status.HTTP_400_BAD_REQUEST)
    #     if instance.state == ReleaseTaskState.RUNNING:
    #         return Response({"message": "running"},status=status.HTTP_409_CONFLICT)
    #     next = Stage.objects.order_by("seq").filter(seq__gt=instance.current.seq).first()
    #     current = instance.current
    #     stage = Stage.objects.filter(pk=request.query_params.get("stage")).first()
    #     if stage:
    #         if stage.seq < current.seq:
    #             return Response({"message": "stage < current"}, status=status.HTTP_400_BAD_REQUEST)
    #         if stage.seq == current.seq and instance.state in {ReleaseTaskState.PENDING,ReleaseTaskState.FAILED,ReleaseTaskState.COMPLETED}:
    #             pass
    #         if stage.seq == next.seq and instance.state in {ReleaseTaskState.PENDING,ReleaseTaskState.FAILED}:
    #             pass
    #         return Response({"message": ""},status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         if instance.state in {ReleaseTaskState.PENDING,ReleaseTaskState.FAILED}:
    #             # execute current
    #             pass
    #         if instance.state in {ReleaseTaskState.COMPLETED}:
    #             # execute next
    #             pass
    #     return Response({"message" : "123"}, status=status.HTTP_400_BAD_REQUEST)


    # def update(self, request: Request,*args, **kwargs):
    #     instance: ReleaseTask = self.get_object()
    #     serializer = ReleaseTaskMutationModelSerializer(instance=instance,data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(updated_by=request.user)
    #         return Response(self.get_serializer(instance=serializer.instance).data,status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request: Request, *args, **kwargs):
        instance :ReleaseTask = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request: Request, *args, **kwargs):
        project = request.query_params.get("project")
        if project:
            queryset = self.get_queryset().filter(project_id=int(project))
        else:
            queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    @action(methods=["GET"],detail=True,url_path="history")
    def get_task_history(self, request: Request, *args, **kwargs):
        queryset = ReleaseTaskHistory.objects.filter(is_deleted=0)
        page = self.paginate_queryset(queryset)
        serializer = ReleaseTaskHistoryModelSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    @action(methods=["GET"], detail=True, url_path="progress")
    def get_task_progress(self, request: Request, *args, **kwargs):
        queryset = ReleaseTaskProgress.objects.filter(is_deleted=0)
        page = self.paginate_queryset(queryset)
        serializer = ReleaseTaskProgressModelSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)