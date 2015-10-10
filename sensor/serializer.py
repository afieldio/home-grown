from rest_framework import serializers
from sensor.models import Sensor, SensorData


class SensorDataSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SensorData
		field = ('id', 'data', 'sub_date')


class SensorSerializer(serializers.ModelSerializer):
	sensorData = SensorDataSerializer(many=True)

	class Meta:
		model = Sensor
		fields = ('id', 'sensor_name', 'sensorData')
