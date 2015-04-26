import json
from django.test import Client
from django.test import TestCase
from core.models import Host, Instance
from core.status import ACTIVE, DELETED


class APITestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(APITestCase, cls).setUpClass()
        cls.web_client = Client()

    def setUp(self):
        self.host = Host.objects.create(cpu=777, memory=777, disk_space=777)
        self.instance = Instance.objects.create(
            cpu=2,
            memory=8,
            disk_space=50,
            host=self.host
        )

    def test_create_host(self):
        self.web_client.post('/hosts', {
            'cpu': 333222,
            'memory': 333222,
            'disk_space': 333222,
        })

        host = Host.objects.get(cpu=333222)

        self.assertEqual(host.status, ACTIVE)

    def test_list_all_hosts(self):
        response = self.web_client.get('/hosts')
        hosts = json.loads(response.content)
        self.assertEqual(len(hosts), 1)

    def test_get_one_host(self):
        response = self.web_client.get(
            '/hosts/{host_id}'.format(host_id=self.host.id)
        )
        host = json.loads(response.content)
        self.assertEqual(host.get('cpu'), self.host.cpu)

    def test_delete_host(self):
        self.web_client.delete(
            '/hosts/{host_id}'.format(host_id=self.host.id)
        )
        host = Host.objects.get(id=self.host.id)
        self.assertEqual(host.status, DELETED)

    def test_create_instance(self):
        self.web_client.post(
            '/hosts/{host_id}/instances'.format(host_id=self.host.id),
            {'cpu': 4444, 'memory': 4444, 'disk_space': 4444}
        )

        instance = Instance.objects.get(cpu=4444)

        self.assertEqual(instance.status, ACTIVE)
        self.assertEqual(instance.host.id, self.host.id)

    def test_list_all_instances(self):
        response = self.web_client.get(
            '/hosts/{host_id}/instances'.format(host_id=self.host.id)
        )
        instances = json.loads(response.content)
        self.assertEqual(len(instances), 1)

    def test_get_one_instance(self):
        response = self.web_client.get(
            '/hosts/{host_id}/instances/{instance_id}'.format(
                host_id=self.host.id, instance_id=self.instance.id
            )
        )
        instance = json.loads(response.content)
        self.assertEqual(instance.get('cpu'), self.instance.cpu)

    def test_delete_instance(self):
        self.web_client.delete(
            '/hosts/{host_id}/instances/{instance_id}'.format(
                host_id=self.host.id,
                instance_id=self.instance.id
            )
        )
        instance = Instance.objects.get(id=self.instance.id)
        self.assertEqual(instance.status, DELETED)
