from django.db import models
from django.contrib.auth.forms import UserCreationForm, User
from django import forms


class Sito(models.Model):  # Sito pytań do akcji kwaterunkowej
    intro = models.CharField(max_length=500)
    yes = models.CharField(max_length=50, null=True)
    no = models.CharField(max_length=50, null=True)
    oswiadczenie = models.TextField()
    obywatelstwo = models.CharField(max_length=150)
    student = models.CharField(max_length=150)
    doktorant = models.CharField(max_length=150)
    zamiar = models.CharField(max_length=150)
    pierwszegosto = models.CharField(max_length=150)
    pelnywym = models.CharField(max_length=150)
    erasmus = models.CharField(max_length=150)
    buttondalej = models.CharField(max_length=100)


class ExtendedCreationForm(UserCreationForm):  # Rozszerzenie formularza rejestracji
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",)

    def save(self, commit=True):
        user = super(ExtendedCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
