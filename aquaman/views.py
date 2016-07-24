from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from rest_framework.response import Response
from models import Sensor
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Sensor
from .serializer import SensorSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from forms import ContactForm
from django.core.mail import EmailMessage

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

# Create your views here.


def index(request):
    context = {'state':'home'}
    
    return render(request, 'index.html', context)

def data(request):
    try:
        latest_grow_temp = Sensor.objects.filter(
            sensor_name="GT").latest("sub_date")
        latest_sump_temp = Sensor.objects.filter(
        sensor_name="ST").latest("sub_date")
        latest_fish_temp = Sensor.objects.filter(
            sensor_name="FT").latest("sub_date")
        latest_air_temp = Sensor.objects.filter(
            sensor_name="AT").latest('sub_date')
        latest_air_pressure = Sensor.objects.filter(
            sensor_name="AP").latest('sub_date')
        latest_light_lux = Sensor.objects.filter(
            sensor_name="LS").order_by('sub_date').reverse()[:2]
        light = False
    except Exception, e:
        latest_grow_temp = "99.99"
        latest_sump_temp = "99.99"
        latest_fish_temp = "99.99"
        latest_air_temp = "99.99"
        latest_air_pressure = "99.99"
        latest_light_lux = "99.99"
        raise e

    

    if latest_light_lux[0].data < 10 and latest_light_lux[1].data < 10:
        light = False
    else:
        light = True

    print light

    # import ipdb; ipdb.set_trace()
    all_fish_temp = Sensor.objects.filter(
        sensor_name="FT").order_by('sub_date')

    # import ipdb; ipdb.set_trace()
    context = {'latest_grow_temp': latest_grow_temp, 'latest_sump_temp':
               latest_sump_temp, 'latest_fish_temp': latest_fish_temp, 'all_fish_temp': all_fish_temp, 'light': light, 'latest_light_lux': latest_light_lux, 'state': 'data' }

    return render(request, 'data.html', context)

def graph(request, sn):
    if sn == 'ft':
        sensor_name = 'Fish Tank'
    elif sn == 'st':
        sensor_name = 'Sump Tank'
    elif sn == 'gt':
        sensor_name = 'Grow Area'
    else:
        sensor_name = 'UNKNOWN'

    sensor_list = Sensor.objects.values_list('sensor_name').distinct()

    sn = sn.upper()
    q = Sensor.objects.filter(sensor_name=sn).order_by(
        "sub_date").values('data', 'sub_date')
    all_sensor_data = json.dumps(list(q), cls=DjangoJSONEncoder)

    context = {'all_sensor_data': all_sensor_data,
               'sensor_name': sensor_name, 'sensor_list': sensor_list, 'state': 'data'}

    return render(request, 'detail.html', context)


def graph_data(request, sn):
    sn = sn.upper()
    q = Sensor.objects.filter(sensor_name=sn).order_by(
        "sub_date").values('data', 'sub_date')
    all_sensor_data = json.dumps(list(q), cls=DjangoJSONEncoder)
    return JsonResponse(all_sensor_data, safe=False)


def allgraphs(request):
    sensor_list = Sensor.objects.values_list('sensor_name').distinct()

    context = {'sensor_list': sensor_list}

    return render(request, 'all_graphs.html', context)


def about(request):
    context = {'state': 'about'}
    return render(request, 'about.html', context)


def presentation(request):
    context = {'state': 'presentation'}
    return render(request, 'presentation.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            contact_name = request.POST.get('name', '')
            contact_email = request.POST.get('email', '')
            form_content = request.POST.get('description', '')
            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })

            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['a.field738@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('home')
    else:
        form = ContactForm()

    context = RequestContext(request, {'form': form, 'state': 'contact'})
    return render_to_response('contact.html', context=context)


#
#   API
#


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
        # import pdb; pdb.set_trace()

        sensor = self.get_object(pk)
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)

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
