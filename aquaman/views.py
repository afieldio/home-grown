from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.
def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def presentation(request):
	return render(request, 'presentation.html')
