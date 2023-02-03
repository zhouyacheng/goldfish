import asyncio
import websockets
import os
import json
import django
from typing import Dict
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codebox.settings')
from rest_framework_simplejwt.authentication import JWTAuthentication
from asgiref.sync import sync_to_async
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError
import paramiko
from django.conf import settings

django.setup()


@sync_to_async
def get_host(hostid: int):
    from jumpserver.models import Host
    host_obj: Host = Host.objects.get(id=hostid)
    return host_obj

@sync_to_async
def log(**kwargs):
    from jumpserver.models import Track
    Track.objects.create(**kwargs)

async def handler(websocket):
    from jumpserver.models import Host,Track
    port = 22
    vaildate_data: str = await websocket.recv()
    # 1.接受token和host id
    # 2.校验token
    # 3.接受命令
    # 4.执行命令返回
    print(vaildate_data,type(vaildate_data))
    ser_vaildate_data:Dict = json.loads(vaildate_data)
    raw_token = ser_vaildate_data.get("token")
    hostid = int(ser_vaildate_data.get("hostid"))
    try:
        jwtauth = JWTAuthentication()
        validated_token = jwtauth.get_validated_token(raw_token)
        user = await sync_to_async(jwtauth.get_user)(validated_token)
        host_obj:Host = await get_host(hostid)
        await websocket.send(f"Hello {user.username}  !")
        """
        user = models.ForeignKey(User,models.PROTECT,db_column="user_id")
        host = models.ForeignKey("Host",models.PROTECT,db_column="host_id")
        source_ip = models.GenericIPAddressField()
        op_type = models.IntegerField(choices=op_type_choices)
        op_date = models.DateTimeField(auto_now_add=True)
        command = models.CharField(max_length=255,null=True,blank=True,verbose_name="命令")
        op_state = models.BooleanField(verbose_name="执行结果")
        """
        await log(user_id=user.pk,host_id=host_obj.pk,source_ip=host_obj.ip,op_type=1,op_state=0)

        while True:
            command: str = await websocket.recv()
            print(command,type(command))
            if command == "q":
                await log(user_id=user.pk, host_id=host_obj.pk, source_ip=host_obj.ip, op_type=2, op_state=0)
                await websocket.close(1011, "websocket通道已关闭")
                return
            private = paramiko.RSAKey.from_private_key_file(host_obj.ssh_private_key_path)
            trans = paramiko.Transport((host_obj.ip, port))
            trans.connect(username=host_obj.user, pkey=private)

            ssh = paramiko.SSHClient()
            # 绑定链接
            ssh._transport = trans

            # 执行shell命令
            stdin, stdout, stderror = ssh.exec_command(command)
            stdout_ret = stdout.read().decode('utf-8')
            stderror_ret = stderror.read().decode('utf-8')
            op_state = 0
            if stderror_ret:
                op_state = 1
            await log(user_id=user.pk, host_id=host_obj.pk, source_ip=host_obj.ip,command=command, op_type=3, op_state=op_state)
            await websocket.send(json.dumps({"stdout": stdout_ret,"stderror": stderror_ret}))
            trans.close()

    except InvalidToken as e:
        error_message = "令牌无效或已过期"
        await websocket.send(f"{error_message}!")
    except Exception as e:
        await websocket.send(str(e))




async def main():
    async with websockets.serve(handler, "localhost", 8888):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())