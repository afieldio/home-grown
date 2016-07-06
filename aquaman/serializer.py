from rest_framework import serializers
from models import Sensor

class SensorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sensor
		fields = ('id', 'sensor_name', 'data', 'sub_date')