from django.db import models
from datetime import datetime

# Create your models here.
class Sensor(models.Model):
	sensor_name = models.CharField(max_length=2)
	data = models.FloatField(default='99.99')
	sub_date = models.DateTimeField(default=datetime.now)

#FT = Fish Temp
#ST = Sump Temp
#GT = Grow Temp
