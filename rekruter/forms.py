from django import forms
from django.contrib.auth.forms import UserCreationForm
from rekruter.models import User, ApplicationFormFields


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


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'quarter',
        )

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
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
    location = forms.CharField(widget=forms.HiddenInput())
    faculty = forms.CharField(widget=forms.HiddenInput())
    deangroup = forms.CharField(widget=forms.HiddenInput())
    semester = forms.CharField(widget=forms.HiddenInput())
    spouse_cohabitant = forms.CharField(widget=forms.HiddenInput())
    special_case_docs = forms.CharField(widget=forms.HiddenInput())
    international_placement = forms.CharField(widget=forms.HiddenInput())
    mailinglist = forms.CharField(widget=forms.HiddenInput())
    dataprocessing = forms.CharField(widget=forms.HiddenInput())
    attachment = forms.FileField(max_length=250, allow_empty_file=True)

    class Meta:
        model = ApplicationFormFields
        fields = (
         'sh_choice1', 'sh_choice2', 'sh_choice3', 'if_room_change',
         'duration', 'location', 'faculty', 'deangroup', 'semester',
         'spouse_cohabitant', 'special_case_docs', 'international_placement',
         'mailinglist', 'dataprocessing', 'attachment',
        )

    def save(self, commit=True):
        application = super(ApplicationForm, self).save(commit=False)
        application.sh_choice1 = self.cleaned_data["sh_choice1"]
        application.sh_choice2 = self.cleaned_data["sh_choice2"]
        application.sh_choice3 = self.cleaned_data["sh_choice3"]
        application.if_room_change = self.cleaned_data["if_room_change"]
        application.duration = self.cleaned_data["duration"]
        application.location = self.cleaned_data["location"]
        application.faculty = self.cleaned_data["faculty"]
        application.deangroup = self.cleaned_data["deangroup"]
        application.semester = self.cleaned_data["semester"]
        application.spouse_cohabitant = self.cleaned_data["spouse_cohabitant"]
        application.special_case_docs = self.cleaned_data["special_case_docs"]
        application.international_placement = self.cleaned_data["international_placement"]
        application.mailinglist = self.cleaned_data["mailinglist"]
        application.dataprocessing = self.cleaned_data["dataprocessing"]
        application.attachment = self.cleaned_data["attachment"]
        if commit:
            application.save()
        return application
