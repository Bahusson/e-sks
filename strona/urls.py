from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    path('infos/<int:info_id>/', views.info, name='info'),
]
