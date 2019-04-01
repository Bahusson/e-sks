from modeltranslation.translator import translator, TranslationOptions
from rekruter.models import Sito

class SitoTranslate(TranslationOptions):
    fields = ('intro', 'oswiadczenie', 'obywatelstwo', 'student', 'doktorant', 'zamiar', 'zadnezpow', 'pelnywym', 'erasmus', 'bilateral', 'buttondalej')

translator.register(Sito, SitoTranslate)

#class ZapisTranslate(TranslationOptions):
#    fields = ('?', '?')

#translator.register(Zapis, ZapisTranslate)
