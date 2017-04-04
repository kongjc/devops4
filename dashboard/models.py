# coding=utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class user(models.Model):
#     username            = models.CharField(max_length=32, null=True)
#     login_time          = models.DateField()
#
#     class Meta:
#         db_table        = "user"


class Server(models.Model):
    """

    """
    hostname            = models.CharField(max_length=32, unique=True, null=False)
    ip                  = models.CharField(max_length=15, unique=True)
    cpu                 = models.CharField(max_length=50)
    mem                 = models.CharField(max_length=50)
    disk                = models.CharField(max_length=50)
    sn                  = models.CharField(max_length=32)
    idc                 = models.CharField(max_length=50)
    ipinfo              = models.CharField(max_length=255)
    product             = models.CharField(max_length=50)
    remark              = models.TextField(default='')

    def __str__(self):
        return "{} {}".format(self.hostname, self.ip)

    class Meta:
        db_table        = "server"


class Department(models.Model):
    """

    """
    name = models.CharField(max_length=11, null=True)

    class Meta:
        db_table        = "department"


class Profile(models.Model):
    """
    User 表的关联属性
    """
    user                = models.OneToOneField(User)
    phone               = models.CharField(max_length=11, null=True)
    title               = models.CharField(max_length=32, null=True)
    department          = models.ForeignKey(Department, null=True)
    cn_name             = models.CharField(max_length=50, null=True)

    class Meta:
        db_table        = "user_profile"
        default_related_name = "profile"


