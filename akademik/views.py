from django.shortcuts import render, redirect
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad
from .models import PortalBaseItem as Pbi
from .models import UserMenuItem as Umi
from .models import UserLinkItem as Uli
from .models import CouncilMenuItem as Cmi
from .models import CouncilLinkItem as Cli
from .models import TranslatorMenuItem as Tmi
from .models import TranslatorLinkItem as Tli
from .models import HotelMenuItem as Hmi
from .models import HotelLinkItem as Hli
from esks.special.decorators import council_only, hotel_staff_only, translators_only
from rekruter.models import User, QuarterClass
from rekruter.forms import IniForm


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


def showmydata(request):
    ru = request.user
    userdata = User.objects.get(
     id=ru.id, email=ru.email,
     first_name=ru.first_name,
     last_name=ru.last_name,
     quarter=ru.quarter)
    if request.method == 'POST':
        uid = User.objects.get(id=ru.id)
        form = IniForm(request.POST, instance=uid)
        if form.is_valid():
            form.save()
            return redirect('userdatapersonal')
    else:
        form = IniForm()
        quarter = userdata.__dict__['quarter']
        locations = list(QuarterClass.objects.all())
        quarters = locations[0]
        quartzlist = [
         'stud_local', 'stud_foreign', 'phd', 'bank',
         'new1', 'new23', 'new_foreign', 'erasmus', 'bilateral',
        ]  # To nie powinno być na stałe w kodzie ale jako zmienna z admina.
        setter = quarters.__getattribute__(quartzlist[int(quarter)-1])
        setlist = []
        for item in quartzlist:
            setlist.append(quarters.__getattribute__(item))
        context = {
         'value': 2,
         'form': form,
         'setter': setter,
         'setlist': setlist,
         'udata': userdata,
         }
        # zdefiniuj dodatkowe konteksty tutaj.
        pl = PortalLoad(P, L, Pbi, 0, Umi, Uli, )
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'panels/user/mydata.html'
        return render(request, template, context_lazy)
