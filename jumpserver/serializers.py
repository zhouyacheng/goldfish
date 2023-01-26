from rest_framework import serializers
from .models import Organization,Host

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Organization

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Host
        extra_kwargs = {
            "password": {"write_only":True},
            "is_deleted": {"write_only":True},
            "ssh_public_key_path": {"write_only":True},
            "ssh_private_key_path": {"write_only":True},
        }