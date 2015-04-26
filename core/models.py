from django.db import models
from status import ACTIVE, INACTIVE, DELETED


STATUS_CHOICES = (
    (ACTIVE, 'active'),
    (INACTIVE, 'inactive'),
    (DELETED, 'deleted')
)


class Host(models.Model):
    cpu = models.IntegerField()
    memory = models.IntegerField()
    disk_space = models.IntegerField()
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )

    def __unicode__(self):
        return unicode(self.id)


class Instance(models.Model):
    cpu = models.IntegerField()
    memory = models.IntegerField()
    disk_space = models.IntegerField()
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )
    host = models.ForeignKey(Host)

    def __unicode__(self):
        return unicode(self.id)
