from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Sito(models.Model):
    # Sito pytań do akcji kwaterunkowej
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


class FormItems(models.Model):
    # Klasa do tłumaczeń rekrutera. Do usunięcia w produkcji
    login = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    re_password = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    register = models.CharField(max_length=50, null=True)
    admin_panel = models.CharField(max_length=50, null=True)
    back = models.CharField(max_length=50, null=True)
    action = models.CharField(max_length=50, null=True)


class QuarterClass(models.Model):
    # Klasa do tłumaczenia nazw Akcji Kwaterunkowych.
    stud_local = models.CharField(max_length=50, null=True)
    stud_foreign = models.CharField(max_length=50, null=True)
    phd = models.CharField(max_length=50, null=True)
    bank = models.CharField(max_length=50, null=True)
    new1 = models.CharField(max_length=50, null=True)
    new23 = models.CharField(max_length=50, null=True)
    new_foreign = models.CharField(max_length=50, null=True)
    erasmus = models.CharField(max_length=50, null=True)
    bilateral = models.CharField(max_length=50, null=True)


class Profile(models.Model):
    # Klasa zmieniająca klasę usera. Plus dwa dekoratory linkujące.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quarter = models.CharField(max_length=20, blank=True, default='')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ExtendedCreationForm(UserCreationForm):
    # Rozszerzenie formularza rejestracji
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def save(self, quarter, commit=True):
        user = super(ExtendedCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.quarter = quarter
        if commit:
            user.save()
        return user
