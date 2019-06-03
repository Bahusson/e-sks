from django.shortcuts import render
from django.shortcuts import get_object_or_404 as G404
from django.utils import translation
from .models import Blog as B
from .models import Info as I
from .models import Fileserve as F
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import Langmenu, PageLoad


def login(request):
    return render(request, 'login.html')

def home(request):
    pl = PageLoad(P,L,F,I,B,G404,info_id=None,blog_id=None)
    return render(request, 'home.html', {'items': pl.items, 'langs': pl.langs, 'blogs': pl.blogs, 'infos': pl.infos, 'files': pl.files})

def blog(request, blog_id):
    pl = PageLoad(P,L,F,I,B,G404,None,blog_id)
    return render(request, 'blog.html', {'items': pl.items, 'langs': pl.langs, 'blog': pl.blog, 'infos': pl.infos, 'files': pl.files})

def info(request, info_id):
    pl = PageLoad(P,L,F,I,B,G404,info_id,None)
    return render(request, 'info.html', {'items': pl.items, 'langs': pl.langs, 'blog': pl.blog, 'info': pl.info, 'infos': pl.infos, 'files': pl.files})
