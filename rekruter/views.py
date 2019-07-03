from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Sito
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from .models import ExtendedCreationForm, FormItems, QuarterClass
from django.contrib.auth.forms import AuthenticationForm


def initial(request):
    if request.method == 'POST':
        # Tworzy zmienną dla sesji użytkownika do późniejszego wykorzystania.
        request.session['quarter'] = request.POST['quarter']
        return redirect('register')
    else:
        pl = PageLoad(P, L)
        locations = list(Sito.objects.all())
        sitos = locations[0]
    context = {'sitos': sitos, 'items': pl.items, 'langs': pl.langs}
    return render(request, 'registration/initial.html', context)


def logger(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Tutaj trzeba wstawić jakiś error message.
            pass
    else:
        form = AuthenticationForm()
        locations = list(FormItems.objects.all())
        items = locations[0]
        locations1 = list(P.objects.all())
        items1 = locations1[0]
    context = {'form': form, 'item': items, 'item1': items1, }
    return render(request, 'registration/login.html', context)


def register(request):
    # Tutaj odbieramy zmienną zdefiniowaną wcześniej.
    quarter = request.session['quarter']
    locations = list(QuarterClass.objects.all())
    quarters = locations[0]
    quartzlist = [
    'stud_local', 'stud_foreign', 'phd', 'bank',
    'new1', 'new23', 'new_foreign', 'erasmus', 'bilateral',
    ]
    setter = quarters.__dict__[quartzlist[int(quarter)-1]]
    if request.method == 'POST':  # Jeśli wysyłamy formularz do Bazy danych.
        form = ExtendedCreationForm(request.POST)

        # Po rejestracji automatycznie loguje klienta podanym loginem i hasłem.
        if form.is_valid():  # Jeśli formularz jest poprawny.
            form.save(quarter)      # Zapisz formularz.
            username = form.cleaned_data['username']  # Nazwa Usera z prawidłowego formularza.
            password = form.cleaned_data['password1']  # Hasło j.w.
            user = authenticate(username=username, password=password)  # Sprawdza shaszowane dane powyżej w bazie danych.
            login(request, user)  # Loguje usera.
            return redirect('home')  # Przekierowuje na stronę główną zalogowanego usera.
    else:  # Zanim wyślemy cokolwiek mysimy wygenerować formularz na stronie.
        form = ExtendedCreationForm()
        locations = list(FormItems.objects.all())
        items = locations[0]
        context = {'form': form,
                   'item': items,
                   'quarter': quarter,
                   'setter': setter}
    return render(request, 'registration/register.html', context)


#def unlogger(request):
