from django.shortcuts import render
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib.auth.decorators import user_passes_test
# from esks.special.decorators import user_has_quarters


# Panel obsługi.
@staff_member_required(login_url='logger')
def staffpanel(request):
    pl = PageLoad(P, L)
    context = {
     'items': pl.items,
     'langs': pl.langs, }
    return render(request, 'akademik/panel/staff.html', context)


# Panel użytkownika.
# @user_passes_test(lambda u: u.is_authenticated, login_url='initial')
# @user_has_quarters(login_url='initial')
def userpanel(request):
    pl = PageLoad(P, L)
    context = {
     'items': pl.items,
     'langs': pl.langs, }
    return render(request, 'akademik/panel/user.html', context)
