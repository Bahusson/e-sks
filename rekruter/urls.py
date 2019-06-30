from django.urls import path

from . import views

urlpatterns = [
    path('initial/', views.initial, name='initial'),
    path('register/', views.register, name='register'),
    ]
