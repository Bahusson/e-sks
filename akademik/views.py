from django.shortcuts import render, redirect
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad
from django.contrib.admin.views.decorators import staff_member_required
from rekruter.models import User, QuarterClass


# Panel Rady
@staff_member_required(login_url='logger')
def staffpanel_c(request):
    pl = PageLoad(P, L)
    context = {
     'items': pl.items,
     'langs': pl.langs, }
    template = 'panel_rady.html'
    return render(request, template, context)


# Panel Obsługi Akademików
@staff_member_required(login_url='logger')
def staffpanel_h(request):
    pl = PageLoad(P, L)
    context = {
     'items': pl.items,
     'langs': pl.langs, }
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
        pl = PageLoad(P, L)
        context = {
         'items': pl.items,
         'langs': pl.langs, }
        template = 'panel_uzytkownika.html'
        return render(request, template, context)


def showmydata(request):
    userdata = User.objects.get(
     id=request.user.id, email=request.user.email,
     first_name=request.user.first_name, last_name=request.user.last_name,
     quarter=request.user.quarter)
    print(userdata.__dict__['id'])
    if request.method == 'POST':
        pass
    else:
        pl = PageLoad(P, L)
        quarter = userdata.__dict__['quarter']
        print("wartość kwatery to:" + str(quarter))
        locations = list(QuarterClass.objects.all())
        quarters = locations[0]
        quartzlist = [
         'stud_local', 'stud_foreign', 'phd', 'bank',
         'new1', 'new23', 'new_foreign', 'erasmus', 'bilateral',
        ]  # To nie powinno być na stałe w kodzie ale jako zmienna z admina.
        setter = quarters.__getattribute__(quartzlist[int(quarter)-1])
        print(setter)
        context = {
         'setter': setter,
         'udata': userdata,
         'items': pl.items,
         'langs': pl.langs, }
        template = 'akademik/panel/user/mydata.html'
        return render(request, template, context)
