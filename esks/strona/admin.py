from django.contrib import admin

# Register your models here.
from .models import Pageitem, Blog, Info, Fileserve

admin.site.register(Pageitem)

admin.site.register(Blog)

admin.site.register(Info)

admin.site.register(Fileserve)
