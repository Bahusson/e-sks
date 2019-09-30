from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as G404
from rekruter.models import User
from .models import PageSkin as S
from .models import Blog as B
from .models import Info as In
from .models import Fileserve as F
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageElement as pe
from esks.special.classes import PageLoad, ActivePageItems
import pytz
import datetime


# Strona główna.
def home(request):
    api = ActivePageItems(request, B, pytz, datetime)
    active_blogs = api.active_items
    api = ActivePageItems(request, In, pytz, datetime)
    active_infos = api.active_items
    api = ActivePageItems(request, F, pytz, datetime)
    active_files = api.active_items
    context = {
     'blogs': active_blogs,
     'infos': active_infos,
     'files': active_files, }
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
    # pe_b = pe(B)
    api = ActivePageItems(request, B, pytz, datetime)
    active_blogs = api.active_items
    context = {
     'blogs': active_blogs, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/allblogs.html'
    return render(request, template, context_lazy)


# Wszystkie informacje.
def allinfos(request):
    # pe_i = pe(In)
    api = ActivePageItems(request, In, pytz, datetime)
    active_infos = api.active_items
    context = {
     'infos': active_infos, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/allinfos.html'
    return render(request, template, context_lazy)


# Wszystkie pliki.
def allfiles(request):
    # pe_f = pe(F)
    api = ActivePageItems(request, F, pytz, datetime)
    active_files = api.active_items
    context = {
     'files': active_files, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/allfiles.html'
    return render(request, template, context_lazy)


# Mapa strony. I wyjście na edycję elementów dla rady.
def pagemap(request):
    pe_i = pe(In)
    pe_b = pe(B)
    pe_f = pe(F)
    api = ActivePageItems(request, B, pytz, datetime)
    active_blogs = api.active_items
    api = ActivePageItems(request, In, pytz, datetime)
    active_infos = api.active_items
    api = ActivePageItems(request, F, pytz, datetime)
    active_files = api.active_items
    if request.user.is_authenticated:
        userlevel = request.user.role_council
        if userlevel > 0:
            active_blogs = pe_b.listed
            active_infos = pe_i.listed
            active_files = pe_f.listed
    context = {
     'blogs': active_blogs,
     'infos': active_infos,
     'files': active_files, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/pagemap.html'
    return render(request, template, context_lazy)
