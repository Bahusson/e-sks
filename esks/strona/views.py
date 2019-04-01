from django.shortcuts import render, get_object_or_404

from .models import Pageitem
from .models import Blog


def home(request, pageitem_id):
    blogs = Blog.objects
    item = get_object_or_404(Blog, pk=pageitem_id)
    return render(request, 'home.html', {'item': item, 'blogs': blogs})
