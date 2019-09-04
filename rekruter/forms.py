from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from rekruter.models import User, ApplicationFormFields
from akademik.models import HousingParty


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
        user.city = self.cleaned_data["city"]
        user.city = self.cleaned_data["album"]

        if commit:
            user.save()
        return user


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


class ApplicationForm(forms.ModelForm):
    sh_choice1 = forms.CharField(widget=forms.HiddenInput())
    sh_choice2 = forms.CharField(widget=forms.HiddenInput())
    sh_choice3 = forms.CharField(widget=forms.HiddenInput())
    if_room_change = forms.CharField(widget=forms.HiddenInput())
    duration = forms.CharField(widget=forms.HiddenInput())
    # location = forms.CharField(widget=forms.HiddenInput())
    faculty = forms.CharField(widget=forms.HiddenInput())
    degree = forms.CharField(widget=forms.HiddenInput())
    deangroup = forms.CharField(max_length=30, required=False)
    semester = forms.CharField(widget=forms.HiddenInput())
    spouse_cohabitant = forms.CharField(widget=forms.HiddenInput())
    special_case_docs = forms.CharField(widget=forms.HiddenInput())
    international_placement = forms.CharField(widget=forms.HiddenInput())
    mailinglist = forms.CharField(widget=forms.HiddenInput())
    dataprocessing = forms.CharField(widget=forms.HiddenInput())
    # attachment = forms.FileField(max_length=250, allow_empty_file=True)

    class Meta:
        model = ApplicationFormFields
        fields = (
         'sh_choice1', 'sh_choice2', 'sh_choice3', 'if_room_change',
         'duration',
         # 'location',
         'faculty', 'deangroup', 'semester',
         'spouse_cohabitant', 'special_case_docs', 'international_placement',
         'mailinglist', 'dataprocessing',  # 'attachment',
        )

    def save(self, uid, commit=True):
        application = super(ApplicationForm, self).save(commit=False)
        application.owner = uid
        application.sh_choice1 = int(self.cleaned_data["sh_choice1"])
        application.sh_choice2 = int(self.cleaned_data["sh_choice2"])
        application.sh_choice3 = int(self.cleaned_data["sh_choice3"])
        application.if_room_change = int(self.cleaned_data["if_room_change"])
        application.duration = int(self.cleaned_data["duration"])
        # application.location = self.cleaned_data["location"]
        application.faculty = int(self.cleaned_data["faculty"])
        application.degree = int(self.cleaned_data["degree"])
        application.deangroup = self.cleaned_data["deangroup"]
        application.semester = int(self.cleaned_data["semester"])
        application.spouse_cohabitant = int(self.cleaned_data["spouse_cohabitant"])
        application.special_case_docs = int(self.cleaned_data["special_case_docs"])
        application.international_placement = int(self.cleaned_data["international_placement"])
        application.mailinglist = int(self.cleaned_data["mailinglist"])
        application.dataprocessing = int(self.cleaned_data["dataprocessing"])
        # application.attachment = self.cleaned_data["attachment"]
        if commit:
            application.save()
        return application


class PartyForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    #title_pl = forms.CharField(max_length=200)
    #title_en = forms.CharField(max_length=200)
    quarter = forms.CharField(widget=forms.HiddenInput())
    # date_start = forms.DateTimeField(widget=widgets.AdminSplitDateTime())
    # date_end = forms.DateTimeField(widget=widgets.AdminSplitDateTime())
    # date_start = forms.SplitDateTimeField()
    # date_end = forms.SplitDateTimeField()
    comment = forms.CharField(widget=forms.Textarea, required=False)
    # comment_pl = forms.CharField(widget=forms.Textarea, required=False)
    # comment_en = forms.CharField(widget=forms.Textarea, required=False)
    announcement = forms.CharField(widget=forms.Textarea, required=False)
    # announcement_pl = forms.CharField(widget=forms.Textarea, required=False)
    # announcement_en = forms.CharField(widget=forms.Textarea, required=False)
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
        model = HousingParty
        fields = (
         'title',
         #'title_pl', 'title_en',
         'quarter',
         # 'date_start', 'date_end',
         'comment', #'comment_pl', 'comment_en',
         'announcement',
         #'announcement_pl', 'announcement_en',
         'userdata1',
         'sh_preferences', 'userdata2',
         'formmap', 'faculty_data', 'extra_info', 'agreements1')

    # Tworzy takie rozbite pole DateTime jak to w adminie.
    # https://stackoverflow.com/questions/15643019/datetime-field-in-django-form-model
    # def __init__(self, *args, **kwargs):
    #    super(PartyForm, self).__init__(*args, **kwargs)
    #    self.fields['date_start'].widget = widgets.AdminSplitDateTime()
    #    self.fields['date_end'].widget = widgets.AdminSplitDateTime()

    def save(self, uid, commit=True):
        party = super(PartyForm, self).save(commit=False)
        party.owner = uid
        party.title = self.cleaned_data["title"]
        # party.title_pl = self.cleaned_data["title"]
        # party.title_en = self.cleaned_data["title_en"]
        party.quarter = self.cleaned_data["quarter"]
    #    party.date_start = self.cleaned_data["date_start"]
    #    party.date_end = self.cleaned_data["date_end"]
        party.comment = self.cleaned_data["comment"]
        # party.comment_pl = self.cleaned_data["comment"]
        # party.comment_en = self.cleaned_data["comment_en"]
        party.announcement = self.cleaned_data["announcement"]
        # party.announcement_pl = self.cleaned_data["announcement"]
        # party.announcement_en = self.cleaned_data["announcement_en"]
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
