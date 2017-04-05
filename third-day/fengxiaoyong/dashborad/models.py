from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=32)
    class Meta:
        db_table = 'department'


class Userprofile(models.Model):
    user = models.OneToOneField(User)
    department = models.ForeignKey('Department')
    phone = models.CharField(max_length=11, null=True)
    title = models.CharField(max_length=32, null=True)
    name = models.CharField(max_length=32, null=True)
    class Meta:
        db_table = 'userprofile'




