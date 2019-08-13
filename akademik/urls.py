from django.urls import path
from . import views

urlpatterns = [
    path('staffpanel', views.staffpanel, name='staffpanel'),
    path('userpanel', views.userpanel, name='userpanel'),
]
