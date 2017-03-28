# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170326_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='disk',
            field=models.CharField(max_length=51),
        ),
    ]
