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


# Pojedyńcze aktualności w zbliżeniu.
def make_blog(request, blog_id):
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
    template = 'strona/manage/makeinfo.html'
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
    template = 'strona/manage/makefile.html'
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
