from django.db import models
from datetime import datetime

# Create your models here.
class Sensor(models.Model):
	sensor_name = models.CharField(max_length=2)

#FT = Fish Temp
#ST = Sump Temp
#GT = Grow Temp
	

class SensorData(models.Model):
	data = models.FloatField(default='99.99')
	sub_date = models.DateTimeField(default=datetime.now)
	sensor = models.ForeignKey(Sensor, related_name='sensorData')

	def __unicode__(self):
		return '%s, %d, %s' % (self.id, self.data, self.sub_date)

# 	def get_reading(self):
# 		raise NotImplement

# 	class Meta:
# 		abstract = True

# class TemperatureSensor(Sensor):
# 	moisture_limit = models.Integer()

# 	def get_reading(self):
# 		self.data.do_something()
