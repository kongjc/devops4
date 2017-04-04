# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20170326_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cn_name',
            field=models.CharField(default=b'\xe4\xb8\xad\xe6\x96\x87\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', max_length=50, null=True),
        ),
    ]
