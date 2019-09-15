from django.shortcuts import render
from django.shortcuts import get_object_or_404 as G404
from .models import PageSkin as S
from .models import Blog as B
from .models import Info as In
from .models import Fileserve as F
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageElement as pe
from esks.special.classes import PageLoad


# Strona główna.
def home(request):
    pe_b = pe(B)
    pe_i = pe(In)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.listed,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/home.html'
    return render(request, template, context_lazy)


# Pojedyńcze aktualności w zbliżeniu.
def blog(request, blog_id):
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
    template = 'strona/blog.html'
    return render(request, template, context_lazy)


# Pojedyńcze informacje w zbliżeniu.
def info(request, info_id):
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
    template = 'strona/info.html'
    return render(request, template, context_lazy)


# Wszystkie aktualności.
def allblogs(request):
    pe_b = pe(B)
    pe_i = pe(In)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.elements,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/allblogs.html'
    return render(request, template, context_lazy)


# Wszystkie informacje.
def allinfos(request):
    pe_i = pe(In)
    pe_b = pe(B)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.elements,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/allinfos.html'
    return render(request, template, context_lazy)


# Wszystkie pliki.
def allfiles(request):
    pe_i = pe(In)
    pe_b = pe(B)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.elements,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/allfiles.html'
    return render(request, template, context_lazy)


# Wszystkie pliki.
def pagemap(request):
    if request.method == POST:
        p = request.POST.get('element_sent')
        request.session['make_element'] = p
    else:
        pe_i = pe(In)
        pe_b = pe(B)
        pe_f = pe(F)
        context = {
         'blogs': pe_b.elements,
         'infos': pe_i.elements,
         'files': pe_f.elements, }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(
         skins=S, context=context)
        template = 'strona/pagemap.html'
        return render(request, template, context_lazy)
