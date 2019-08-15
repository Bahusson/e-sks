from django.urls import path
from . import views

urlpatterns = [
    path('panel_rady', views.staffpanel_c, name='staffpanel_c'),
    path('panel_akademika', views.staffpanel_h, name='staffpanel_h'),
    path('panel_uzytkownika', views.userpanel, name='userpanel'),
    path('twoje_dane', views.showmydata, name='userdatapersonal'),
]
