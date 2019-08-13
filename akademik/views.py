from django.shortcuts import render
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


# Panel obsługi.
@staff_member_required(login_url='logger')
def staffpanel(request):
    pl = PageLoad(P, L)
    context = {
     'items': pl.items,
     'langs': pl.langs, }
    return render(request, 'akademik/panel/staff.html', context)


# Panel użytkownika.
@login_required(login_url='logger')
def userpanel(request):
    pl = PageLoad(P, L)
    context = {
     'items': pl.items,
     'langs': pl.langs, }
    return render(request, 'akademik/panel/user.html', context)
