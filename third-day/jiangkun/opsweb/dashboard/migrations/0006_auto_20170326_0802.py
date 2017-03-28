# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_profile'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='user_profile',
        ),
    ]
