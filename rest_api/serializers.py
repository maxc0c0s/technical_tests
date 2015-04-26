from rest_framework import serializers
from core.models import Host, Instance


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('id', 'cpu', 'memory', 'disk_space', 'status')


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = ('id', 'cpu', 'memory', 'disk_space', 'status', 'host')
