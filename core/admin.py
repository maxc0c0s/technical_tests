from django.contrib import admin
from .models import Host, Instance


# Register your models here.
admin.site.register(Host)
admin.site.register(Instance)
