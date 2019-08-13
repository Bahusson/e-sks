from modeltranslation.translator import translator, TranslationOptions
from strona.models import Pageitem, Blog, Info, Fileserve


class PageitemsTranslate(TranslationOptions):
    fields = (
     'lang_flag', 'headtitle', 'mainpage', 'information', 'akamap', 'contact',
     'logout', 'news', 'docs', 'login', 'panel_user', 'panel_staff')


translator.register(Pageitem, PageitemsTranslate)


class BlogsTranslate(TranslationOptions):
    fields = ('title', 'body')


translator.register(Blog, BlogsTranslate)


class InfosTranslate(TranslationOptions):
    fields = ('title', 'body', 'image')


translator.register(Info, InfosTranslate)


class FileserveTranslate(TranslationOptions):
    fields = ('title', 'body')


translator.register(Fileserve, FileserveTranslate)
