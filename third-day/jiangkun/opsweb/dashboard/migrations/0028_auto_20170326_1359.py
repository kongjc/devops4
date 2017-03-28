# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_auto_20170326_1358'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='server',
            table='server',
        ),
    ]
