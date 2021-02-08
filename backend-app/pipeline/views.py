import json
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def config(request):
    config_data = open("/static/config.json")
    config_json = json.load(config_data)
    config_data.close()

    return render(request, 'config.html', config_json)

def ping(request):
    return HttpResponse("OK", status='200')

