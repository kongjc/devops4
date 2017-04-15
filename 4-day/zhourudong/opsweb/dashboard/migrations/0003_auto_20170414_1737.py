# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170413_2239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'permissions': set([('view_server', '访问服务服务器信息')])},
        ),
        migrations.AlterField(
            model_name='profile',
            name='chinaname',
            field=models.CharField(max_length=32, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='server',
            name='ipinfo',
            field=models.CharField(verbose_name="[{'eth0':'192.168.1.1', 'mac': ''},{'eth0':'192.168.1.1', 'mac': ''}]", max_length=255),
        ),
        migrations.AlterField(
            model_name='server',
            name='remark',
            field=models.TextField(default=''),
        ),
    ]
