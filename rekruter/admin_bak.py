from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.
from .models import Sito
from .models import FormItems
from .models import QuarterClass
from .models import Profile


# Do wywalenia jeśli rozszerzenie AbstractBaseUser zadziała
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


# Do wywalenia jeśli rozszerzenie AbstractBaseUser zadziała
class CustomUserAdmin1(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(Sito)
admin.site.register(FormItems)
admin.site.register(QuarterClass)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin1)
