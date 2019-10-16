from modeltranslation.translator import translator, TranslationOptions
from .models import PortalBaseItem, HousingPartyItems
from .models import HotelMenuItem, CouncilMenuItem, TranslatorMenuItem
from .models import HotelLinkItem, CouncilLinkItem, TranslatorLinkItem
from .models import UserMenuItem, UserLinkItem, HousingParty
from .models import ApplicationListItems, UserListItems, AdminTextTools


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


class HousingPartyItemsTranslate(TranslationOptions):
    fields = (
        'party_title', 'choose_party', 'time_start', 'time_end', 'comment',
        'announce', 'tick_form', 'p_from', 'p_to', 'changeme', 'all_parties',
        'active_parties', 'past_parties', 'future_parties', 'new_party_view',
        'owner', 'userinfo', 'housing_party', 'change_and_apply',
    )


translator.register(HousingPartyItems, HousingPartyItemsTranslate)


class ApplicationListItemsTranslate(TranslationOptions):
    fields = ('realname', )


translator.register(ApplicationListItems, ApplicationListItemsTranslate)


class UserListItemsTranslate(TranslationOptions):
    fields = ('realname', )


translator.register(UserListItems, UserListItemsTranslate)


class AdminTextToolsTranslate(TranslationOptions):
    fields = ('sortme', 'ascending', 'descending', )


translator.register(AdminTextTools, AdminTextToolsTranslate)
