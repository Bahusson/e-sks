from django.contrib import admin

# Register your models here.
from .models import PortalBaseItem
from .models import HotelMenuItem, CouncilMenuItem, TranslatorMenuItem, UserMenuItem
from .models import HotelLinkItem, CouncilLinkItem, TranslatorLinkItem, UserLinkItem


admin.site.register(PortalBaseItem)
admin.site.register(HotelMenuItem)
admin.site.register(CouncilMenuItem)
admin.site.register(TranslatorMenuItem)
admin.site.register(UserMenuItem)
admin.site.register(HotelLinkItem)
admin.site.register(CouncilLinkItem)
admin.site.register(TranslatorLinkItem)
admin.site.register(UserLinkItem)
