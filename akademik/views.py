from django.shortcuts import render, redirect
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib.auth.decorators import user_passes_test
# from rekruter.models import User


# Panel obsługi.
@staff_member_required(login_url='logger')
def staffpanel(request):
    pl = PageLoad(P, L)
    context = {
     'items': pl.items,
     'langs': pl.langs, }
    return render(request, 'akademik/panel/staff.html', context)


# Panel użytkownika.
# Jeśli nie masz jeszcze przydzielonej kwatery przekieruje Cię do przydziału.
def userpanel(request):
    quarter = request.user.quarter
    if quarter == '':
        return redirect('initial')
    else:
        pl = PageLoad(P, L)
        context = {
         'items': pl.items,
         'langs': pl.langs, }
        return render(request, 'akademik/panel/user.html', context)
