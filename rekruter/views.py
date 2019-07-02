from django.shortcuts import render, get_object_or_404, redirect
from django.utils import translation
from django.contrib.auth import authenticate, login
from .models import Sito
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from .models import ExtendedCreationForm


# Create your views here.
def initial(request):
    pl = PageLoad(P, L)
    locations = list(Sito.objects.all())
    sitos = locations[0]
    return render(request, 'registration/initial.html', {'sitos': sitos, 'items': pl.items, 'langs': pl.langs})

def register(request):
    if request.method == 'POST':  # Jeśli wysyłamy formularz do Bazy danych.
        form = ExtendedCreationForm(request.POST)

        # Po rejestracji automatycznie loguje klienta podanym loginem i hasłem.
        if form.is_valid():  # Jeśli formularz jest poprawny.
            form.save()      # Zapisz formularz.
            username = form.cleaned_data['username']  # Nazwa Usera z prawidłowego formularza.
            password = form.cleaned_data['password1']  # Hasło j.w.
            user = authenticate(username=username, password=password)  # Sprawdza shaszowane dane powyżej w bazie danych.
            login(request, user)  # Loguje usera.
            return redirect('home')  # Przekierowuje na stronę główną zalogowanego usera.

    else:  # Zanim wyślemy cokolwiek mysimy wygenerować formularz na stronie.
        form = ExtendedCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)
