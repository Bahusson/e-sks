from django.shortcuts import render, get_object_or_404
from django.utils import translation

from .models import Pageitem
from .models import Blog
from .models import Info
from .models import Fileserve
from esks.settings import LANGUAGES

lang_id = []
langsl = []
langslist = []
locations = list(Pageitem.objects.all())
items = locations[0]

for item in LANGUAGES :
    lang_id.append("lang_flag_" + str(item[0]))

x = len(lang_id) -1
y = 0

while x+1 > 0 :
    z = items.__dict__[lang_id[y]]
    langsl.append(z)
    x = x-1
    y = y+1

    langslist = zip(lang_id, langsl)

def login(request):
    return render(request, 'login.html')

def home(request):
    items = locations[0]
    blogs = Blog.objects
    langs = langslist
    infos = Info.objects
    files = Fileserve.objects
    return render(request, 'home.html', {'items': items, 'langs': langs, 'blogs': blogs, 'infos': infos, 'files': files})

def blog(request, blog_id):
    items = locations[0]
    infos = Info.objects
    files = Fileserve.objects
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog.html', {'items': items, 'blog': blog, 'infos': infos, 'files': files})

def info(request, info_id):
    items = locations[0]
    files = Fileserve.objects
    infos = Info.objects
    info = get_object_or_404(Info, pk=info_id)
    return render(request, 'info.html', {'items': items, 'blog': blog, 'info': info, 'infos': infos, 'files': files})
