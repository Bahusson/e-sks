from django.shortcuts import render, get_object_or_404
from django.utils import translation

from .models import Sito

# Create your views here.
def initial(request):
    locations = list(Sito.objects.all())
    sitos = locations[0]
    return render(request, 'initial.html', {'sitos': sitos})
