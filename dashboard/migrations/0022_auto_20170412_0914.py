# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20170409_0552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='cn_name',
            new_name='name',
        ),
    ]
