from modeltranslation.translator import translator, TranslationOptions
from rekruter.models import Sito
from rekruter.models import FormItems
from rekruter.models import QuarterClass


class SitoTranslate(TranslationOptions):
    fields = ('intro', 'yes', 'no', 'oswiadczenie', 'obywatelstwo', 'student', 'doktorant', 'zamiar', 'zamiar', 'pierwszegosto', 'pelnywym', 'erasmus', 'buttondalej',)

translator.register(Sito, SitoTranslate)


class FormItemsTranslate(TranslationOptions):
    fields = ('login', 'password', 're_password', 'name', 'surname', 'email', 'register', 'admin_panel', 'back', 'action',)

translator.register(FormItems, FormItemsTranslate)


class QuarterClassTranslate(TranslationOptions):
    fields = ('stud_local', 'stud_foreign', 'phd', 'bank', 'new1', 'new23', 'new_foreign', 'erasmus', 'bilateral',)

translator.register(QuarterClass, QuarterClassTranslate)
