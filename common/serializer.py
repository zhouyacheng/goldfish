from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.response import Response
from iac.models import BaseModel,DatetimeModel
from django.contrib.auth.models import User
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from common.auth import BearerTokenAuthentication


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username"]

class AuthorSummaryModelSerializer(serializers.ModelSerializer):
    created_by =  AuthorModelSerializer(read_only=True)
    updated_by =  AuthorModelSerializer(read_only=True)
    deleted_by =  AuthorModelSerializer(read_only=True)

@extend_schema_field(OpenApiTypes.BINARY)
class FormDataFileField(serializers.FileField):
    pass


class MutationSerializerMixin(object):
    def get_fields(self):
        fields = {}
        for name,field in super().get_fields().items():
            field.required = False
            fields[name] = field
        return fields

class CreationSerializerMixin(object):
    def get_fields(self):
        fields = {}
        for name,field in super().get_fields().items():
            if not field.read_only:
                fields[name] = field
        return fields
class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel


class DateTimeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatetimeModel
        extra_kwargs = {
            "create_time": {"read_only": True},
            "update_time": {"read_only": True},
            "delete_time": {"read_only": True},
        }

class AuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(max_length=40,read_only=True,required=False)
    expired_time = serializers.DateTimeField(read_only=True,required=False)

    def validate(self, attrs):
        # 1.校验用户名密码
        # 2.生成token和过期时间
        username = attrs.get("username")
        password = attrs.get("password")
        if username and password:
            user = authenticate(request=self.context.get("request"),
                                username=username,
                                password=password)
            if not user:
                return Response({"detail": "用户名或密码输入错误"})
        else:
            msg = 'Must include "username" and "password"'
            raise serializers.ValidationError(msg)
        token,expired_time = BearerTokenAuthentication().login(user.id)
        attrs["token"] = token
        attrs["expired_time"] = expired_time

        return attrs