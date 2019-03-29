from django.shortcuts import render, get_object_or_404

from .models import Pageitem
from .models import Blog

# Create your views here.
def home(request, pageitem_id):
    blogs = Blog.objects
    item = get_object_or_404(Job, pk=pageitem_id)
    return render(request, 'home.html', {'item':item , 'blogs':blogs})
