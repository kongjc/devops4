# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
class User(models.Model):
    id          = models.AutoField(primary_key=True)
    username    = models.CharField(max_length=32, null=True)
    login_time  = models.DateTimeField()
    aaa         = models.CharField("test", max_length=50)

    class Meta:
        db_table = "User"
"""

"""
创建迁移文件 对 dashboard 应用
python manage.py makemigrations dashboard
查看迁移SQL语句 dashboard 应用 的 0002 序号
python manage.py sqlmigrate dashboard 0002
执行迁移 对 dashboard 应用
python manage.py migrate dashboard
"""


class Server(models.Model):
    hostname        = models.CharField(max_length=32, unique=True, null=False)
    ip              = models.CharField(max_length=15, unique=True)
    cpu             = models.CharField(max_length=50)
    mem             = models.CharField(max_length=50)
    disk            = models.CharField(max_length=50)
    sn              = models.CharField(max_length=32)
    idc             = models.CharField(max_length=50)
    ipinfo          = models.CharField("[{'eth0':'192.168.1.1', 'mac':'0011', },{'eth1':'192.168.1.2', 'mac':'0022', }]", max_length=255)
    product         = models.CharField(max_length=50)
    remark          = models.TextField(default="")

    def __str__(self):
        return "{} {}".format(self.hostname, self.ip)

    class Meta:
        db_table = "server"


class Department(models.Model):
    name        = models.CharField(max_length=11, null=True)

    class Meta:
        db_table = "department"
#
#
class Profile(models.Model):
    user        = models.OneToOneField(User)
    phone       = models.CharField(max_length=11, null=True)
    title       = models.CharField(max_length=32, null=True)
    # department  = models.CharField(max_length=32, null=True)
    department  = models.ForeignKey(Department, default=1)
    name        = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = "user_profile"
        default_related_name = "profile"





