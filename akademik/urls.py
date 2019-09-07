from django.urls import path
from . import views, views_c

urlpatterns = [
    path('panel_rady', views_c.staffpanel_c, name='staffpanel_c'),
    path('panel_akademika', views.staffpanel_h, name='staffpanel_h'),
    path('panel_uzytkownika', views.userpanel, name='userpanel'),
    path('panel_tlumacza', views.translatorpanel, name='translatorpanel'),
    path('twoje_dane', views.showmydata, name='userdatapersonal'),
    path('aplikacja_ds', views.dormapply, name='dsapply'),
    path('kreator_akcji/<party_id>/', views_c.makemeparty, name='makemeparty'),
    path('akcje_kwaterunkowe', views_c.allparties, name='allparties'),
]
