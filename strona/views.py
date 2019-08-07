from django.shortcuts import render
from django.shortcuts import get_object_or_404 as G404
from .models import Blog as B
from .models import Info as In
from .models import Fileserve as F
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import Blog, Info, File

bl = Blog(P, L)
inf = Info()
fil = File()


def home(request):
    bl.gen(B=B)
    inf.gen(In=In)
    fil.gen(F=F)
    context = {
     'items': bl.items,
     'langs': bl.langs,
     'blogs': bl.blogs,
     'infos': inf.infos,
     'files': fil.files, }
    return render(request, 'strona/home.html', context)


def blog(request, blog_id):
    bl.gen(B=B, G404=G404, blogid=blog_id)
    inf.gen(In=In)
    fil.gen(F=F)
    context = {
     'items': bl.items,
     'langs': bl.langs,
     'blog': bl.blog,
     'infos': inf.infos,
     'files': fil.files, }
    return render(request, 'strona/blog.html', context)


def info(request, info_id):
    bl.gen(B=B)
    inf.gen(In=In, G404=G404, infoid=info_id)
    fil.gen(F=F)
    context = {
     'items': bl.items,
     'langs': bl.langs,
     'blogs': bl.blogs,
     'info': inf.info,
     'infos': inf.infos,
     'files': fil.files, }
    return render(request, 'strona/info.html', context)
