import json
import urllib.parse
import threading
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.generics import ListAPIView,RetrieveAPIView,GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.conf import settings
from django.contrib.auth.models import User,AnonymousUser
from rest_framework.permissions import IsAuthenticated
from common.paginations import CustomPageNumberPagination
from .models import Task,TaskState , Repository,Template,Release,TaskEvent,Stats,PeriodTask
from .serializer import PeriodTaskSummaryModelSerializer,PeriodTaskModelSerializer,PeriodTaskCreationModelSerializer,PeriodTaskMutationSerializer,StatsModelSerializer,TaskEventModelSerializer,ReleaseModelSerializer,ReleaseModelSummarySerializer,TaskModelSerializer,RepositoryModelSerializer,TaskModelSummarySerializer,TemplateModelSerializer,TemplateCreationModelSerializer,TemplateMutationSerializer
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .runner import TaskRunner
from django.utils import timezone
from django.db.models import Q
from rest_framework.decorators import action
from gitea import ApiClient,Configuration,RepositoryApi
from packaging.version import Version
from urllib.parse import urlparse
from .repositories import GiteaRepositoryProvider
from .tasks import execute_task, sync_gitea_release,sync_all_release




class RepositoryViewSet(GenericViewSet):
    queryset = Repository.objects.filter(is_deleted=0)
    serializer_class = RepositoryModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user,updated_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request,*args, **kwargs):
        instance :Repository = self.get_object()
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
            q = Q(name__icontains=kw) | Q(owner__icontains=kw)
            queryset = self.get_queryset().filter(q)
        else:
            queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    @action(methods=["GET"],detail=True,url_path="releases")
    def releases(self,request: Request,*args, **kwargs):
        instance: Repository = self.get_object()
        queryset = Release.objects.filter(repository=instance)
        kw = request.query_params.get("kw")
        if kw:
            try:
                version = Version(kw)
                release = version.release
                if len(release) == 1:
                    queryset = queryset.filter(major=version.major)
                elif len(release) == 2:
                    queryset = queryset.filter(major=version.major,minor=version.minor)
                elif len(release) == 3:
                    queryset = queryset.filter(major=version.major,minor=version.minor,micro=version.micro)
                else:
                    return Response({"message": "版本信息不合法"})
            except:
                pass
        res = self.paginate_queryset(queryset)
        return self.get_paginated_response(ReleaseModelSummarySerializer(res,many=True).data)

    # def _sync_relesaes(self, request ,instance: Repository, user_id):
    #     # provider = GiteaRepositoryProvider(token=instance.token, url=instance.url)
    #     latest_release_instance: Release = Release.objects.first()
    #     lower = None
    #     if latest_release_instance:
    #         lower = latest_release_instance.version
    #
    #     try:
    #         for tag in instance.provider.tags(lower=lower):
    #             Release.objects.create(
    #                 repository=instance,
    #                 archive_url=tag.archive_url,
    #                 commit=tag.commit,
    #                 major=tag.version.major,
    #                 minor=tag.version.minor,
    #                 micro=tag.version.micro,
    #                 created_by_id=user_id,
    #                 updated_by_id=user_id,
    #             ).save()
    #     except (ValueError,Exception) as e:
    #         print(str(e))
    #         return str(e)
    @releases.mapping.put
    def sync_releases(self,request: Request,*args, **kwargs):
        instance: Repository = self.get_object()
        user = request.user.id
        if not request.user:
            user = AnonymousUser.id
        # sync_gitea_release.delay(instance.pk,user)
        sync_all_release.delay(instance.pk,user)
        # threading.Thread(target=self._sync_relesaes,args=(request,instance,user),daemon=True).start()
        return Response({"message": "ok"},status=status.HTTP_204_NO_CONTENT)

    @action(methods=["POST","GET","PUT"],detail=True,permission_classes=[],url_path="webhook",url_name="webhook")
    def webhook(self,request: Request,*args, **kwargs):
        import socket
        # "html_url": "http://node01:3000/17600192707/helloworld",
        url :str = request.data.get("repository",{}).get("html_url")
        hostname = urlparse(url).hostname
        ip = socket.gethostbyname(hostname)
        parsed_url = url.replace(hostname,ip)
        # instance: Repository = Repository.objects.filter(url=parsed_url).first()
        instance: Repository = self.get_object()
        user = request.user.id
        if not request.user:
            user = AnonymousUser.id
        # sync_gitea_release.delay(instance.pk, user)
        sync_all_release.delay(instance.pk, user)
        # threading.Thread(target=self._sync_relesaes, args=(request, instance), daemon=True).start()
        return Response({"message": "ok"}, status=status.HTTP_204_NO_CONTENT)

class TaskViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ["id","create_time"]

    def list(self,request: Request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = TaskModelSummarySerializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def update(self, request: Request, *args, **kwargs):
        instance: Task = self.get_object()
        new_instance = Task.objects.create(
            release=instance.release,
            playbook=instance.playbook,
            inventories=instance.inventories,
            forks=instance.forks,
            timeout=instance.timeout,
            envvars=instance.envvars,
            extravars=instance.extravars,
            created_by=request.user,
            updated_by=request.user,
        )
        # serializer = self.serializer_class(instance=new_instance)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        execute_task.delay(new_instance.pk)
        # runner = TaskRunner(instance=new_instance)
        # _, runner = runner.execute()
        return Response({"status": new_instance.state, 'output': new_instance.output})
            # return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = TaskModelSummarySerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request: Request,*args,**kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance: Task = serializer.save(created_by=request.user,updated_by=request.user)
                execute_task.delay(instance.pk)
                # runner = TaskRunner(instance=instance)
                # _,runner = runner.execute()
                return Response({"status": instance.state,'output': instance.output})
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["GET"],detail=True,url_path="stats")
    def get_stats(self,request: Request,*args,**kwargs):
        instance = self.get_object()
        stats = Stats.objects.filter(task=instance)
        return Response(StatsModelSerializer(instance=stats,many=True).data,status=status.HTTP_200_OK)


