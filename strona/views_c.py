from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
from akademik.models import PortalBaseItem as Pbi
from akademik.models import CouncilMenuItem as Cmi
from akademik.models import CouncilLinkItem as Cli
from .models import PageSkin as S
from .models import Blog, Info, Fileserve
from rekruter.models import User, FormItems
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageElement as pe
from esks.special.classes import PortalLoad
from esks.special.classes import ActivePageItems
from esks.special.decorators import council_only
from .models import FormElement
from .forms import BlogForm, InfoForm, FileserveForm
import pytz
import datetime

# Tworzy wpis w aktualnościach.
@council_only(login_url='staffpanel_c', power_level=1)
def make_element(request, form_type):
    userdata = User.objects.get(
     id=request.user.id)
    create = True
    formdict = {
      'blog': BlogForm,
      'info': InfoForm,
      'file': FileserveForm,
     }
    if request.method == 'POST':
        form_from_dict = formdict[form_type]
        form = form_from_dict(request.POST, request.FILES)
        if form.is_valid():
            form.save(userdata)
            return redirect('staffpanel_c')
    else:
        form = formdict[form_type]
        pe_fi = pe(FormItems)
        pe_fe = pe(FormElement)
    pe_fi = pe(FormItems)
    context = {
     'creator_form': create,
     'diff': form_type,
     'udata': userdata,
     'form': form,
     'formitem': pe_fi.baseattrs,
     'f_item': pe_fe.baseattrs,
     }
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/manage/makeelement.html'
    return render(request, template, context_lazy)


# Backup tworzenia za pomocą sesji. Do usunięcia przy updacie.
@council_only(login_url='staffpanel_c', power_level=1)
def change_element(request, form_type, form_id):
    userdata = User.objects.get(
     id=request.user.id)
    # form_type = request.session['element_type']
    # form_id = int(request.session['element_id'])
    formdict = {
      'blog': BlogForm,
      'info': InfoForm,
      'file': FileserveForm,
     }
    elemdict = {
       'blog': Blog,
       'info': Info,
       'file': Fileserve,
     }
    form_from_dict = formdict[form_type]
    element = elemdict[form_type]
    if request.method == 'POST':
        # form_from_dict = formdict[form_type]
        form = form_from_dict(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(userdata)
            return redirect('staffpanel_c')
    else:
        instance = G404(element, id=form_id)
        # form = formdict[form_type]
        form = form_from_dict(instance=instance)
        pe_fi = pe(FormItems)
        pe_fe = pe(FormElement)
    pe_fi = pe(FormItems)
    context = {
     'diff': form_type,
     'udata': userdata,
     'form': form,
     'formitem': pe_fi.baseattrs,
     'f_item': pe_fe.baseattrs,
     }
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/manage/makeelement.html'
    return render(request, template, context_lazy)


# Pozwala członkom rady zmieniać i edytować elementy strony danego typu.
@council_only(login_url='logger')
def allelements(request, elem_type):
    elemdict = {
       'blog': Blog,
       'info': Info,
       'file': Fileserve,
     }
    element = elemdict[elem_type]
    api = ActivePageItems(request, element, pytz, datetime)
    active_elements = api.active_items
    addvariable = 'add' + elem_type
    context = {
     'addvar': addvariable,
     'element_type': elem_type,
     'elements': active_elements, }
    pl = PortalLoad(P, L, Pbi, 1, Cmi, Cli, )
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/manage/allelements.html'
    return render(request, template, context_lazy)
