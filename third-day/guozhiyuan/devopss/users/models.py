from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50,unique=True,default='',null=True)

    class Meta:
        db_table = 'department'

    def __unicode__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30,default='')
    phone = models.CharField(max_length=11,null=True,default='')
    title = models.CharField(max_length=50,null=True,default='')
    department = models.ForeignKey(Department, null=True,default='')

    class Meta:
        db_table = 'user_profile'
        default_related_name = 'profile'
        verbose_name = "Profile"
        verbose_name_plural = verbose_name

    def __unicode__(self):
         return self.user.username