from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  # , logout
from .models import Sito
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from .models import FormItems, QuarterClass
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm, ProfileForm


# Wstępny formularz przydzielający akcję kwaterunkową.
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


# Formularz logowania. Do przeróbki po zmienie autentykacji.
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


# Formularz rejestracji. Do wywalenia po zmienie autentykacji.
def register(request):
    # Tutaj odbieramy zmienną zdefiniowaną wcześniej.
    quarter = request.session['quarter']
    locations = list(QuarterClass.objects.all())
    quarters = locations[0]
    quartzlist = [
     'stud_local', 'stud_foreign', 'phd', 'bank',
     'new1', 'new23', 'new_foreign', 'erasmus', 'bilateral',
    ]  # To nie powinno być na stałe w kodzie ale jako zmienna z panelu admina.
    setter = quarters.__getattribute__(quartzlist[int(quarter)-1])
    if request.method == 'POST':
        form = UserForm(request.POST)
        #profile_form = ProfileForm(request.POST)
        # Po rejestracji automatycznie loguje klienta podanym loginem i hasłem.
        if form.is_valid():
            user = form.save()
            #userprofile = profile_form.saveq(quarter, commit=False)
            #userprofile.user = user
            #userprofile.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            # Sprawdza shaszowane dane powyżej w bazie danych.
            login(request, user)
            return redirect('home')
            # Przekierowuje na stronę główną zalogowanego usera.
    else:
        form = UserForm()
        locations = list(FormItems.objects.all())
        items = locations[0]
        context = {'form': form,
                   'item': items,
                   'setter': setter, }
    return render(request, 'registration/register.html', context)


# def unlogger(request):
