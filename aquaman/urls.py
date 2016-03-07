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
from sensor import views

urlpatterns = [
    
    url(r'^sensor/', include('sensor.urls', namespace="sensor")),
    url(r'^sensor/(?P<sn>[a-z]{2})/$', views.graph, name='graph'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'aquaman.views.index'),
    url(r'^about/$', 'aquaman.views.about'),
    url(r'^presentation/$', 'aquaman.views.presentation'),
    url(r'^$', 'aquaman.views.index'),

]
