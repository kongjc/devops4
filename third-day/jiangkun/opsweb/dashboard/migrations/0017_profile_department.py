# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_remove_profile_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(default=1, to='dashboard.Department'),
        ),
    ]
