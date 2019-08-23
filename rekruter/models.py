from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


# Klasa zmienia autentykację Usera na email jak w Core2.
class User(AbstractBaseUser, PermissionsMixin):
    USER = 1
    COUNCIL = 2
    COUNCIL_ADMIN = 3
    SUPERUSER = 4
    ROLE_CHOICES = (
     (USER, 'User'),
     (COUNCIL, 'Council'),
     (COUNCIL_ADMIN, 'Council Admin'),
     (SUPERUSER, 'Superuser'),
    )
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('staff status'), default=False,)
    is_active = models.BooleanField(_('active'), default=True)
    is_translator = models.BooleanField(_('translator'), default=False)
    is_hotel = models.BooleanField(_('hotel'), default=False)
    role_council = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    quarter = models.CharField(_('quarter'), max_length=2, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


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
    assigned_to = models.CharField(max_length=50, null=True)
    data_correct = models.CharField(max_length=250)
    assign_again = models.CharField(max_length=250)
    list_select = models.CharField(max_length=50)


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

    def gen_quartzlist(self):
        self.quartzlista = []
        for attr in self:
            self.quartzlista.append(attr)
        return self.quartzlista
