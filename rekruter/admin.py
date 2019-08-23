from django.contrib import admin


# Register your models here.
from .models import Sito, FormItems, QuarterClass, User, StudentHouse
from .models import IfRoomChange, TimePeriod, StudyFaculty, StudyDegree
from .models import SpouseCohabitant, SpecialCase, ApplicationFormFields


admin.site.register(Sito)
admin.site.register(FormItems)
admin.site.register(QuarterClass)
admin.site.register(User)
admin.site.register(StudentHouse)
admin.site.register(IfRoomChange)
admin.site.register(TimePeriod)
admin.site.register(StudyFaculty)
admin.site.register(StudyDegree)
admin.site.register(SpouseCohabitant)
admin.site.register(SpecialCase)
admin.site.register(ApplicationFormFields)
