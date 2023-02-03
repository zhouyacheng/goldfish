from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Organization,Host
from .serializers import OrganizationSerializer,HostSerializer
from rest_framework.decorators import action,api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.files.uploadedfile import InMemoryUploadedFile
from pathlib import Path
from datetime import datetime,timedelta,timezone
from uuid import uuid4
from typing import List
from django.conf import settings
from django.db.transaction import atomic
import pytz
import os
import paramiko
from common.models import File
from .tasks import load_server_to_mysql
# Create your views here.

class OrganizationModelViewSet(ModelViewSet):
    queryset = Organization.objects.all().filter(is_deleted=0)
    serializer_class = OrganizationSerializer



    @action(methods=["GET"],detail=False)
    def all(self,request):
        results = []
        nodes = {}
        for o in self.get_queryset().filter(is_deleted=0).order_by("level"):
            pid = o.parent_id
            id = o.id

            data = self.serializer_class(o).data
            data.setdefault("children", [])
            nodes[id] = data
            if pid:
                nodes[pid]["children"].append(data)
            else:
                results.append(data)
        return Response(data={"results": results},status=status.HTTP_200_OK)

    # @action(methods=["DELETE"],detail=False)
    # def delete_node(self, request: Request, *args, **kwargs):
    #     node_set = set()
    #     node_id = int(request.query_params.get("node_id"))
    #     node_set.add(node_id)
    #     # obj = self.get_queryset().get(id=node_id)
    #     # obj.is_deleted = 1
    #     # obj.save()
    #     for o in self.get_queryset().filter(is_deleted=0):
    #         if o.parent_id and o.parent_id in node_set:
    #             node_set.add(o.id)
    #             # o.is_deleted = 1
    #             # o.save()
    #     self.get_queryset().filter(id__in=node_set).update(is_deleted=1)
    #     #     elif pid and pid not in node_set:
    #     #         nodes[pid]["children"].append(data)
    #     #     else:
    #     #         results.append(data)
    #     # print(node_set)
    #     # return Response(data={"results": results}, status=status.HTTP_204_NO_CONTENT)
    #     return Response(data={"results": "删除成功"}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request: Request, *args, **kwargs):
        node_set = set()
        node_id = int(kwargs.get("pk"))
        node_set.add(node_id)
        with atomic():
            for obj in self.get_queryset().filter(is_deleted=0):
                if obj.parent_id in node_set:
                    node_set.add(obj.id)
            self.get_queryset().filter(id__in=node_set).update(is_deleted=1)
        return Response(data={"results": "删除成功"}, status=status.HTTP_204_NO_CONTENT)



class HostModelViewSet(ModelViewSet):
    queryset = Host.objects.filter(is_deleted=0)
    serializer_class = HostSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["org"]


