from django import forms
from django.contrib.auth.forms import UserCreationForm
from rekruter.models import User, ApplicationFormFields
from akademik.models import HousingParty as HParty
from esks.special.classes import checkifnull as cn
import datetime


class ExtendedCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)
    gender = forms.CharField(widget=forms.HiddenInput(), required=False)
    citizenship = forms.CharField(max_length=30)
    dowod = forms.CharField(max_length=20, required=False)
    passport = forms.CharField(max_length=20, required=False)
    telephone = forms.CharField(max_length=30)
    street = forms.CharField(max_length=30)
    building_no = forms.CharField(max_length=15)
    local_no = forms.CharField(max_length=10, required=False)
    postcode = forms.CharField(max_length=7)
    city = forms.CharField(max_length=25)
    album = forms.CharField(max_length=25, required=False)

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'gender',
            'citizenship',
            'dowod',
            'passport',
            'telephone',
            'street',
            'building_no',
            'local_no',
            'postcode',
            'city',
            'album',
        )

    def save(self, commit=True):
        user = super(ExtendedCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.gender = int(self.cleaned_data["gender"])
        user.citizenship = self.cleaned_data["citizenship"]
        user.dowod = self.cleaned_data["dowod"]
        user.passport = self.cleaned_data["passport"]
        user.telephone = self.cleaned_data["telephone"]
        user.street = self.cleaned_data["street"]
        user.building_no = self.cleaned_data["building_no"]
        user.local_no = self.cleaned_data["local_no"]
        user.postcode = self.cleaned_data["postcode"]
        user.city = self.cleaned_dstateata["city"]
        user.city = self.cleaned_data["album"]

        if commit:
            user.save()
        return user


# Zmienia akcję kwaterunkową.
class IniForm(forms.ModelForm):
    quarter = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('quarter', )

    def save(self, commit=True):
        user = super(IniForm, self).save(commit=False)
        user.quarter = self.cleaned_data["quarter"]
        if commit:
            user.save()
        return user


# Zmienia podstawowe uprawnienia dla rady studentów.
class PowerForm(forms.ModelForm):
    role_council = forms.BooleanField(required=False)
    is_translator = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('is_translator', )

    def save(self, role, commit=True):
        user = super(PowerForm, self).save(commit=False)
        user.is_translator = self.cleaned_data["is_translator"]
        user.role_council = role
        if commit:
            user.save()
        return user


# Formularz to tworzenia i modyfikowania podań o akademik. UWAGA!
# Rośnie Ci złożoność cyklomatyczna! - najlepiej zrób dwa formularze.
# Jeden do tworzenia a drugi do modyfikacji.
class ApplicationForm(forms.ModelForm):
    sh_choice1 = forms.CharField(widget=forms.HiddenInput(), required=False)
    sh_choice2 = forms.CharField(widget=forms.HiddenInput(), required=False)
    sh_choice3 = forms.CharField(widget=forms.HiddenInput(), required=False)
    if_room_change = forms.CharField(widget=forms.HiddenInput(), required=False)
    duration = forms.CharField(widget=forms.HiddenInput(), required=False)
    location = forms.CharField(widget=forms.HiddenInput(), required=False)
    faculty = forms.CharField(widget=forms.HiddenInput(), required=False)
    degree = forms.CharField(widget=forms.HiddenInput(), required=False)
    deangroup = forms.CharField(max_length=30, required=False)
    semester = forms.CharField(widget=forms.HiddenInput(), required=False)
    spouse_cohabitant = forms.CharField(widget=forms.HiddenInput(), required=False)
    special_case_docs = forms.CharField(widget=forms.HiddenInput(), required=False)
    international_placement = forms.CharField(widget=forms.HiddenInput(), required=False)
    mailinglist = forms.CharField(widget=forms.HiddenInput(), required=False)
    dataprocessing = forms.CharField(widget=forms.HiddenInput(), required=False)
    # attachment = forms.FileField(max_length=250, allow_empty_file=True)

    class Meta:
        model = ApplicationFormFields
        fields = (

        )

    def save(self, uid, commit=True, **kwargs):
        application = super(ApplicationForm, self).save(commit=False)
        application.owner = uid
        application.sh_choice1 = cn(self.cleaned_data["sh_choice1"])
        application.sh_choice2 = cn(self.cleaned_data["sh_choice2"])
        application.sh_choice3 = cn(self.cleaned_data["sh_choice3"])
        application.if_room_change = cn(self.cleaned_data["if_room_change"])
        application.duration = cn(self.cleaned_data["duration"])
        application.location = self.cleaned_data["location"]
        application.faculty = cn(self.cleaned_data["faculty"])
        application.degree = cn(self.cleaned_data["degree"])
        application.deangroup = self.cleaned_data["deangroup"]
        application.semester = cn(self.cleaned_data["semester"])
        application.spouse_cohabitant = cn(self.cleaned_data["spouse_cohabitant"])
        application.special_case_docs = cn(self.cleaned_data["special_case_docs"])
        application.international_placement = self.cleaned_data["international_placement"]
        application.mailinglist = self.cleaned_data["mailinglist"]
        application.dataprocessing = self.cleaned_data["dataprocessing"]
        # application.attachment = self.cleaned_data["attachment"]
        if application.timeapplied is None:
            application.timeapplied = datetime.datetime.now()
        if application.status is None:
            application.status = 0
        if application.quarter is None:
            request = kwargs['request']
            application.quarter = request.user.quarter
        if commit:
            application.save()
        return application


class PartyForm(forms.ModelForm):
    title_pl = forms.CharField(max_length=200)
    title_en = forms.CharField(max_length=200)
    quarter = forms.CharField(widget=forms.HiddenInput())
    date_start = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    date_end = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    comment_pl = forms.CharField(widget=forms.Textarea, required=False)
    comment_en = forms.CharField(widget=forms.Textarea, required=False)
    announcement_pl = forms.CharField(widget=forms.Textarea, required=False)
    announcement_en = forms.CharField(widget=forms.Textarea, required=False)
    userdata1 = forms.BooleanField(required=False)
    sh_preferences = forms.BooleanField(required=False)
    userdata2 = forms.BooleanField(required=False)
    formmap = forms.BooleanField(required=False)
    faculty_data = forms.BooleanField(required=False)
    extra_info = forms.BooleanField(required=False)
    agreements1 = forms.BooleanField(required=False)
    # agreements2 = forms.BooleanField(required=False)
    # agreements3 = forms.BooleanField(required=False)

    class Meta:
        model = HParty
        fields = (
         'title_pl', 'title_en', 'quarter', 'date_start', 'date_end',
         'comment_pl', 'comment_en', 'announcement_pl', 'announcement_en',
         'userdata1',  'sh_preferences', 'userdata2',
         'formmap', 'faculty_data', 'extra_info', 'agreements1')

    def save(self, uid, commit=True):
        party = super(PartyForm, self).save(commit=False)
        party.owner = uid
        party.title_pl = self.cleaned_data["title_pl"]
        party.title_en = self.cleaned_data["title_en"]
        party.quarter = self.cleaned_data["quarter"]
        party.date_start = self.cleaned_data["date_start"]
        party.date_end = self.cleaned_data["date_end"]
        party.comment_pl = self.cleaned_data["comment_pl"]
        party.comment_en = self.cleaned_data["comment_en"]
        party.announcement_pl = self.cleaned_data["announcement_pl"]
        party.announcement_en = self.cleaned_data["announcement_en"]
        party.userdata1 = self.cleaned_data["userdata1"]
        party.sh_preferences = self.cleaned_data["sh_preferences"]
        party.userdata2 = self.cleaned_data["userdata2"]
        party.formmap = self.cleaned_data["formmap"]
        party.faculty_data = self.cleaned_data["faculty_data"]
        party.extra_info = self.cleaned_data["extra_info"]
        party.agreements1 = self.cleaned_data["agreements1"]

        if commit:
            party.save()
        return party
