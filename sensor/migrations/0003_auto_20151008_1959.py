# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0002_sensor_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.FloatField(default=b'99.99')),
                ('sub_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='data',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='sub_date',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_name',
            field=models.CharField(max_length=2),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='sensor',
            field=models.ForeignKey(to='sensor.Sensor'),
        ),
    ]
