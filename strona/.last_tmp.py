from django.shortcuts import render
from django.shortcuts import get_object_or_404 as G404
from .models import PageSkin as S
from .models import Blog as B
from .models import Info as In
from .models import Fileserve as F
from strona.models import Pageitem as P
from esks.settings import LANGUAGES as L
from esks.special.classes import Blog, PageSkinner


# Strona główna.
def home(request):
    ps = PageSkinner(P, L)
    bl = Blog()
    inf = Info()
    fil = File()
    ps.gen(skins=S, choice=0)  # Do zmiany po ustawieniu reszty w panelu usera.
    bl.gen(B=B)
    inf.gen(In=In)
    fil.gen(F=F)
    context = {
     'items': ps.items,
     'langs': ps.langs,
     'skin': ps.skin,
     'blogs': bl.bloglist,
     'infos': inf.infos,
     'files': fil.files, }
    template = 'strona/home.html'
    return render(request, template, context)


# Pojedyńcze aktualności w zbliżeniu.
def blog(request, blog_id):
    bl = Blog(P, L)
    inf = Info()
    fil = File()
    bl.gen(B=B, G404=G404, blogid=blog_id)
    inf.gen(In=In)
    fil.gen(F=F)
    context = {
     'items': bl.items,
     'langs': bl.langs,
     'blog': bl.blog,
     'infos': inf.infos,
     'files': fil.files, }
    template = 'strona/blog.html'
    return render(request, template, context)


# Pojedyńcze informacje w zbliżeniu.
def info(request, info_id):
    bl = Blog(P, L)
    inf = Info()
    fil = File()
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
    template = 'strona/info.html'
    return render(request, template, context)