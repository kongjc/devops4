# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_porfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='porfile',
            name='department',
        ),
    ]
