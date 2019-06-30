from django.shortcuts import render, get_object_or_404
from django.utils import translation
from .models import Sito
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def initial(request):
    pl = PageLoad(P, L)
    locations = list(Sito.objects.all())
    sitos = locations[0]
    return render(request, 'registration/initial.html', {'sitos': sitos, 'items': pl.items, 'langs': pl.langs})


def register(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
