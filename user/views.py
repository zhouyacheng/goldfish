from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView,UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserModelSerializers
from utils.paginations import CustomPageNumberPagination
from rest_framework.decorators import action


class UserModelViewSet(ModelViewSet):
    # queryset = User.objects.all()
    queryset = UserProfile.objects.all()
    serializer_class = UserModelSerializers
    filter_backends = [DjangoFilterBackend]
    # filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ('username',)
    # ordering_fields = ("username")
    # filter_fields = ("id","username")
    # ordering_fields = ("id","username")
    pagination_class = CustomPageNumberPagination

    # def get_queryset(self):
    #     query_param = self.request.query_params.get("username","")
    #     qs = super().get_queryset()
    #     if query_param:
    #         qs = super().get_queryset().filter(username__icontains=query_param)
    #     return qs

    # def partial_update(self, request, *args, **kwargs):
    #     print("+" * 50)
    #     print(request.data)
    #     return super().partial_update(request,*args, **kwargs)

    def update(self, request, *args, **kwargs):
        print("=" * 50)
        print(request.data)
        return super().update(request, *args, **kwargs)


    @action(["GET"],detail=False)
    def whoami(self,request):
        return Response(data={"user": {"id": request.user.pk , "username": request.user.username}})


    @action(["POST"],detail=True)
    def reset_password(self,request,pk=None):
        try:
            user = User.objects.get(pk=pk)
        except Exception as e:
            raise ValueError("未查询到对应用户")
        old_password = request.data.get("old_password")
        password = request.data.get("password","1")
        confirm_password = request.data.get("confirm_password","2")
        if password != confirm_password:
            return Response({"message": "密码输入不一致"})
        if user.check_password(old_password):
            user.set_password(password)
            user.save()
            return Response({"message": "密码重置成功"})
        return Response({"message": "旧密码校验未通过"})


class MenuItem(dict):
    def __init__(self,id,name,path=None):
        super().__init__()
        self['id'] = id
        self['name'] = name
        self['path'] = path
        self['children'] = []

    def append(self,item):
        self['children'].append(item)

@api_view(["GET"])
# @permission_classes([IsAuthenticated,IsAdminUser])
def menulist_view(request: Request):
    menulist = []
    # print(request.user)
    # print(request.auth)
    # print(request.user.is_superuser)
    if request.user.is_superuser:
        item = MenuItem(1,'用户管理')
        item.append(MenuItem(101,'用户列表','/users'))
        item.append(MenuItem(102,'角色列表','/users/roles'))
        item.append(MenuItem(103,'权限列表','/users/perms'))
        menulist.append(item)
    item = MenuItem(2, '堡垒机')
    item.append(MenuItem(201, '服务器列表', '/bastion/servers'))
    item.append(MenuItem(202, '数据库列表', '/bastion/databases'))
    item.append(MenuItem(203, '登录列表', '/bastion/login'))
    menulist.append(item)

    return Response(menulist)