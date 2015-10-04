from django.db import models
from datetime import datetime

# Create your models here.
class Sensor(models.Model):
	data = models.FloatField(default='99.99')
	sensor_name = models.CharField(max_length=10)
	sub_date = models.DateTimeField(default=datetime.now)

