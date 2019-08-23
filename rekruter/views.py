from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  # , logout
from .models import Sito
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from .models import FormItems, User
from django.contrib.auth.forms import AuthenticationForm
from .forms import ExtendedCreationForm, IniForm


# Wstępny formularz przydzielający akcję kwaterunkową.
# Posiada jedno ukryte pole które zmienia akcję kwaterunkową usera.
def initial(request):
    if request.method == 'POST':
        uid = User.objects.get(id=request.user.id)
        form = IniForm(request.POST, instance=uid)
        if form.is_valid():
            form.save()
            return redirect('userdatapersonal')

    else:
        form = IniForm()
        pl = PageLoad(P, L)
        locations = list(Sito.objects.all())
        sitos = locations[0]
        context = {
         'form': form,
         'sitos': sitos,
         'items': pl.items,
         'langs': pl.langs, }
        template = 'registration/initial.html'
        return render(request, template, context)


# Formularz rejestracji. Do wywalenia po zmienie autentykacji.
def register(request):
    if request.method == 'POST':
        form = ExtendedCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            # Sprawdza shaszowane dane powyżej w bazie danych.
            login(request, user)
            return redirect('home')
            # Przekierowuje na stronę główną zalogowanego usera.
    else:
        form = ExtendedCreationForm()
        locations = list(FormItems.objects.all())
        items = locations[0]
        context = {'form': form,
                   'item': items, }
    template = 'registration/register.html'
    return render(request, template, context)


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
        context = {'form': form,
                   'item': items,
                   'item1': items1, }
        template = 'registration/login.html'
    return render(request, template, context)

    '''
    # Tutaj odbieramy zmienną zdefiniowaną wcześniej.
    quarter = request.session['quarter']
    locations = list(QuarterClass.objects.all())
    quarters = locations[0]
    quartzlist = [
     'stud_local', 'stud_foreign', 'phd', 'bank',
     'new1', 'new23', 'new_foreign', 'erasmus', 'bilateral',
    ]  # To nie powinno być na stałe w kodzie ale jako zmienna z panelu admina.
    setter = quarters.__getattribute__(quartzlist[int(quarter)-1])
    '''
# def unlogger(request):
