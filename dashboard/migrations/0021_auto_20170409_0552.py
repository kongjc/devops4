# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20170409_0551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'permissions': (('view_server', '\u8bbf\u95ee\u670d\u52a1\u5668\u4fe1\u606f'),)},
        ),
    ]
