# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_profile_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='usernamme',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
