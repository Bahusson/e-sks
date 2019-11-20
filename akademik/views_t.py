from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
from django.forms import formset_factory
from strona.models import Pageitem as P
from strona.models import PageSkin as S
from esks.settings import LANGUAGES as L
from esks.special.classes import PortalLoad, PageElement
from .models import PortalBaseItem as Pbi
from .models import TranslatorMenuItem as Tmi
from .models import TranslatorLinkItem as Tli
from esks.special.decorators import translators_only
from rekruter.models import User
from .forms_t import PageItemForm
from .forms_t import TMIListForm
from rekruter.forms import LangForm


# Panel Tłumaczeniowy - pusty.
@translators_only(login_url='logger')
def translatorpanel(request):
    language = request.user.language
    if language == '':
        return redirect('setmylanguage')
    else:
        # zdefiniuj dodatkowe konteksty tutaj.
        pl = PortalLoad(P, L, Pbi, 3, Tmi, Tli)
        context_lazy = pl.lazy_context(skins=S)
    template = 'panels/translator/panel_tlumacza.html'
    return render(request, template, context_lazy)


# Zmiana języka tłumaczeń.
@translators_only(login_url='logger')
def setmylanguage(request):
    userdata = User.objects.get(
     id=request.user.id)
    if 'sendlang' in request.POST:
        form = LangForm(request.POST, instance=userdata)
        userlang = request.POST.get('sendlang')
        if form.is_valid():
            form.save(userlang)
        return redirect('setmylanguage')
    else:
        lang = request.user.language
        userflag = "lang_flag_" + lang
        p_item = PageElement(P)
        p_item_objects = p_item.baseattrs
        preqlist = list(p_item_objects.__dict__.keys())
        # Zmień 'langpos' na 2 jeśli chcesz uniemożliwić tłumaczenie na Angielski.
        # Zmień na 0 jeśli chcesz umożliwić tłumaczenie na Polski (niezalecane).
        langpos = 1
        flagslist = preqlist[langpos+3:len(L)+3]
        lang_tups = L[langpos:]
        lang_ids = []
        for lang_tup in lang_tups:
            lang_ids.append(lang_tup[0])
        context = {
         "userflag": userflag,
         "lang_ids": lang_ids,
         "flagsobjects": p_item_objects,
         "flagslist": flagslist,
        }
        pl = PortalLoad(P, L, Pbi, 3, Tmi, Tli)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'panels/translator/setmylanguage.html'
        return render(request, template, context_lazy)


# Pierwszy widok testowy.
# Tłumaczenie Pageitem za pomocą importu szeregu zmiennych.
@translators_only(login_url='logger')
def elementstranslate(request):
    lang = request.user.language
    instance = P.objects.get(id=1)
    p_item = PageElement(P)
    p_item_names = p_item.get_attrnames(L, 2)
    p_item_names = p_item_names[1:]  # Obcinacz flagi
    p_item_names_lang = []
    for item in p_item_names:
        item = str(item) + "_" + lang
        p_item_names_lang.append(item)
    # print(p_item_names_lang)
    if request.method == 'POST':
        form = PageItemForm(
         request.POST, instance=instance, upd_fields=p_item_names_lang)
        if form.is_valid():
            form.save()
            return redirect('elementstranslate')
    else:
        p_item_objects = p_item.get_setlist(0, L, 2)
        p_item_objects = p_item_objects[1:]  # Obcinacz flagi
        # Dla szerszego spektrum sprawdź wzór na change_element
        form = PageItemForm(instance=instance, upd_fields=p_item_names_lang)
        context = {
         "trans_from_list": p_item_objects,
         "trans_to_list": p_item_names_lang,
         "form": form,
        }
        pl = PortalLoad(P, L, Pbi, 3, Tmi, Tli)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'panels/translator/elementstranslate.html'
        return render(request, template, context_lazy)


# Drugi widok testowy. Tłumaczenie listy rozwijanej.
@translators_only(login_url='logger')
def menustranslate(request):
    lang = request.user.language
    # instance = Tmi.objects.get(id=1)
    p_item = PageElement(Tmi)
    instancelist = p_item.listed
    # print(instancelist)
    p_item_names = p_item.get_attrnames(L, 2)
    p_item_names_lang = []
    for item in p_item_names:
        item = str(item) + "_" + lang
        p_item_names_lang.append(item)
    # Monkey filter (obetnij niepotrzebne elementy):
    p_item_names_lang = p_item_names_lang[0]
    # p_item_names_lang = list(p_item_names_lang)
    print(p_item_names_lang)
    if request.method == 'POST':
        num = 1
        for instance in instancelist:
            print(instance, p_item_names_lang)
            form = TMIListForm(
             request.POST, instance=instance, upd_fields=p_item_names_lang)
            # print(form)
            if form.is_valid():
                print('form is valid')
                form.save()
                num += 1
            else:
                print('form is invalid')
        return redirect('menustranslate')
    else:
        p_item_objects = p_item.get_droplist(L, 2)
        print(p_item_objects)
        forms = []
        for instance in instancelist:
            form = TMIListForm(instance=instance, upd_fields=p_item_names_lang)
            forms.append(form)
        context = {
         "trans_from_list": p_item_objects,
         "trans_to_list": p_item_names_lang,
         "forms": forms,
        }
        pl = PortalLoad(P, L, Pbi, 3, Tmi, Tli)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'panels/translator/menustranslate.html'
        return render(request, template, context_lazy)
