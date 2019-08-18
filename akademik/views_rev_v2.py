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
    #zdefiniuj dodatkowe konteksty tutaj.
    ps = PageSkinner(
    	P, L, skins=S, choice=0)
    template = 'panel_rady.html'
    return render(request, template, ps.context)

    

# Panel Obsługi Akademików
@staff_member_required(login_url='logger')
def staffpanel_h(request):
    #zdefiniuj dodatkowe konteksty tutaj.
    ps = PageSkinner(
    	P, L, skins=S, choice=0)
    template = 'panel_akademika.html'
    return render(request, template, ps.context)

# Panel użytkownika.
# Jeśli nie masz jeszcze przydzielonej kwatery,
# przekieruje Cię najpierw do przydziału.
def userpanel(request):
    quarter = request.user.quarter
    if quarter == '':
        return redirect('initial')
    else:
        #zdefiniuj dodatkowe konteksty tutaj.
        ps = PageSkinner(
         P, L, skins=S, choice=0)
   template = 'panel_uzytkownika.html'     
   return render(request, template, ps.context)
        	

def showmydata(request):
    with request.user as ru:   
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
        #zdefiniuj dodatkowe konteksty tutaj.
        ps = PageSkinner(
         	P, L, skins=S, choice=0, context=context)      
        template = 'akademik/panel/user/mydata.html'     
        return render(request, template, ps.context)
       