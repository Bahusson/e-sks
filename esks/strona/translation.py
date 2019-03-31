from modeltranslation.translator import translator, TranslationOptions
from strona.models import Pageitem, Blog

class PageitemsTranslate(TranslationOptions):
    fields = ('lang_flag', 'headtitle', 'mainpage', 'info', 'akamap', 'contact', 'logout', 'news')

translator.register(Pageitem, PageitemsTranslate)

class BlogsTranslate(TranslationOptions):
    fields = ('title', 'body')

translator.register(Blog, BlogsTranslate)
