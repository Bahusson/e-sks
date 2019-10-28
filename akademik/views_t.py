from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad, PageElement, PartyMaster
from esks.special.classes import AllParties
from .models import PortalBaseItem as Pbi
from .models import UserMenuItem as Umi
from .models import UserLinkItem as Uli
from .models import TranslatorMenuItem as Tmi
from .models import TranslatorLinkItem as Tli
from .models import HotelMenuItem as Hmi
from .models import HotelLinkItem as Hli
from .models import HousingParty as HParty
from .models import HousingPartyItems as Hpi
from rekruter.models import StudentHouse as Sh
from rekruter.models import IfRoomChange as Ifr
from rekruter.models import TimePeriod as Tper
from rekruter.models import StudyFaculty as Stf
from rekruter.models import StudyDegree as Std
from rekruter.models import SpouseCohabitant as Sch
from rekruter.models import SpecialCase as Scs
from esks.special.decorators import hotel_staff_only, translators_only, user_only
from rekruter.models import User, FormItems, QuarterClassB
from rekruter.forms import IniForm, ApplicationForm
import datetime
import pytz


# Panel Tłumaczeniowy
@translators_only(login_url='logger')
def elementstranslate(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PortalLoad(P, L, Pbi, 3, Tmi, Tli)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panels/translator/panel_tlumacza.html'
    return render(request, template, context_lazy)
