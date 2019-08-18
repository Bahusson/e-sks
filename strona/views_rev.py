from django.shortcuts import render
from django.shortcuts import get_object_or_404 as G404
from .models import PageSkin as S
from .models import Blog as B
from .models import Info as In
from .models import Fileserve as F
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageElement, PageElememtById, PageSkinner


# Strona główna.
def home(request):
    pe = PageElement()
    pe_b = pe(B)
    pe_i = pe(In)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.listed,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    ps = PageSkinner(
    	P, L, skins=S,
    	choice=0, context=context)
    template = 'strona/home.html'
    return render(request, template, ps.context)


# Pojedyńcze aktualności w zbliżeniu.
def blog(request, blog_id):
    pe = PageElement()
    pe_b = pe(
    	B, G404=G404,
    	id=blog_id)
    pe_i = pe(In)
    pe_f = pe(F)
    context = {
     'blog': pe_b.by_id,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    ps = PageSkinner(
    	P, L, skins=S,
    	choice=0, context=context)
    template = 'strona/blog.html'
    return render(request, template, ps.context)


# Pojedyńcze informacje w zbliżeniu.
def info(request, info_id):
    pe = PageElement()
    pi = PageElementById()
    pe_b = pe(B)
    pe_i = pi(
    	In, G404=G404,
    	id=info_id)
    pe_f = pe(F)
    context = {
     'blogs': pe_b.elements,
     'info': pe_i.by_id,
     'infos': pe_i.elements,
     'files': pe_f.elements, }
    ps = PageSkinner(
    	P, L, skins=S,
    	choice=0, context=context)
    template = 'strona/info.html'
    return render(request, template, ps.context)
