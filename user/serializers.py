from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UserProfile


class UserModelSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only=True,help_text="确认密码")
    token = serializers.CharField(max_length=1000, read_only=True, help_text="token令牌")

    class Meta:
        # model = User
        model = UserProfile
        fields = ["id", "username", "password", "confirm_password", "token","email","is_superuser","is_active"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        # print(password,confirm_password)
        if password != confirm_password:
            raise serializers.ValidationError("输入的密码与确认密码不一致")
        try:
            User.objects.get(username=username)
            raise serializers.ValidationError("注册的用户名已存在")
        except Exception as e:
            print(str(e))
        return attrs

    def create(self, validated_data: dict):
        # {'username': 'zzz1', 'password': '1234567890', 'confirm_password': '1234567890'}
        try:
            del validated_data["confirm_password"]
            user = super().create(validated_data=validated_data)
            user.set_password(validated_data.get("password"))
            user.save()
        except:
            raise serializers.ValidationError("保存用户注册信息失败")

        # from rest_framework_simplejwt.settings import api_settings

        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        #
        # payload = jwt_payload_handler(user)
        # user.token = jwt_encode_handler(payload)
        return user