@api_view(["POST"])
def remote_ssh(request:Request, *args, **kwargs):
    commands = request.data.get("commands")
    ip = request.data.get("ip")
    user = request.data.get("user")
    port = 22
    print(f"commands: {commands}")
    obj = Host.objects.get(ip=ip,user=user)
    private = paramiko.RSAKey.from_private_key_file(obj.ssh_private_key_path)
    trans = paramiko.Transport((ip, port))
    trans.connect(username=user, pkey=private)

    # ssh通信
    ssh = paramiko.SSHClient()
    # 绑定链接
    ssh._transport = trans

    # 执行shell命令
    # stdin, stdout, stderror = ssh.exec_command('top -bw 500 -n 1')
    for command in commands:
        stdin, stdout, stderror = ssh.exec_command(command)
        # 打印命令输入后的结果
        print(stdout.read().decode('utf-8'))
        # 打印报错信息
        print(stderror.read().decode('utf-8'))
    trans.close()
    return Response({"result": "ok"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload(request:Request):
    """
    1.文件大小判断
    2.文件类型检测
    3.图片缩略图
    4.
    :param request:
    :return:
    """
    # 上传的文件大小最大限制,单位M
    fileinfo_dict = {}
    file_maximum = 1
    files = request.FILES.getlist("file")
    if len(files) > 3:
        return Response({"result": f"最多支持同时上传3个文件"})
    for file in files:
        # print(file,type(file),len(file))
        if file.size >= 1024 * 1024 * file_maximum:
            return Response({"message": f"文件大小超过{file_maximum}M限制"})
        upload_root_path = settings.JUMPSERVER_UPLOADS_DIR
        # parent_path = datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y%m%d%H%M%S")
        parent_path = datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y%m%d%H%M")
        uuid = uuid4().hex
        filename = Path(uuid)
        sub_path = upload_root_path / parent_path
        if not os.path.exists(sub_path):
            sub_path.mkdir(parents=True,exist_ok=True)

        with open(sub_path / filename ,"wb",) as f:
            for chunk in file.chunks():
                f.write(chunk)
        fileinfo_dict[uuid] = {}
        fileinfo_dict[uuid]["filename"] = file.name
        fileinfo_dict[uuid]["filepath"] = str(parent_path / filename)
    return Response({"result": "ok", "fileinfo": fileinfo_dict})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def private_key_upload(request:Request,*args,**kwargs):
    """
    1.文件大小判断
    2.文件类型检测
    3.图片缩略图
    4.
    :param request:
    :return:
    """
    # 上传的文件大小最大限制,单位M
    fileinfo_dict = {}
    file_maximum = 1
    files = request.FILES.getlist("file")
    ip = request.data.get("ip")
    user = request.data.get("user")
    obj = Host.objects.get(ip=ip,user=user)
    for file in files:
        # print(file,type(file),len(file))
        if file.size >= 1024 * 1024 * file_maximum:
            return Response({"message": f"文件大小超过{file_maximum}M限制"})
        upload_root_path = settings.JUMPSERVER_UPLOADS_DIR / "private_key"
        parent_path = f"{obj.ip}/{obj.user}"
        sub_path = upload_root_path / parent_path
        filename = "id_rsa"
        if not os.path.exists(sub_path):
            sub_path.mkdir(parents=True,exist_ok=True)

        with open(sub_path / filename ,"wb",) as f:
            for chunk in file.chunks():
                f.write(chunk)
        obj.ssh_private_key_path = sub_path / filename
        obj.save()
    return Response({"result": "ok"})


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def upload(request:Request):
#     """
#     1.文件大小判断
#     2.文件类型检测
#     3.图片缩略图
#     4.
#     :param request:
#     :return:
#     """
#     print(request.data)
#     file = request.data.get("file")
#     print(file.open())
#     print(file.size)
#     if file.size > 1024 * 1024 * 0.5:
#         return Response({"message": "文件大小超过0.5M限制"})
#     print(len([i for i in file.chunks()]))
#     print(next(file.chunks()))
#     print(file.multiple_chunks())
#     return Response({"message": "ok"})


# def load_server_to_mysql(file_path: str):
#     from pyspark.sql import SparkSession
#     from pyspark import SparkConf, SparkContext
#     from pyspark.sql.types import (
#         StructType,
#         StringType,
#         StructField,
#         IntegerType,
#         DoubleType,
#         DateType,
#     )
#
#     spark = SparkSession.builder.master("local[*]").appName("yc_local").getOrCreate()
#     schema = StructType([
#         StructField("name", StringType(), True),
#         StructField("alias_name", StringType(), True),
#         StructField("ip", StringType(), True),
#         StructField("user", StringType(), True),
#         StructField("password", StringType(), True),
#         StructField("ssh_public_key_path", StringType(), True),
#         StructField("ssh_private_key_path", StringType(), True),
#         StructField("is_deleted", IntegerType(), True),
#         StructField("add_date", StringType(), True),
#         StructField("org_id", IntegerType(), True),
#     ])
#     df = spark.read.csv(
#         path=f"file://{file_path}",
#         sep=",",
#         header=False,
#         schema=schema,
#     )
#
#     # init_df = spark.createDataFrame()
#     df.show()
#     df.createOrReplaceTempView("t1")
#     df.write.jdbc(
#         url="jdbc:mysql://node2:3306/codebox?useSSL=false&useUnicode=true&characterEncoding=UTF-8",
#         table="jmp_host",
#         mode="append",
#         properties={"user": "yc", "password": "zzyycc1013"}
#     )
#     spark.stop()
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_server(request:Request):
    """
    1.文件大小判断
    2.文件类型检测
    3.图片缩略图
    4.
    :param request:
    :return:
    """
    # 上传的文件大小最大限制,单位M
    fileinfo_dict = {}
    file_maximum = 1
    files = request.FILES.getlist("file")
    if len(files) > 3:
        return Response({"result": f"最多支持同时上传3个文件"})
    file_instance = File()
    for file in files:
        # print(file,type(file),len(file))
        if file.size >= 1024 * 1024 * file_maximum:
            return Response({"message": f"文件大小超过{file_maximum}M限制"})
        upload_root_path = settings.JUMPSERVER_UPLOADS_DIR
        # parent_path = datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y%m%d%H%M%S")
        parent_path = datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y%m%d%H%M")
        uuid = uuid4().hex
        filename = Path(uuid)
        sub_path = upload_root_path / parent_path
        if not os.path.exists(sub_path):
            sub_path.mkdir(parents=True,exist_ok=True)

        with open(sub_path / filename ,"wb",) as f:
            for chunk in file.chunks():
                f.write(chunk)
        file_instance.name = file.name
        file_instance.uuid = uuid
        file_instance.path = str(sub_path / filename)
        file_instance.size = file.size
        file_instance.save()
        fileinfo_dict[uuid] = {}
        fileinfo_dict[uuid]["filename"] = file.name
        fileinfo_dict[uuid]["filepath"] = str(parent_path / filename)
        try:
            load_server_to_mysql.delay(str(sub_path / filename))
        except Exception as e:
            print(str(e))
    return Response({"result": "ok", "fileinfo": fileinfo_dict})