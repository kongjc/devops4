# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_remove_profile_cn_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cn_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
