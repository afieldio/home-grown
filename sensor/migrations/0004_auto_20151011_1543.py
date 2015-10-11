# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0003_auto_20151008_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensor',
            name='data',
            field=models.FloatField(default=b'99.99'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='sub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.DeleteModel(
            name='SensorData',
        ),
    ]
