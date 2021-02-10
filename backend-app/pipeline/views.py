import json
from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'home.html')

def config(request):
    config_data = staticfiles_storage.open("config.json")
    config_json = json.load(config_data)
    config_data.close()
    print(config_json)

    return JsonResponse(config_json)

def ping(request):
    return HttpResponse("OK", status='200')

