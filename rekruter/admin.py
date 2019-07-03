from django.contrib import admin

# Register your models here.
from .models import Sito
from .models import FormItems

admin.site.register(Sito)
admin.site.register(FormItems)
