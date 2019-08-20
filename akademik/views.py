from django.shortcuts import render, redirect
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from esks.special.decorators import council_only, hotel_staff_only, translators_only
# from django.contrib.admin.views.decorators import staff_member_required
from rekruter.models import User, QuarterClass


# Panel Rady
@council_only(login_url='logger')
def staffpanel_c(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panel_rady.html'
    return render(request, template, context_lazy)


# Panel Obsługi Akademików
@hotel_staff_only(login_url='logger')
def staffpanel_h(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panel_akademika.html'
    return render(request, template, context_lazy)


# Panel Tłumaczeniowy
@translators_only(login_url='logger')
def translatorpanel(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panel_tlumacza.html'
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
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S)
    template = 'panel_uzytkownika.html'
    return render(request, template, context_lazy)


def showmydata(request):
    ru = request.user
    userdata = User.objects.get(
     id=ru.id, email=ru.email,
     first_name=ru.first_name,
     last_name=ru.last_name,
     quarter=ru.quarter)

    if request.method == 'POST':
        pass
    else:
        quarter = userdata.__dict__['quarter']
        locations = list(QuarterClass.objects.all())
        quarters = locations[0]
        quartzlist = [
         'stud_local', 'stud_foreign', 'phd', 'bank',
         'new1', 'new23', 'new_foreign', 'erasmus', 'bilateral',
        ]  # To nie powinno być na stałe w kodzie ale jako zmienna z admina.
        setter = quarters.__getattribute__(quartzlist[int(quarter)-1])
        context = {
         'setter': setter,
         'udata': userdata,
         }
        # zdefiniuj dodatkowe konteksty tutaj.
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'panels/user/mydata.html'
        return render(request, template, context_lazy)
