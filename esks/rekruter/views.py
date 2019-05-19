from django.shortcuts import render, get_object_or_404
from django.utils import translation

from .models import Sito

# Create your views here.
def initial(request):
    sito = Sito.objects
    return render(request, 'initial.html', {'sito': sito})
