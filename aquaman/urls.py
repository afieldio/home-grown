"""aquaman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^(?P<sn>[a-z]{2})/$', views.graph, name='graph'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'aquaman.views.index', name='home' ),
    url(r'^about/$', 'aquaman.views.about', name='about'),
    url(r'^presentation/$', 'aquaman.views.presentation', name='presentation'),
    url(r'^contact/$', 'aquaman.views.contact', name='contact'),
    url(r'^data/$', 'aquaman.views.data', name='data'),
    url(r'^$', 'aquaman.views.index'),
    url(r'^sensorsapi/$', views.AllSensors.as_view()),
    url(r'^sensorsapi/(?P<pk>[0-9]+)/$', views.DetailSensor.as_view()),
    url(r'^(?P<sn>[a-z]{2})/$', views.graph, name='graph'),
    url(r'^graph_data/(?P<sn>[a-z]{2})/$', views.graph_data, name='data'),
    url(r'^posttweet/(?P<tweet_type>[a-z]+)$', views.posttweet, name='posttweet'),
    url(r'^accounts/login/$', auth_views.login),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
