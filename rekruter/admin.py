from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User


# Register your models here.
from .models import Sito
from .models import FormItems
from .models import QuarterClass
from .User import ExtendedUser


admin.site.register(Sito)
admin.site.register(FormItems)
admin.site.register(QuarterClass)
# admin.site.unregister(User)
admin.site.register(ExtendedUser)
