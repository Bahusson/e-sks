from django.shortcuts import render, get_object_or_404
from django.utils import translation
from .models import Sito
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import Langmenu

# Create your views here.
def initial(request):
    items = Langmenu(P,L).flag
    langs = Langmenu(P,L).list
    locations = list(Sito.objects.all())
    sitos = locations[0]
    return render(request, 'initial.html', {'sitos': sitos, 'items': items, 'langs': langs})
