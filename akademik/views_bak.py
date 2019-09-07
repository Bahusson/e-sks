from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
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
from .models import HousingPartyItems as Hpi
from rekruter.models import StudentHouse as Sh
from rekruter.models import IfRoomChange as Ifr
from rekruter.models import TimePeriod as Tper
from rekruter.models import StudyFaculty as Stf
from rekruter.models import StudyDegree as Std
from rekruter.models import SpouseCohabitant as Sch
from rekruter.models import SpecialCase as Scs
from esks.special.decorators import council_only, hotel_staff_only, translators_only
from rekruter.models import User, FormItems, QuarterClassB
from rekruter.forms import IniForm, ApplicationForm, PartyForm
import datetime
import pytz


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


class PartyMaster(object):
    # Podstawka zwraca wszystkie akcje kwaterunkowe
    def __init__(self):
        self.all_parties = PageElement(HParty)
        tz_UTC = pytz.timezone('Europe/Warsaw')
        self.dt_now = datetime.datetime.now(tz_UTC)
        self.list_parties = self.all_parties.listed

    # Zwraca wszystkie akcje bez względu na czas serwera (atrybuty)
    def full_party(self, **kwargs):
        full_parties = []
        attrname = kwargs['attrname']
        x = 0
        for item in self.list_parties:
            full_parties.append(
             str(self.list_parties[x].__dict__[attrname]))
            x = x+1
        return full_parties

    # Zwraca tylko aktywne akcje względem czasu serwera (atrybuty)
    def active_party(self, **kwargs):
        active_parties = []
        attrname = kwargs['attrname']
        x = 0
        for item in self.list_parties:
            if self.list_parties[x].__dict__['date_start'] <= self.dt_now <= self.list_parties[x].__dict__['date_end']:
                active_parties.append(
                 str(self.list_parties[x].__dict__[attrname]))
            x = x+1
        return active_parties

    # Tylko nieaktywne akcje względem czasu serwera (atrybuty)
    def past_party(self, **kwargs):
        inactive_parties = []
        attrname = kwargs['attrname']
        x = 0
        for item in self.list_parties:
            if self.list_parties[x].__dict__['date_end'] < self.dt_now:
                inactive_parties.append(
                 str(self.list_parties[x].__dict__[attrname]))
            x = x+1
        return inactive_parties

    # Tylko zaplanowane akcje względem czasu serwera (atrybuty)
    def future_party(self, **kwargs):
        future_parties = []
        attrname = kwargs['attrname']
        x = 0
        for item in self.list_parties:
            if self.list_parties[x].__dict__['date_start'] > self.dt_now:
                future_parties.append(
                 str(self.list_parties[x].__dict__[attrname]))
            x = x+1
        return future_parties


def party_switch(request):
    y = PartyMaster()
    x = y.active_party(attrname="quarter")
    quarter = request.user.quarter
    if quarter in x:
        print('nowy formularz...')
        return 0
    else:
        print('przekierowuję...')
        return 1


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
             'formitem': pe_fi.baseattrs,
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


# Tworzy nową akcję kwaterunkową wraz z formularzem z poziomu przew. rady.
@council_only(login_url='staffpanel_c', power_level=2)  # Tylko Przewodniczący
def makemeparty(request, party_id):
    userdata = User.objects.get(
     id=request.user.id)
    if request.method == 'POST':
        form = PartyForm(request.POST)
        if form.is_valid():
            form.save(userdata)
            return redirect('staffpanel_c')
    else:
        pe_fi = PageElement(FormItems)
        form = PartyForm()
        sh = PageElement(Sh)
        ifr = PageElement(Ifr)
        tper = PageElement(Tper)
        stf = PageElement(Stf)
        std = PageElement(Std)
        sch = PageElement(Sch)
        scs = PageElement(Scs)
        peqc = PageElement(QuarterClassB)
        hpi = PageElement(Hpi)
        context = {
         'udata': userdata,
         'formitem': pe_fi.baseattrs,
         'form2': form,
         'houselist': sh.listed,
         'staylist': ifr.listed,
         'periodlist': tper.listed,
         'facultylist': stf.listed,
         'degreelist': std.listed,
         'spouselist': sch.listed,
         'scaselist': scs.listed,
         'setlist': peqc.listed,
         'p_item':hpi.baseattrs
         }
        pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'forms/partymaker.html'
        return render(request, template, context_lazy)


# Na razie pokazuje tylko akcje aktywne.
# Do zmiany, żeby był wybór.
@council_only(login_url='logger')
def allparties(request, view_filter="2"):
    pm = PartyMaster()
    all_parties = pm.all_parties
    range = {
     "1": pm.full_party(attrname="id"),
     "2": pm.active_party(attrname="id"),
     "3": pm.past_party(attrname="id"),
     "4": pm.future_party(attrname="id"),
    }
    if request.method == 'POST':
        view_filter = str(request.POST.get('view_filter'))
    active_parties = []
    for item in range[view_filter]:
        obj = all_parties.elements.get(pk=item)
        active_parties.append(obj)
    pe_fi = PageElement(FormItems)
    all_parties = PageElement(HParty)
    hpi = PageElement(Hpi)
    peqc = PageElement(QuarterClassB)
    context = {
     'formitem': pe_fi.baseattrs,
     'parties': active_parties,
     'p_item':hpi.baseattrs,
     'setter': peqc.listed,
     'view_filter': view_filter,
     }
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = 'panels/council/allparties.html'
    return render(request, template, context_lazy)
