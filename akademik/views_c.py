# Widoki Rady Studentów
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad, PageElement, PartyMaster
from .models import PortalBaseItem as Pbi
from .models import CouncilMenuItem as Cmi
from .models import CouncilLinkItem as Cli
from .models import HousingParty as HParty
from .models import HousingPartyItems as Hpi
from rekruter.models import StudentHouse as Sh
from rekruter.models import IfRoomChange as Ifr
from rekruter.models import TimePeriod as Tper
from rekruter.models import StudyFaculty as Stf
from rekruter.models import StudyDegree as Std
from rekruter.models import SpouseCohabitant as Sch
from rekruter.models import SpecialCase as Scs
from esks.special.decorators import council_only
from rekruter.models import User, FormItems, QuarterClassB
from rekruter.forms import PartyForm
import datetime
import pytz


# Panel Rady
@council_only(login_url='logger')
def staffpanel_c(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panels/council/panel_rady.html'
    return render(request, template, context_lazy)


# Tworzy nową akcję kwaterunkową wraz z formularzem z poziomu przew. rady.
@council_only(login_url='staffpanel_c', power_level=2)  # Tylko Przewodniczący
def makemeparty(request, party_id):
    userdata = User.objects.get(
     id=request.user.id)
    if request.method == 'POST':
        form = PartyForm(request.POST)
        if form.is_valid():
            form.save(userdata)
            return redirect('staffpanel_c')
    else:
        pe_fi = PageElement(FormItems)
        form = PartyForm()
        sh = PageElement(Sh)
        ifr = PageElement(Ifr)
        tper = PageElement(Tper)
        stf = PageElement(Stf)
        std = PageElement(Std)
        sch = PageElement(Sch)
        scs = PageElement(Scs)
        peqc = PageElement(QuarterClassB)
        hpi = PageElement(Hpi)
        context = {
         'udata': userdata,
         'formitem': pe_fi.baseattrs,
         'form2': form,
         'houselist': sh.listed,
         'staylist': ifr.listed,
         'periodlist': tper.listed,
         'facultylist': stf.listed,
         'degreelist': std.listed,
         'spouselist': sch.listed,
         'scaselist': scs.listed,
         'setlist': peqc.listed,
         'p_item': hpi.baseattrs
         }
        pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'forms/partymaker.html'
        return render(request, template, context_lazy)


# Na razie pokazuje tylko akcje aktywne.
# Do zmiany, żeby był wybór.
@council_only(login_url='logger')
def allparties(request, view_filter="2"):
    pm = PartyMaster(HParty, pytz, datetime)
    all_parties = pm.all_parties
    range = {
     "1": pm.full_party(attrname="id"),
     "2": pm.active_party(attrname="id"),
     "3": pm.past_party(attrname="id"),
     "4": pm.future_party(attrname="id"),
    }
    if request.method == 'POST':
        view_filter = str(request.POST.get('view_filter'))
    active_parties = []
    for item in range[view_filter]:
        obj = all_parties.elements.get(pk=item)
        active_parties.append(obj)
    pe_fi = PageElement(FormItems)
    all_parties = PageElement(HParty)
    hpi = PageElement(Hpi)
    peqc = PageElement(QuarterClassB)
    context = {
     'formitem': pe_fi.baseattrs,
     'parties': active_parties,
     'p_item': hpi.baseattrs,
     'setter': peqc.listed,
     'view_filter': view_filter,
     }
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = 'panels/council/allparties.html'
    return render(request, template, context_lazy)
