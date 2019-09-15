from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
from akademik.models import PortalBaseItem as Pbi
from akademik.models import CouncilMenuItem as Cmi
from akademik.models import CouncilLinkItem as Cli
from .models import PageSkin as S
from .models import Blog as B
from .models import Info as In
from .models import Fileserve as F
from rekruter.models import User, FormItems
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageElement as pe
from esks.special.classes import PageLoad, PortalLoad
from esks.special.decorators import council_only
from .models import FormElement
from .forms import BlogForm, InfoForm, FileserveForm


# Tworzy wpis w aktualnościach.
@council_only(login_url='staffpanel_c', power_level=1)
def make_element(request):
    userdata = User.objects.get(
     id=request.user.id)
    
    formdict = {
      'blog': BlogForm,
      'info': InfoForm,
      'file': FileserveForm,
     }
    if request.method == 'POST':
        # form = BlogForm(request.POST)
        form_from_dict = formdict[form_type]
        form = form_from_dict(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(userdata)
            return redirect('staffpanel_c')
    else:
        # form = BlogForm()
        form = formdict[form_type]
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


@council_only(login_url='staffpanel_c', power_level=1)
def make_blog(request):
    userdata = User.objects.get(
     id=request.user.id)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(userdata)
            return redirect('staffpanel_c')
    else:
        form = BlogForm()
        pe_fi = pe(FormItems)
        pe_fe = pe(FormElement)
    pe_fi = pe(FormItems)
    context = {
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


# Pojedyńcze informacje w zbliżeniu.
def make_info(request, info_id):
    pe_i = pe(In)
    pe_b = pe(B)
    pe_i_id = pe_i.by_id(
     G404=G404,
     id=info_id)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.elements,
     'info': pe_i_id,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/manage/makeelement.html'
    return render(request, template, context_lazy)


# Pojedyńcze informacje w zbliżeniu.
def make_file(request, info_id):
    pe_i = pe(In)
    pe_b = pe(B)
    pe_i_id = pe_i.by_id(
     G404=G404,
     id=info_id)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.elements,
     'info': pe_i_id,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/manage/makeelement.html'
    return render(request, template, context_lazy)


# Pojedyńcze aktualności w zbliżeniu.
def change_blog(request, blog_id):
    pe_b = pe(B)
    pe_b_id = pe_b.by_id(
     G404=G404, id=blog_id)
    pe_i = pe(In)
    pe_f = pe(F)
    context = {
     'blog': pe_b_id,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/manage/makeblog.html'
    return render(request, template, context_lazy)


# Pojedyńcze informacje w zbliżeniu.
def change_info(request, info_id):
    pe_i = pe(In)
    pe_b = pe(B)
    pe_i_id = pe_i.by_id(
     G404=G404,
     id=info_id)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.elements,
     'info': pe_i_id,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/manage/makeinfo.html'
    return render(request, template, context_lazy)


# Pojedyńcze informacje w zbliżeniu.
def change_file(request, info_id):
    pe_i = pe(In)
    pe_b = pe(B)
    pe_i_id = pe_i.by_id(
     G404=G404,
     id=info_id)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.elements,
     'info': pe_i_id,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/manage/makefile.html'
    return render(request, template, context_lazy)
