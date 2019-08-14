from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    USER = 1
    COUNCIL = 2
    STAFF = 3
    SUPERUSER = 4
    ROLE_CHOICES = (
     (USER, 'Student'),
     (COUNCIL, 'Teacher'),
     (STAFF, 'Staff'),
     (SUPERUSER, 'Superuser'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quarter = models.CharField(max_length=20, blank=True, null=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
