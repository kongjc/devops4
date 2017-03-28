# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170326_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='disk',
            field=models.CharField(max_length=50),
        ),
    ]
