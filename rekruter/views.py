from django.shortcuts import render, get_object_or_404
from django.utils import translation
from .models import Sito
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad

# Create your views here.
def register(request):
    pl = PageLoad(P,L)
    locations = list(Sito.objects.all())
    sitos = locations[0]
    return render(request, 'rekruter/register.html', {'sitos': sitos, 'items': pl.items, 'langs': pl.langs})
