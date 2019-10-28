from django.urls import path
from . import views, views_c, views_t

# Uwaga: Niektóre ścieżki są wspólne!
urlpatterns = [
    # Ścieżki Użytkownika:
    path('panel_akademika', views.staffpanel_h, name='staffpanel_h'),
    path('panel_uzytkownika', views.userpanel, name='userpanel'),
    path('twoje_dane', views.showmydata, name='userdatapersonal'),
    path('aplikacja_ds', views.dormapply, name='dsapply'),
    # Ścieżki Rady Studentów:
    path('panel_rady', views_c.staffpanel_c, name='staffpanel_c'),
    path('kreator_akcji', views_c.makemeparty, name='makemeparty'),
    path('akcje_kwaterunkowe', views_c.allparties, name='allparties'),
    path('edytuj_akcje', views_c.changemeparty, name='changemeparty'),
    path('wnioski_o_akademik', views_c.allapplied, name='allapplied'),
    path('szukaj_uzytkownikow', views_c.allusers, name='allusers'),
    path(
     'edycja_uzytkownika/<int:user_id>', views_c.changeuser, name='changeuser'
     ),
    # Ścieżki Tłumacza:
    path('panel_tlumacza', views_t.translatorpanel, name='translatorpanel'),
    path(
     'tlumacz_element', views_t.elementstranslate, name='elementstranslate'
     ),
]
