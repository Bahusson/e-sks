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
    blogs = Blog.objects
    infos = Info.objects
    files = Fileserve.objects
    return render(request, 'home.html', {'items': items, 'blogs': blogs, 'infos': infos, 'files': files})

def blog(request, blogs_id):
    blogs = get_object_or_404(Info, pk=blogs_id)
    return render(request, 'blog.html', {'blogs':blogs})

def info(request, infos_id):
    infos = get_object_or_404(Info, pk=infos_id)
    return render(request, 'info.html', {'infos':infos})
