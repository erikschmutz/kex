from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pipeline-home'),
    path('config/', views.config, name='pipeline-config'),
    path('ping/', views.ping, name='pipeline-ping'),
]
