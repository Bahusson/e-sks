from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from strona.models import (Pageitem as P, PageSkin as S)
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad, PageElement, PartyMaster
from .models import (
 PortalBaseItem as Pbi, UserMenuItem as Umi, UserLinkItem as Uli,
 HotelMenuItem as Hmi, HotelLinkItem as Hli, HousingParty as HParty)
from rekruter.models import (
 StudentHouse as Sh, IfRoomChange as Ifr, TimePeriod as Tper,
 StudyFaculty as Stf, StudyDegree as Std, SpouseCohabitant as Sch,
 SpecialCase as Scs, User, FormItems, QuarterClassB)
from esks.special.decorators import hotel_staff_only
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
        peqc = PageElement(QuarterClassB)
        form = IniForm()
        quarter = userdata.__dict__['quarter']
        myquarter = peqc.list_specific(int(quarter)-1)
        quarterlist = peqc.listed
        context = {
         'formitem': pe_fi.baseattrs,
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


# Funkcja sprawdza czy akcja użytkownika jest tą właściwą i jeśli nie,
# daje mu inne do wyboru. Rownież w razie jakby ktoś dał ciała i zdefiniował
# dwie akcje kwaterunkowe tego samego typu, to funkcja zwróci Id tylko 1.
def party_switch(request):
    y = PartyMaster(HParty, pytz, datetime)
    z = y.dict_active_id_quarter()
    print(z)
    quarter = request.user.quarter
    if quarter in z.values():
        # Ten kawałek uzyskuje pierwszy klucz z wartości słownika...
        a = list(z.keys())[list(z.values()).index(quarter)]
        print('nowy formularz...')
        request.session['partyformid'] = a
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
            form.save(userdata, request=request)
            return redirect('userpanel')
    else:
        redir = party_switch(request)
        if redir == 1:
            return redirect('allparties')  # Gdzie przekierować?
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
            hp = PageElement(HParty)
            puzzle = hp.by_id(G404=G404, id=request.session['partyformid'])
            context = {
             'udata': userdata,
             'formitem': pe_fi.baseattrs,
             'form': form,
             'houselist': sh.list_shorter(cut_fr=1),
             'staylist': ifr.list_shorter(cut_fr=1),
             'periodlist': tper.list_shorter(cut_fr=1),
             'facultylist': stf.list_shorter(cut_fr=1),
             'degreelist': std.list_shorter(cut_fr=1),
             'spouselist': sch.list_shorter(cut_fr=1),
             'scaselist': scs.list_shorter(cut_fr=1),
             'service': service,
             'puzzle': puzzle
             }
            pl = PortalLoad(P, L, Pbi, 0, Umi, Uli, )
            context_lazy = pl.lazy_context(skins=S, context=context)
            template = 'forms/dormapply.html'
            return render(request, template, context_lazy)
