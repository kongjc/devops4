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
        '''
        以人类可读的友好形式返回指定的数据，python 3 中使用 __str__
        python 2 中使用 __unicode__
        '''
        return "{} {}".format(self.hostname, self.ip)

    class Meta:
        db_table        = "server"          # 数据库表名


class Department(models.Model):
    """
    部门表
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
        '''
        在模型关系中，一个模型通过模型关系访问另外一个模型的时候可以通过 .name (点后面跟上一个名字)，这个name就是related_name， 
        默认值为模型名（小写的），也可以更改这个名字，通过 Meta 的 default_related_name 去修改
        '''
        default_related_name = "profile"            # 默认的反向名称


