from django.shortcuts import render, get_object_or_404, redirect
from django.utils import translation
from django.contrib.auth import authenticate, login
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_datap['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)
