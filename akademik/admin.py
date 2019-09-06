from django.contrib import admin

# Register your models here.
from .models import PortalBaseItem
from .models import HotelMenuItem, CouncilMenuItem, TranslatorMenuItem
from .models import HotelLinkItem, CouncilLinkItem, TranslatorLinkItem
from .models import UserMenuItem, UserLinkItem, HousingParty
from .models import HousingPartyItems


admin.site.register(PortalBaseItem)
admin.site.register(HotelMenuItem)
admin.site.register(CouncilMenuItem)
admin.site.register(TranslatorMenuItem)
admin.site.register(UserMenuItem)
admin.site.register(HotelLinkItem)
admin.site.register(CouncilLinkItem)
admin.site.register(TranslatorLinkItem)
admin.site.register(UserLinkItem)
admin.site.register(HousingParty)
admin.site.register(HousingPartyItems)
