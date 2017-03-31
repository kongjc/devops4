from django.db import models
from django.contrib.auth.models import User


class Server(models.Model):
    hostname = models.CharField(max_length=32, unique=True)
    ip = models.CharField(max_length=14, unique=True)
    cpu = models.CharField(max_length=50)
    mem = models.CharField(max_length=50)
    disk = models.CharField(max_length=50)
    sn = models.CharField(max_length=32)
    idc = models.CharField(max_length=50)
    ip_info = models.CharField("[{'eth0': '192.168.1.1'}]", max_length=255)
    product = models.CharField(max_length=50)
    remark = models.TextField(default='')

    def __str__(self):
        return 'server {}'.format(self.hostname)

    class Meta:
        db_table = 'server'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=11, default='')
    department = models.ForeignKey('Department')
    title = models.CharField(max_length=32, default='')

    def __str__(self):
        return 'profile {}'.format(self.user.username)

    class Meta:
        db_table = 'user_profile'


class Department(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return 'department {}'.format(self.name)

    class Meta:
        db_table = 'department'
