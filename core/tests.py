from django.test import TestCase
from models import Host, Instance
from status import ACTIVE


class HostTestCase(TestCase):
    def setUp(self):
        Host.objects.create(cpu=20, memory=100, disk_space=2000)

    def test_host_active_on_creation(self):
        host = Host.objects.get(cpu=20)

        self.assertEqual(host.status, ACTIVE)


class InstanceTestCase(TestCase):
    def setUp(self):
        host = Host.objects.create(cpu=20, memory=100, disk_space=2000)
        Instance.objects.create(cpu=2, memory=8, disk_space=50, host=host)

    def test_instance_active_on_creation(self):
        instance = Instance.objects.get(cpu=2)

        self.assertEqual(instance.status, ACTIVE)
