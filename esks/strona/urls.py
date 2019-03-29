from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/<int:lang_id>/', views.home, name='home'),
]
