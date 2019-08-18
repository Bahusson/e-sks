from django.shortcuts import render, redirect
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PageSkinner
from django.contrib.admin.views.decorators import staff_member_required
from rekruter.models import User, QuarterClass


# Panel Rady
@staff_member_required(login_url='logger')
def staffpanel_c(request):
    ps = PageSkinner(P, L)
    ps.gen(skins=S, choice=0)
    context = {
     'items': ps.items,
     'langs': ps.langs,
     'skin': ps.skin, }
    template = 'panel_rady.html'
    return render(request, template, context)


# Panel Obsługi Akademików
@staff_member_required(login_url='logger')
def staffpanel_h(request):
    ps = PageSkinner(P, L)
    ps.gen(skins=S, choice=0)
    context = {
     'items': ps.items,
     'langs': ps.langs,
     'skin': ps.skin, }
    template = 'panel_akademika.html'
    return render(request, template, context)


# Panel użytkownika.
# Jeśli nie masz jeszcze przydzielonej kwatery,
# przekieruje Cię najpierw do przydziału.
def userpanel(request):
    quarter = request.user.quarter
    if quarter == '':
        return redirect('initial')
    else:
        ps = PageSkinner(P, L)
        ps.gen(skins=S, choice=0)
        context = {
         'items': ps.items,
         'langs': ps.langs,
         'skin': ps.skin, }
        template = 'panel_uzytkownika.html'
        return render(request, template, context)


def showmydata(request):
    userdata = User.objects.get(
     id=request.user.id, email=request.user.email,
     first_name=request.user.first_name, last_name=request.user.last_name,
     quarter=request.user.quarter)

    if request.method == 'POST':
        pass
    else:
        ps = PageSkinner(P, L)
        ps.gen(skins=S, choice=0)
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
         
        template = 'akademik/panel/user/mydata.html'
        return render(request, template, context)