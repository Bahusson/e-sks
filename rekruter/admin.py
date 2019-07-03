from django.contrib import admin

# Register your models here.
from .models import Sito
from .models import FormItems
from .models import QuarterClass

admin.site.register(Sito)
admin.site.register(FormItems)
admin.site.register(QuarterClass)
