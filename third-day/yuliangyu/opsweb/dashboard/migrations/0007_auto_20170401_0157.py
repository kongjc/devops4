# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_profile_usernamme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='usernamme',
            new_name='name',
        ),
    ]
