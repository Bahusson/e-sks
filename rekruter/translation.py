from modeltranslation.translator import translator, TranslationOptions
from rekruter.models import Sito, FormItems, QuarterClassB, StudentHouse
from rekruter.models import IfRoomChange, TimePeriod, StudyFaculty
from rekruter.models import StudyDegree, SpouseCohabitant, SpecialCase
from rekruter.models import ApplicationStatus


class SitoTranslate(TranslationOptions):
    fields = (
     'intro', 'yes', 'no', 'oswiadczenie', 'obywatelstwo', 'student',
     'doktorant', 'zamiar', 'zamiar', 'pierwszegosto', 'pelnywym', 'erasmus',
     'buttondalej',)


translator.register(Sito, SitoTranslate)


class FormItemsTranslate(TranslationOptions):
    fields = (
     'login', 'password', 're_password', 'name', 'surname', 'email',
     'register', 'admin_panel', 'back', 'action', 'assigned_to',
     'data_correct', 'assign_again', 'list_select', 'personal_data',
     'citizenship', 'passport', 'dowod', 'gender', 'warning_f',
     'tel_mandatory', 'defaul_t', 'telephone', 'preferences', 'match_prefs',
     'see_map', 'choose', 'i_ask', 'time_in_sh', 'adress_data', 'street',
     'building_no', 'local_no', 'postcode', 'city', 'click_map', 'search',
     'check_search', 'check_mandatory', 'search_failed', 'pref_as_stud',
     'faculty', 'degree', 'deangroup', 'album', 'semester', 'additional_info',
     'spouse_cohabitant', 'special_case_docs', 'statement', 'agree',
     'disagree', 'mail_join', 'data_processing', 'appendix', 'sendme', 'ufile',
     'browse', 'appendix_name', 'del_file', 'down_file', 'nofile_chosen',
     'nought', 'male', 'female', 'other', 'app_for_sh', 'app_no', 'state',
     'number', 'created', 'spouseID', 'stays', 'show_by', 'results', 'total',
     'agree_international', )


translator.register(FormItems, FormItemsTranslate)


class StudentHouseTranslate(TranslationOptions):
    fields = ('name', )


translator.register(StudentHouse, StudentHouseTranslate)


class IfRoomChangeTranslate(TranslationOptions):
    fields = ('name', )


translator.register(IfRoomChange, IfRoomChangeTranslate)


class TimePeriodTranslate(TranslationOptions):
    fields = ('name', )


translator.register(TimePeriod, TimePeriodTranslate)


class StudyFacultyTranslate(TranslationOptions):
    fields = ('name', )


translator.register(StudyFaculty, StudyFacultyTranslate)


class StudyDegreeTranslate(TranslationOptions):
    fields = ('name', )


translator.register(StudyDegree, StudyDegreeTranslate)


class SpouseCohabitantTranslate(TranslationOptions):
    fields = ('name', )


translator.register(SpouseCohabitant, SpouseCohabitantTranslate)


class SpecialCaseTranslate(TranslationOptions):
    fields = ('name', )


translator.register(SpecialCase, SpecialCaseTranslate)


class ApplicationStatusTranslate(TranslationOptions):
    fields = ('name', )


translator.register(ApplicationStatus, ApplicationStatusTranslate)


class QuarterClassBTranslate(TranslationOptions):
    fields = ('name', )


translator.register(QuarterClassB, QuarterClassBTranslate)
