from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api import views

urlpatterns = [
    url(r'^hosts/?$', views.HostsView.as_view()),
    url(r'^hosts/(?P<host_id>[0-9]+)/?$', views.HostView.as_view()),
    url(
        r'^hosts/(?P<host_id>[0-9]+)/instances/?$',
        views.InstancesView.as_view()
    ),
    url(
        r'^hosts/(?P<host_id>[0-9]+)/instances/(?P<instance_id>[0-9]+)/?$',
        views.InstanceView.as_view()
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
