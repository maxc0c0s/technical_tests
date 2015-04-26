from core.models import Host, Instance
from core.status import DELETED
from rest_api.serializers import HostSerializer, InstanceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def get_host(host_id):
    try:
        return Host.objects.get(id=host_id)
    except Host.DoesNotExist:
        raise Http404


def get_instance(host_id, instance_id):
    try:
        return Instance.objects.get(host=host_id, id=instance_id)
    except Instance.DoesNotExist:
        raise Http404


class HostsView(APIView):
        """
        List all hosts or create a new host
        """
        def get(self, request, format=None):
            hosts = Host.objects.all()
            serializer = HostSerializer(hosts, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = HostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class HostView(APIView):
        """
        details of a given host or delete a given host(by deleting we mean
        status set to DELETED)
        """
        def get(self, request, host_id, format=None):
            host = get_host(host_id)
            serializer = HostSerializer(host)
            return Response(serializer.data)

        def delete(self, request, host_id, format=None):
            host = get_host(host_id)
            host.status = DELETED
            host.save()
            return Response(status=status.HTTP_200_OK)


class InstancesView(APIView):
        """
        List all instances for a given host or create a new instance for a given
        host
        """
        def get(self, request, host_id, format=None):
            host = get_host(host_id)
            instances = Instance.objects.filter(host=host)
            serializer = InstanceSerializer(instances, many=True)
            return Response(serializer.data)

        def post(self, request, host_id, format=None):
            host = get_host(host_id)
            request.data.update({'host': host.id})
            serializer = InstanceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class InstanceView(APIView):
        """
        details of a given instance of a given host or delete the given
        instance of a given host(be deleting we mean status set to DELETED)
        """
        def get(self, request, host_id=None, instance_id=None, format=None):
            instance = get_instance(host_id, instance_id)
            serializer = InstanceSerializer(instance)
            return Response(serializer.data)

        def delete(self, request, host_id=None, instance_id=None, format=None):
            instance = get_instance(host_id, instance_id)
            instance.status = DELETED
            instance.save()
            return Response(status=status.HTTP_200_OK)
