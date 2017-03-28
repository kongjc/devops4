# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
    ]
