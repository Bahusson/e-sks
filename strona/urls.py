from django.urls import path
from . import views, views_c

urlpatterns = [
    path('', views.home, name='home'),
    path('mapa_strony', views.pagemap, name='pagemap'),
    path('aktualnosci', views.allblogs, name='allblogs'),
    path('informacje', views.allinfos, name='allinfos'),
    path('wazne_pliki', views.allfiles, name='allfiles'),
    path('aktualnosc/<int:blog_id>/', views.blog, name='blog'),
    path('informacja/<int:info_id>/', views.info, name='info'),
    # Widoki edytorskie dla rady studentów:
    path('dodaj/<form_type>/', views_c.make_element, name='make_element'),
    path(
     'zmien/<form_type>/<int:form_id>',
     views_c.change_element, name='change_element'),
    path(
     'zmien_element/<elem_type>/', views_c.allelements, name='allelements'),
]