class TemplateViewSet(GenericViewSet):
    queryset = Template.objects.filter(is_deleted=0)
    serializer_class = TemplateModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request, *args, **kwargs):
        serializer = TemplateCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user, updated_by=request.user)
            return Response(self.serializer_class(serializer.instance).data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = TemplateMutationSerializer(instance=instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(self.serializer_class(serializer.instance).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, *args, **kwargs):
        instance: Repository = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.deleted_by = request.user
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request: Request):
        kw = request.query_params.get("kw")
        if kw:
            queryset = self.get_queryset().filter(name__icontains=kw)
        else:
            queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

class ReleaseViewSet(GenericViewSet):
    queryset = Release.objects.filter(is_deleted=0)
    serializer_class = ReleaseModelSerializer
    # serializer_class = RepositoryModelSerializer
    permission_classes = [IsAuthenticated]

    # def create(self, request: Request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(created_by=request.user, updated_by=request.user)
    #         return Response(ReleaseModelSummarySerializer(serializer.instance).data,status=status.HTTP_200_OK)
    #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    # def update(self, request: Request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.serializer_class(instance=instance, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(updated_by=request.user)
    #         return Response(ReleaseModelSummarySerializer(serializer.instance).data, status=status.HTTP_200_OK)
    #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request: Request, *args, **kwargs):
    #     instance: Repository = self.get_object()
    #     instance.delete_time = timezone.now()
    #     instance.is_deleted = 1
    #     instance.deleted_by = request.user
    #     instance.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)

        return Response(ReleaseModelSummarySerializer(serializer.instance).data, status=status.HTTP_200_OK)

    # def list(self, request: Request):
    #     queryset = self.get_queryset()
    #     page = self.paginate_queryset(queryset)
    #     serializer = self.serializer_class(page, many=True)
    #
    #     return self.get_paginated_response(ReleaseModelSummarySerializer(serializer.instance).data)

    # @action(methods=["GET"], detail=True, url_path="releases")
    # def releases(self, request: Request, *args, **kwargs):
    #     instance: Repository = self.get_object()
    #     queryset = Release.objects.filter(repository=instance)
    #     res = self.paginate_queryset(queryset)
    #     return self.get_paginated_response(ReleaseModelSummarySerializer(res, many=True).data)

    # def _sync_relesaes(self, request, instance: Repository):
    #     provider = GiteaRepositoryProvider(token=instance.token, url=instance.url)
    #     latest_release_instance: Release = Release.objects.first()
    #     lower = None
    #     if latest_release_instance:
    #         lower = latest_release_instance.version
    #     try:
    #         for tag in provider.tags(lower=lower):
    #             Release.objects.create(
    #                 repository=instance,
    #                 archive_url=tag.archive_url,
    #                 commit=tag.commit,
    #                 major=tag.version.major,
    #                 minor=tag.version.minor,
    #                 micro=tag.version.micro,
    #                 created_by=request.user,
    #                 updated_by=request.user,
    #             ).save()
    #     except (ValueError, Exception) as e:
    #         print(str(e))
    #         return str(e)
    #
    # def sync_releases(self, request: Request, *args, **kwargs):
    #     instance: Repository = self.get_object()
    #     threading.Thread(target=self._sync_relesaes, args=(request, instance), daemon=True).start()
    #     return Response({"message": "ok"}, status=status.HTTP_204_NO_CONTENT)



class TaskEventViewSet(GenericViewSet):
    queryset = TaskEvent.objects.all()
    serializer_class = TaskEventModelSerializer
    permission_classes = [IsAuthenticated]


    def retrieve(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request: Request):
        kw = request.query_params.get("kw")
        if kw:
            q = Q(host__icontains=kw) | Q(ip__icontains=kw)
            queryset = self.get_queryset().filter(q)
        else:
            queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

class PeriodTaskViewSet(GenericViewSet):
    queryset = PeriodTask.objects.filter(is_deleted=0)
    serializer_class = PeriodTaskSummaryModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request,*args, **kwargs):
        serializer = PeriodTaskCreationModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(created_by=request.user,updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = PeriodTaskMutationSerializer(instance=instance,data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(updated_by=request.user)
            return Response(self.get_serializer(instance=serializer.instance).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request,*args, **kwargs):
        instance :PeriodTask = self.get_object()
        instance.delete_time = timezone.now()
        instance.is_deleted = 1
        instance.enabled = 0
        instance.deleted_by = request.user
        # instance.beat.delete()
        # instance.beat.save()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request: Request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self,request: Request):
        kw = request.query_params.get("kw")
        if kw:
            q = Q(name__icontains=kw) | Q(owner__icontains=kw)
            queryset = self.get_queryset().filter(q)
        else:
            queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)
