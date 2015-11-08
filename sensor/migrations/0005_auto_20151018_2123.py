# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0004_auto_20151011_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='data',
            new_name='sensor_data',
        ),
    ]
