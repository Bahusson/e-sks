from django.shortcuts import render, redirect
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad, PageElement
from .models import PortalBaseItem as Pbi
from .models import UserMenuItem as Umi
from .models import UserLinkItem as Uli
from .models import CouncilMenuItem as Cmi
from .models import CouncilLinkItem as Cli
from .models import TranslatorMenuItem as Tmi
from .models import TranslatorLinkItem as Tli
from .models import HotelMenuItem as Hmi
from .models import HotelLinkItem as Hli
from .models import HousingParty as HParty
from rekruter.models import StudentHouse as Sh
from rekruter.models import IfRoomChange as Ifr
from rekruter.models import TimePeriod as Tper
from rekruter.models import StudyFaculty as Stf
from rekruter.models import StudyDegree as Std
from rekruter.models import SpouseCohabitant as Sch
from rekruter.models import SpecialCase as Scs
from esks.special.decorators import council_only, hotel_staff_only, translators_only
from rekruter.models import User, FormItems, QuarterClassB
from rekruter.forms import IniForm, ApplicationForm
import datetime
import pytz
# from django.core.files.uploadedfile import SimpleUploadedFile


# Panel Rady
@council_only(login_url='logger')
def staffpanel_c(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panels/council/panel_rady.html'
    return render(request, template, context_lazy)


# Panel Obsługi Akademików
@hotel_staff_only(login_url='logger')
def staffpanel_h(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PortalLoad(P, L, Pbi, 2, Hmi, Hli)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panels/hotel/panel_akademika.html'
    return render(request, template, context_lazy)


# Panel Tłumaczeniowy
@translators_only(login_url='logger')
def translatorpanel(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PortalLoad(P, L, Pbi, 3, Tmi, Tli)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panels/translator/panel_tlumacza.html'
    return render(request, template, context_lazy)


# Panel użytkownika.
# Jeśli nie masz jeszcze przydzielonej kwatery,
# przekieruje Cię najpierw do przydziału.
def userpanel(request):
    quarter = request.user.quarter
    if quarter == '':
        return redirect('initial')
    else:
        # zdefiniuj dodatkowe konteksty tutaj.
        pl = PortalLoad(P, L, Pbi, 0, Umi, Uli, )
        context_lazy = pl.lazy_context(skins=S)
    template = 'panels/user/panel_uzytkownika.html'
    return render(request, template, context_lazy)


# Funkcja pokazuje dane użytkownika i pozwala zmienić akcję kwaterunkową.
def showmydata(request):
    userdata = User.objects.get(
     id=request.user.id)
    if request.method == 'POST':
        form = IniForm(request.POST, instance=userdata)
        if form.is_valid():
            form.save()
            return redirect('userdatapersonal')
    else:
        pe_fi = PageElement(FormItems)
        pe_fi0 = pe_fi.list_specific(0)
        peqc = PageElement(QuarterClassB)
        form = IniForm()
        quarter = userdata.__dict__['quarter']
        myquarter = peqc.list_specific(int(quarter)-1)
        quarterlist = peqc.listed
        context = {
         'formitem': pe_fi0,
         'form': form,
         'setter': myquarter,
         'setlist': quarterlist,
         'udata': userdata,
         }
        # zdefiniuj dodatkowe konteksty tutaj.
        pl = PortalLoad(P, L, Pbi, 0, Umi, Uli, )
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'panels/user/mydata.html'
        return render(request, template, context_lazy)


# Funkcja zwraca numery akcji kwaterunkowych, które są aktualnie 'aktywne'
# względem czasu serwera.
def active_party():
    active_parties = []
    all_parties = PageElement(HParty)
    tz_UTC = pytz.timezone('Europe/Warsaw')
    dt_now = datetime.datetime.now(tz_UTC)
    list_parties = all_parties.listed
    x = 0
    for item in list_parties:
        if list_parties[x].__dict__['date_start'] <= dt_now <= list_parties[x].__dict__['date_end']:
            active_parties.append(str(list_parties[x].__dict__['quarter']))
        x = x+1
    return active_parties


def party_switch(request):
    x = active_party()
    quarter = request.user.quarter
    if quarter in x:
        print('nowy formularz...')
        return 0
    else:
        print('przekierowuję...')
        return 1
    # User zdaje test na to,
    # czy jego atrybut (akcja kwaterunkowa) jest na liście

    # Jesli tak, dostaje przekierowanie na odpowiedni widok formularza

    # Jeśli nie, dostaje przekierowanie na widok
    # na którym jest lista aktywnych akcji

    # + Jeśli tak ale ma wypełnioy, (dodaj foreign field do formularza,
    # albo ekstra pola z info na której stronie jest)
    # to dostaje przekierowanie na inny widok (ten na którym skończył)


# Jeden widok dla wszystkich formularzy aplikacyjnych.
def dormapply(request):
    userdata = User.objects.get(
     id=request.user.id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save(userdata)
            return redirect('userpanel')
    else:
        redir = party_switch(request)
        if redir == 1:
            return redirect('initial')  # Gdzie przekierować jak nie jego akcja?
        else:
            pe_fi = PageElement(FormItems)
            pe_fi0 = pe_fi.list_specific(0)
            form = ApplicationForm()
            sh = PageElement(Sh)
            ifr = PageElement(Ifr)
            tper = PageElement(Tper)
            stf = PageElement(Stf)
            std = PageElement(Std)
            sch = PageElement(Sch)
            scs = PageElement(Scs)
            context = {
             'udata': userdata,
             'formitem': pe_fi0,
             'form': form,
             'houselist': sh.listed,
             'staylist': ifr.listed,
             'periodlist': tper.listed,
             'facultylist': stf.listed,
             'degreelist': std.listed,
             'spouselist': sch.listed,
             'scaselist': scs.listed,
             }
            pl = PortalLoad(P, L, Pbi, 0, Umi, Uli, )
            context_lazy = pl.lazy_context(skins=S, context=context)
            template = 'forms/dormapply.html'
            return render(request, template, context_lazy)
