from rest_framework import serializers
from sensor.models import Sensor

class SensorSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Sensor
		fields = ('id', 'data', 'sensor_name', 'sub_date')
		