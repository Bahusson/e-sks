from modeltranslation.translator import translator, TranslationOptions
from strona.models import Pageitem, Blog, Info, Fileserve, FormElement


class PageitemsTranslate(TranslationOptions):
    fields = (
     'lang_flag', 'headtitle', 'mainpage', 'information', 'akamap', 'contact',
     'logout', 'news', 'docs', 'login', 'panel_user', 'panel_council',
     'panel_staff', 'panel_translator', 'backtouserpanel', 'see_more',
     'pagemap', 'addblog', 'addinfo', 'addfile', 'editme',)


translator.register(Pageitem, PageitemsTranslate)


class BlogsTranslate(TranslationOptions):
    fields = ('title', 'body', 'image', 'video')


translator.register(Blog, BlogsTranslate)


class InfosTranslate(TranslationOptions):
    fields = ('title', 'body', 'image')


translator.register(Info, InfosTranslate)


class FileserveTranslate(TranslationOptions):
    fields = ('title', 'body', 'file')


translator.register(Fileserve, FileserveTranslate)


class FormElementTranslate(TranslationOptions):
    fields = (
     'title', 'pubdate', 'body', 'image', 'video', 'lastmod', 'by', 'blog',
     'info', 'file', 'new', 'change'
     )


translator.register(FormElement, FormElementTranslate)
