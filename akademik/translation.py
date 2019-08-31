from modeltranslation.translator import translator, TranslationOptions
from .models import PortalBaseItem
from .models import HotelMenuItem, CouncilMenuItem, TranslatorMenuItem
from .models import HotelLinkItem, CouncilLinkItem, TranslatorLinkItem
from .models import UserMenuItem, UserLinkItem, HousingParty


# Zmiana kolejności wynika z tego, żeby łatwiej się kopiowało między klasami.
class PortalBaseItemTranslate(TranslationOptions):
    fields = ('title', 'descr')


translator.register(PortalBaseItem, PortalBaseItemTranslate)


class HotelMenuItemTranslate(TranslationOptions):
    fields = ('title', )


translator.register(HotelMenuItem, HotelMenuItemTranslate)


class CouncilMenuItemTranslate(TranslationOptions):
    fields = ('title', )


translator.register(CouncilMenuItem, CouncilMenuItemTranslate)


class TranslatorMenuItemTranslate(TranslationOptions):
    fields = ('title', )


translator.register(TranslatorMenuItem, TranslatorMenuItemTranslate)


class UserMenuItemTranslate(TranslationOptions):
    fields = ('title', )


translator.register(UserMenuItem, UserMenuItemTranslate)


class HotelLinkItemTranslate(TranslationOptions):
    fields = ('title', )


translator.register(HotelLinkItem, HotelLinkItemTranslate)


class CouncilLinkItemTranslate(TranslationOptions):
    fields = ('title', )


translator.register(CouncilLinkItem, CouncilLinkItemTranslate)


class TranslatorLinkItemTranslate(TranslationOptions):
    fields = ('title', )


translator.register(TranslatorLinkItem, TranslatorLinkItemTranslate)


class UserLinkItemTranslate(TranslationOptions):
    fields = ('title', )


translator.register(UserLinkItem, UserLinkItemTranslate)


class HousingPartyTranslate(TranslationOptions):
    fields = ('title', 'comment', 'announcement', )


translator.register(HousingParty, HousingPartyTranslate)
