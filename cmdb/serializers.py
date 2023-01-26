# from rest_framework import serializers
from rest_framework_mongoengine import serializers
from .models import CiType,CiTypeField,Ci

class CiTypeFieldModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CiTypeField


class CiTypeModelSerializer(serializers.DocumentSerializer):
    # citypefield = CiTypeFieldModelSerializer(read_only=True,many=True)
    class Meta:
        model = CiType
        fields = ["id","name","label","version"]

class CiTypeRetriveModelSerializer(serializers.DocumentSerializer):
    # citypefield = CiTypeFieldModelSerializer(read_only=True,many=True)
    class Meta:
        model = CiType
        fields = ["id","name","label","version","fields"]

class CiModelSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Ci
        fields = "__all__"
