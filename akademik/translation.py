from modeltranslation.translator import translator, TranslationOptions
from .models import HotelBaseItem, CouncilBaseItem, TranslatorBaseItem, UserBaseItem
from .models import HotelMenuItem, CouncilMenuItem, TranslatorMenuItem, UserMenuItem
from .models import HotelLinkItem, CouncilLinkItem, TranslatorLinkItem, UserLinkItem


class HotelBaseItemTranslate(TranslationOptions):
    fields = ('title', 'descr')


translator.register(HotelBaseItem, HotelBaseItemTranslate)


class CouncilBaseItemTranslate(TranslationOptions):
    fields = ('title', 'descr')


translator.register(CouncilBaseItem, CouncilBaseItemTranslate)


class TranslatorBaseItemTranslate(TranslationOptions):
    fields = ('title', 'descr')


translator.register(TranslatorBaseItem, TranslatorBaseItemTranslate)


class UserBaseItemTranslate(TranslationOptions):
    fields = ('title', 'descr')


translator.register(UserBaseItem, UserBaseItemTranslate)


class HotelMenuItemTranslate(TranslationOptions):
    fields = ('title', 'position')


translator.register(HotelMenuItem, HotelMenuItemTranslate)


class CouncilMenuItemTranslate(TranslationOptions):
    fields = ('title', 'position')


translator.register(CouncilMenuItem, CouncilMenuItemTranslate)


class TranslatorMenuItemTranslate(TranslationOptions):
    fields = ('title', 'position')


translator.register(TranslatorMenuItem, TranslatorMenuItemTranslate)


class UserMenuItemTranslate(TranslationOptions):
    fields = ('title', 'position')


translator.register(UserMenuItem, UserMenuItemTranslate)


class HotelLinkItemTranslate(TranslationOptions):
    fields = ('title', 'position')


translator.register(HotelLinkItem, HotelLinkItemTranslate)


class CouncilLinkItemTranslate(TranslationOptions):
    fields = ('title', 'position')


translator.register(CouncilLinkItem, CouncilLinkItemTranslate)


class TranslatorLinkItemTranslate(TranslationOptions):
    fields = ('title', 'position')


translator.register(TranslatorLinkItem, TranslatorLinkItemTranslate)


class UserLinkItemTranslate(TranslationOptions):
    fields = ('title', 'position')


translator.register(UserLinkItem, UserLinkItemTranslate)
