from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Sensor
from .serializer import SensorSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.

class AllSensors(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get(self, request, format=None):
		sensors = Sensor.objects.all()
		serializer = SensorSerializer(sensors, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SensorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailSensor(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_object(self, pk):
		try:
			return Sensor.objects.get(pk=pk)
		except Sensor.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		#import pdb; pdb.set_trace()
		
		sensor = self.get_object(pk)
		serializer = SensorSerializer(sensor)
		return Response(serializer.data)

	# def create(self, validated_data):
	# 	#import pdb; pdb.set_trace()
	# 	sensors_data = validated_data.pop('sensorData')
	# 	sensor = Sensor.objects.create(**validated_data)
	# 	for sensor_data in sensors_data:
	# 		SensorData.objects.create(sensor=sensor, **sensor_data)
	# 	return sensor

	def put(self, request, pk, format=None):
		sensor = self.get_object(pk)
		serializer = SensorSerializer(sensor, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		sensor = self.get_object(pk)
		sensor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



def index(request):
    latest_grow_temp = Sensor.objects.filter(sensor_name="GT").latest("sub_date")
    latest_sump_temp = Sensor.objects.filter(sensor_name="ST").latest("sub_date")
    latest_fish_temp = Sensor.objects.filter(sensor_name="FT").latest("sub_date")
    context = {'latest_grow_temp':latest_grow_temp, 'latest_sump_temp':latest_sump_temp, 'latest_fish_temp':latest_fish_temp}
    return render(request, 'sensor/index.html', context)

def detail(request, sensor_id):
    try:
        sensor_detail = Sensor.objects.get(pk=sensor_id)
    except Sensor.DoesNotExist:
        raise Http404("Sensor does not Exist")
    return render(request, 'sensor/detail.html', {'sensor_detail':sensor_detail})
    