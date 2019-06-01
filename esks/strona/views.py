from django.shortcuts import render, get_object_or_404
from django.utils import translation

from .models import Pageitem
from .models import Blog
from .models import Info
from .models import Fileserve

def login(request):
    return render(request, 'login.html')

def home(request):
    locations = list(Pageitem.objects.all())
    items = locations[0]
    langs = Pageitem.objects
    blogs = Blog.objects
    infos = Info.objects
    files = Fileserve.objects
    return render(request, 'home.html', {'items': items, 'langs': langs, 'blogs': blogs, 'infos': infos, 'files': files})

def blog(request, blog_id):
    locations = list(Pageitem.objects.all())
    items = locations[0]
    infos = Info.objects
    files = Fileserve.objects
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog.html', {'items': items, 'blog': blog, 'infos': infos, 'files': files})

def info(request, info_id):
    locations = list(Pageitem.objects.all())
    items = locations[0]
    files = Fileserve.objects
    infos = Info.objects
    info = get_object_or_404(Info, pk=info_id)
    return render(request, 'info.html', {'items': items, 'blog': blog, 'info': info, 'infos': infos, 'files': files})
