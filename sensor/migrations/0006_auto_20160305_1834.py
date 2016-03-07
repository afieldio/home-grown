# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0005_auto_20151018_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='sensor_data',
            new_name='data',
        ),
    ]
