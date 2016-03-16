from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include
from aquaman import views as aqviews

urlpatterns = [
    # url(r'^(?P<sensor_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^sensorsapi/$', views.AllSensors.as_view()),
    url(r'^sensorsapi/(?P<pk>[0-9]+)/$', views.DetailSensor.as_view()),
    url(r'^$', views.index, name='index'),
    url(r'^graph_data/(?P<sn>[a-z]{2})/$', views.graph_data, name='graph_data'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]