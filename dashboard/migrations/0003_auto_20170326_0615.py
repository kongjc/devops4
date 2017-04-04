# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_server_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='sn',
            field=models.CharField(max_length=32),
        ),
    ]
