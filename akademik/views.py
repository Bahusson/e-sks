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
from rekruter.models import StudentHouse as Sh
from rekruter.models import IfRoomChange as Ifr
from rekruter.models import TimePeriod as Tper
from rekruter.models import StudyFaculty as Stf
from rekruter.models import StudyDegree as Std
from esks.special.decorators import council_only, hotel_staff_only, translators_only
from rekruter.models import User, FormItems, QuarterClassB
from rekruter.forms import IniForm, ApplicationForm
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


def dormapply(request):
    userdata = User.objects.get(
     id=request.user.id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES, instance=userdata)
        if form.is_valid():
            form.save()
            return redirect('userpanel')
    else:
        sh = PageElement(Sh)
        ifr = PageElement(Ifr)
        tper = PageElement(Tper)
        stf = PageElement(Stf)
        std = PageElement(Std)
        pe_fi = PageElement(FormItems)
        pe_fi0 = pe_fi.list_specific(0)
        form = ApplicationForm()
        context = {
         'formitem': pe_fi0,
         'form': form,
         'udata': userdata,
         'houselist': sh.listed,
         'staylist': ifr.listed,
         'periodlist': tper.listed,
         'facultylist': stf.listed,
         'degreelist': std.listed,
         }
    pl = PortalLoad(P, L, Pbi, 0, Umi, Uli, )
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = 'panels/user/dormapply.html'
    return render(request, template, context_lazy)
