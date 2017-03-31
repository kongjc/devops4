# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=11)),
                ('title', models.CharField(default='', max_length=32)),
                ('department', models.ForeignKey(to='dashboard.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hostname', models.CharField(unique=True, max_length=32)),
                ('ip', models.CharField(unique=True, max_length=14)),
                ('cpu', models.CharField(max_length=50)),
                ('mem', models.CharField(max_length=50)),
                ('disk', models.CharField(max_length=50)),
                ('sn', models.CharField(max_length=32)),
                ('idc', models.CharField(max_length=50)),
                ('ip_info', models.CharField(verbose_name="[{'eth0': '192.168.1.1'}]", max_length=255)),
                ('product', models.CharField(max_length=50)),
                ('remark', models.TextField(default='')),
            ],
            options={
                'db_table': 'server',
            },
        ),
    ]
