# Widoki Rady Studentów
from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from django.db.models import Q
from strona.models import (Pageitem as P, PageSkin as S)
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad, PageElement, AllParties
from .models import (
 PortalBaseItem as Pbi, CouncilMenuItem as Cmi, CouncilLinkItem as Cli,
 UserMenuItem as Umi, UserLinkItem as Uli, HousingParty as HParty,
 HousingPartyItems as Hpi, ApplicationListItems as Ali, UserListItems as Usli,
 AdminTextTools as Att)
from rekruter.models import (
 ApplicationFormFields as Apf, ApplicationStatus as Aps, StudentHouse as Sh,
 IfRoomChange as Ifr, TimePeriod as Tper, StudyFaculty as Stf,
 StudyDegree as Std, SpouseCohabitant as Sch, SpecialCase as Scs)
from esks.special.decorators import council_only
from esks.special.snippets import menu_switcher
from rekruter.models import User, FormItems, QuarterClassB
from rekruter.forms import PartyForm, IniForm, PowerForm, BasicPowerForm
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
    ali = PageElement(Ali)
    att = PageElement(Att)
    context = {
     'applied': apf,
     'view_filter': view_filter,
     'setter': peqc.listed,
     'appstatus': aps.listed,
     'roomchange': ifr.listed,
     'hotelselector': sh.listed,
     'formitem': pe_fi.baseattrs,
     'applist': ali.listed,
     'attools': att.baseattrs,
     }
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = 'panels/council/allapplied.html'
    return render(request, template, context_lazy)


# Pokazuje zbiorczo wejście na profile wszystkich użytkowników. Sortowalne.
# Docelowo ma mieć wyszukiwanie czasu rzeczywistego. WIP. Niepodłączone...
@council_only(login_url='staffpanel_c', power_level=2)  # Tylko Przewodniczący
def allusers(request):
    query = request.GET.get('q', None)
    view_filter = ["-last_name", "first_name", "quarter"]
    if 'sort' in request.POST:
        x = 0
        while x < 3:
            view_filter[x] = str(request.POST.get('view_filter'+str(x)))
            x = x+1
    usr = User.objects.order_by(view_filter[0], view_filter[1], view_filter[2])
    if query is not None:
        usr = usr.filter(
         Q(first_name__icontains=query)|
         Q(last_name__icontains=query)|
         Q(citizenship__icontains=query))
    pe_fi = PageElement(FormItems)
    peqc = PageElement(QuarterClassB)
    usli = PageElement(Usli)
    att = PageElement(Att)
    context = {
     'userdetails': usr,
     'setter': peqc.listed,
     'view_filter': view_filter,
     'formitem': pe_fi.baseattrs,
     'userlist': usli.listed,
     'attools': att.baseattrs,
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
    roledict = {1: False, 2: True, 3: True, 4: True}
    dictrole = {None: 1, 'on': 2}
    if 'quarter' in request.POST:
        form = IniForm(request.POST, instance=userdata)
        if form.is_valid():
            form.save()
            return redirect('changeuser', user_id)
    elif 'power' in request.POST:
        form2 = PowerForm(request.POST, instance=userdata)
        if form2.is_valid():
            key = request.POST.get('role_council')
            form2.save(dictrole[key])
            return redirect('changeuser', user_id)
    else:
        if userdata.role_council is None:
            cform = BasicPowerForm(request.POST, instance=userdata)
            if cform.is_valid():
                cform.save(1)
                return redirect('changeuser', user_id)
        key2 = userdata.role_council
        form = IniForm()
        form2 = PowerForm(
         instance=userdata, initial={'role_council': roledict[key2]})
        pe_fi = PageElement(FormItems)
        quarter = userdata.__dict__['quarter']
        peqc = PageElement(QuarterClassB)
        if quarter == '':
            myquarter = 'Nieprzydzielony!!!'
        else:
            myquarter = peqc.list_specific(int(quarter)-1)
        quarterlist = peqc.listed
        att = PageElement(Att)
        context = {
         'form': form,
         'form2': form2,
         'service2': service,
         'setter': myquarter,
         'setlist': quarterlist,
         'udata': userdata,
         'formitem': pe_fi.baseattrs,
         'attools': att.baseattrs,
         }
        pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'panels/user/mydata.html'
        return render(request, template, context_lazy)
