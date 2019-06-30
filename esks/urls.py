"""esks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import strona.views
import rekruter.views

urlpatterns = [
    path('admin/', admin.site.urls), #Zmień nazwę żeby była zmyłka dla botów próbujących się dostać do strony administracji
    path('', include('strona.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('initial/', rekruter.views.initial, name='initial'),
    path('strona/', include('strona.urls')),
    path('rekruter/', include('rekruter.urls')), #strona rejestracji do systemu akademików (dla studentów)
#    path('akademik/', include('akademik.urls')), #strona administracyjna dla rady studentów i administracji akademika
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #pliki statyczne ładowane tylko manualnie z poziomu serwera.
