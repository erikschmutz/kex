import json
from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from scripts.train import train_model, save_model
from scripts.config import make_config

def home(request):
    return render(request, 'home.html')

def train(request):
    if request.method == "POST":
        json_string = request.body.decode('utf-8')
        config = make_config(json_string)
        model = train_model(config)
        save_model(config, model)

        return HttpResponse("OK", status='200')

def ping(request):
    return HttpResponse("OK", status='200')

