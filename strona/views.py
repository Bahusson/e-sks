from django.shortcuts import render
from django.shortcuts import get_object_or_404 as G404
#from django.utils import translation
from .models import Blog as B
from .models import Info as I
from .models import Fileserve as F
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import PageLoad


def home(request):
    pl = PageLoad(P, L)
    pl.portal(F, I, B, G404)
    context = {
     'items': pl.items,
     'langs': pl.langs,
     'blogs': pl.blogs,
     'infos': pl.infos,
     'files': pl.files}
    return render(request, 'strona/home.html', context)


def blog(request, blog_id):
    pl = PageLoad(P, L)
    pl.portal(F, I, B, G404, blogid=blog_id)
    context = {
     'items': pl.items,
     'langs': pl.langs,
     'blog': pl.blog,
     'infos': pl.infos,
     'files': pl.files}
    return render(request, 'strona/blog.html', context)


def info(request, info_id):
    pl = PageLoad(P, L)
    pl.portal(F, I, B, G404, infoid=info_id)
    context = {
     'items': pl.items,
     'langs': pl.langs,
     'blogs': pl.blogs,
     'info': pl.info,
     'infos': pl.infos,
     'files': pl.files}
    return render(request, 'strona/info.html', context)
