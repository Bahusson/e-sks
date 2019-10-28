from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad, PageElement
from .models import PortalBaseItem as Pbi
from .models import TranslatorMenuItem as Tmi
from .models import TranslatorLinkItem as Tli
from esks.special.decorators import translators_only
from rekruter.models import User, FormItems, QuarterClassB
from rekruter.forms import IniForm, ApplicationForm


# Panel Tłumaczeniowy
@translators_only(login_url='logger')
def translatorpanel(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PortalLoad(P, L, Pbi, 3, Tmi, Tli)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panels/translator/panel_tlumacza.html'
    return render(request, template, context_lazy)

# Pierwszy widok testowy. To się będzie rozrastać. Może zrobimy na klasie?
# Tłumaczenie Pageitem za pomocą importu szeregu zmiennych.
# Tłumaczenie rozwijanych menu będzie za pomocą Formsetów.
@translators_only(login_url='logger')
def elementstranslate(request):
    p_item = PageElement(P)
    p_item_names = p_item.get_attrnames(L, 2)
    print(p_item_names)
    p_item_objects = p_item.get_setlist(0, L, 2)
    print(p_item_objects)
    context = {
     "trans_from_list": p_item_objects,
     "trans_to_list": p_item_names,
    }
    pl = PortalLoad(P, L, Pbi, 3, Tmi, Tli)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = 'panels/translator/elementstranslate.html'
    return render(request, template, context_lazy)
