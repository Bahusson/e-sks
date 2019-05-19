from modeltranslation.translator import translator, TranslationOptions
from rekruter.models import Sito

class SitoTranslate(TranslationOptions):
    fields = ('intro', 'yes', 'no', 'oswiadczenie', 'obywatelstwo', 'student', 'doktorant', 'zamiar', 'zamiar', 'pierwszegosto', 'pelnywym', 'erasmus', 'buttondalej')

translator.register(Sito, SitoTranslate)

#class ZapisTranslate(TranslationOptions):
#    fields = ('?', '?')

#translator.register(Zapis, ZapisTranslate)
