# Widoki Rady Studentów
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad, PageElement, AllParties
from .models import PortalBaseItem as Pbi
from .models import CouncilMenuItem as Cmi
from .models import CouncilLinkItem as Cli
from .models import UserMenuItem as Umi
from .models import UserLinkItem as Uli
from .models import HousingParty as HParty
from .models import HousingPartyItems as Hpi
from rekruter.models import ApplicationFormFields as Apf
from rekruter.models import ApplicationStatus as Aps
from rekruter.models import StudentHouse as Sh
from rekruter.models import IfRoomChange as Ifr
from rekruter.models import TimePeriod as Tper
from rekruter.models import StudyFaculty as Stf
from rekruter.models import StudyDegree as Std
from rekruter.models import SpouseCohabitant as Sch
from rekruter.models import SpecialCase as Scs
from esks.special.decorators import council_only
from esks.special.snippets import menu_switcher
from rekruter.models import User, FormItems, QuarterClassB
from rekruter.forms import PartyForm, IniForm
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


# Z dwóch poniższych zrób klasę jak będziesz miał chwilę
# i powarunkuj, bo są bardzo podobne - albo niech Kenny to zrobi dla wprawy.
# Tworzy nową akcję kwaterunkową wraz z formularzem z poziomu przew. rady.
@council_only(login_url='staffpanel_c', power_level=2)  # Tylko Przewodniczący
def makemeparty(request):
    userdata = User.objects.get(
     id=request.user.id)
    # Formularz serwisowy pola niewymagane
    service = False
    if request.method == 'POST':
        form = PartyForm(request.POST)
        if form.is_valid():
            form.save(userdata)
            return redirect('staffpanel_c')
    else:
        form = PartyForm()
        pe_fi = PageElement(FormItems)
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
         'p_item': hpi.baseattrs,
         'service': service,
         }
        pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'forms/partymaker.html'
        return render(request, template, context_lazy)


@council_only(login_url='allparties', power_level=2)  # Tylko Przewodniczący
def changemeparty(request):
    userdata = User.objects.get(
     id=request.user.id)
    party_id = request.session.get('partyid')
    # Formularz serwisowy pola niewymagane
    service = False
    if request.method == 'POST':
        instance = HParty.objects.get(id=int(party_id))
        instance2 = G404(HParty, id=int(party_id))
        form = PartyForm(request.POST, instance=instance2)
        if form.is_valid():
            form.save(userdata)
            return redirect('allparties')
    else:
        party_id = request.session.get('partyid')
        varlist = []
        varlist.append(party_id)
        instance = G404(HParty, id=party_id)
        form = PartyForm(instance=instance)
        quart = int(instance.quarter)
        varlist.append(quart)
        pe_fi = PageElement(FormItems)
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
         'p_item': hpi.baseattrs,
         'varlist': varlist,
         'service': service,
         }
        pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'forms/partymaker.html'
        return render(request, template, context_lazy)


# Pokazuje różne akcje kwaterunkowe - widok oparty na klasach.
# Widok zależy od tego kto patrzy. User czy Radny. (menu_switcher)
def allparties(request):
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
    userlevel = request.user.role_council
    if userlevel > 1:
        userlevel = 1
    cmenu = [1, Cmi, Cli]
    umenu = [0, Umi, Uli]
    menusdict = menu_switcher(cmenu, umenu)
    userkey = 'menu'+str(userlevel)
    d_num = menusdict[userkey][0]
    d_menu = menusdict[userkey][1]
    d_list = menusdict[userkey][2]
    pl = PortalLoad(P, L, Pbi, d_num, d_menu, d_list)
    context_lazy = pl.lazy_context(skins=S, context=ap.context)
    template = 'panels/common/allparties.html'
    return render(request, template, context_lazy)


# Pokazuje wszystkie wnioski o akademik i filtruje je względem kryteriów.
@council_only(login_url='logger')
def allapplied(request):
    view_filter = ["-timeapplied", "owner__last_name", "status"]
    if 'sort' in request.POST:
        x = 0
        while x < 3:
            view_filter[x] = str(request.POST.get('view_filter'+str(x)))
            x = x+1
    apf = Apf.objects.order_by(view_filter[0], view_filter[1], view_filter[2])
    peqc = PageElement(QuarterClassB)
    aps = PageElement(Aps)
    ifr = PageElement(Ifr)
    sh = PageElement(Sh)
    pe_fi = PageElement(FormItems)
    context = {
     'applied': apf,
     'view_filter': view_filter,
     'setter': peqc.listed,
     'appstatus': aps.listed,
     'roomchange': ifr.listed,
     'hotelselector': sh.listed,
     'formitem': pe_fi.baseattrs,
     }
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = 'panels/council/allapplied.html'
    return render(request, template, context_lazy)


# Pokazuje zbiorczo wejście na profile wszystkich użytkowników. Sortowalne.
# Docelowo ma mieć wyszukiwanie czasu rzeczywistego. WIP. Niepodłączone...
@council_only(login_url='staffpanel_c', power_level=2)  # Tylko Przewodniczący
def allusers(request):
    view_filter = ["last_name", "first_name", "quarter"]
    if 'sort' in request.POST:
        x = 0
        while x < 3:
            view_filter[x] = str(request.POST.get('view_filter'+str(x)))
            x = x+1
    usr = User.objects.order_by(view_filter[0], view_filter[1], view_filter[2])
    pe_fi = PageElement(FormItems)
    peqc = PageElement(QuarterClassB)
    context = {
     'userdetails': usr,
     'setter': peqc.listed,
     'view_filter': view_filter,
     'formitem': pe_fi.baseattrs,
     }
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = 'panels/council/allusers.html'
    return render(request, template, context_lazy)


# Pozwala członkom rady spojrzeć na profil innego usera.
@council_only(login_url='logger')
def changeuser(request, user_id):
    service = True
    userdata = User.objects.get(
     id=user_id)
    if 'quarter' in request.POST:
        form = IniForm(request.POST, instance=userdata)
        if form.is_valid():
            form.save()
            return redirect('allusers')
    else:
        form = IniForm()
        pe_fi = PageElement(FormItems)
        quarter = userdata.__dict__['quarter']
        peqc = PageElement(QuarterClassB)
        if quarter == '':
            myquarter = 'Nieprzydzielony!!!'
        else:
            myquarter = peqc.list_specific(int(quarter)-1)
        quarterlist = peqc.listed
        context = {
         'form': form,
         'service2': service,
         'setter': myquarter,
         'setlist': quarterlist,
         'udata': userdata,
         'formitem': pe_fi.baseattrs,
         }
        pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'panels/user/mydata.html'
        return render(request, template, context_lazy)
