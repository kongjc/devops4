# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20170414_0720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('view_profile', '\u8bbf\u95ee\u7528\u6237\u4fe1\u606f'), ('view_group', '\u8bbf\u95ee\u7528\u6237\u7ec4\u4fe1\u606f'))},
        ),
    ]
