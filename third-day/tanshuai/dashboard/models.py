from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Server(models.Model):
    hsotname        = models.CharField(max_length=32,unique=True)
    ip              = models.CharField(max_length=15,unique=True)
    cpu             = models.CharField(max_length=50)
    mem             = models.CharField(max_length=50)
    disk            = models.CharField(max_length=50)
    sn              = models.CharField(max_length=32)
    idc             = models.CharField(max_length=50)
    product         = models.CharField(max_length=50)
    remark          = models.TextField(default='')

    class Meta:
        db_table = "server"


class Department(models.Model):
    name            = models.CharField(max_length=11,null=True)

    class Meta:
        db_table = "department"

class Profile(models.Model):
    user            = models.OneToOneField(User)
    phone           = models.CharField(max_length=11, null=True)
    title           = models.CharField(max_length=32, null=True)
    cnname          = models.CharField(max_length=32, null=True)
    # department      = models.CharField(max_length=32, null=True)
    department      = models.ForeignKey(Department, null=True)

    class Meta:
        db_table = "user_profile"
        default_related_name = "profile"
