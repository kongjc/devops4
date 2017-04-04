# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_profile_cn_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cn_name',
        ),
    ]
