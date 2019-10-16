from django.urls import path
from . import views, views_c

urlpatterns = [
    path('panel_rady', views_c.staffpanel_c, name='staffpanel_c'),
    path('panel_akademika', views.staffpanel_h, name='staffpanel_h'),
    path('panel_uzytkownika', views.userpanel, name='userpanel'),
    path('panel_tlumacza', views.translatorpanel, name='translatorpanel'),
    path('twoje_dane', views.showmydata, name='userdatapersonal'),
    path('aplikacja_ds', views.dormapply, name='dsapply'),
    path('kreator_akcji', views_c.makemeparty, name='makemeparty'),
    path('akcje_kwaterunkowe', views_c.allparties, name='allparties'),
    path('edytuj_akcje', views_c.changemeparty, name='changemeparty'),
    path('wnioski_o_akademik', views_c.allapplied, name='allapplied'),
    path('szukaj_uzytkownikow', views_c.allusers, name='allusers'),
    path(
     'edycja_uzytkownika/<int:user_id>', views_c.changeuser, name='changeuser'),
]
