from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pipeline-home'),
    path('train/', views.train_post, name='pipeline-train'),
    path('ping/', views.ping, name='pipeline-ping'),
]
