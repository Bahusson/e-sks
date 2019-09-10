from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad, PageElement, PartyMaster
from esks.special.classes import AllParties
from .models import PortalBaseItem as Pbi
from .models import UserMenuItem as Umi
from .models import UserLinkItem as Uli
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
from esks.special.decorators import hotel_staff_only, translators_only
from rekruter.models import User, FormItems, QuarterClassB
from rekruter.forms import IniForm, ApplicationForm
import datetime
import pytz


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


def party_switch(request):
    y = PartyMaster(HParty, pytz, datetime)
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
    service = True
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save(userdata)
            return redirect('userpanel')
    else:
        redir = party_switch(request)
        if redir == 1:
            return redirect('showparties')  # Gdzie przekierować?
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
             'service': service
             }
            pl = PortalLoad(P, L, Pbi, 0, Umi, Uli, )
            context_lazy = pl.lazy_context(skins=S, context=context)
            template = 'forms/dormapply.html'
            return render(request, template, context_lazy)


# Pokazuje różne akcje kwaterunkowe - widok oparty na klasach.
def showparties(request):
    userdata = User.objects.get(
     id=request.user.id)
    view_filter = "2"
    if 'subbutton' in request.POST:
        view_filter = str(request.POST.get('view_filter'))
    elif 'changeparty' in request.POST:
        request.session['partyid'] = request.POST.get('partyid')
        return redirect('changemeparty')
    elif 'apply_spontaneously' in request.POST:
        form = IniForm(request.POST, instance=userdata)
        if form.is_valid():
            form.save()
            return redirect('dsapply')
    ap = AllParties(
     request, HParty, pytz, datetime, FormItems, Hpi, QuarterClassB,
     view_filter=view_filter, )
    pl = PortalLoad(P, L, Pbi, 0, Umi, Uli)
    context_lazy = pl.lazy_context(skins=S, context=ap.context)
    template = 'panels/common/allparties.html'
    return render(request, template, context_lazy)
