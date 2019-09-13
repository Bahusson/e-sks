from django.urls import path
from . import views, views_c

urlpatterns = [
    path('', views.home, name='home'),
    path('aktualnosci', views.blogs, name='blogs'),
    path('aktualnosc/<int:blog_id>/', views.blog, name='blog'),
    path('informacje', views.infos, name='infos'),
    path('informacja/<int:info_id>/', views.info, name='info'),
    path('mapa_strony', views.pagemap, name='pagemap'),
    # Widoki edytorskie dla rady studentów:
    path('zrob_akt/<int:blog_id>/', views_c.make_blog, name='make_blog'),
    path('zrob_info/<int:blog_id>/', views_c.make_info, name='make_info'),
    path('zrob_plik/<int:blog_id>/', views_c.make_file, name='make_file'),
    path('zmien_akt/<int:blog_id>/', views_c.change_blog, name='change_blog'),
    path('zmien_info/<int:blog_id>/', views_c.change_info, name='change_info'),
    path('zmien_plik/<int:blog_id>/', views_c.change_file, name='change_file'),
]
