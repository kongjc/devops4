# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20170401_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cnname',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
