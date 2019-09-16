from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from esks.settings import AUTH_USER_MODEL
import uuid


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
    OTHER = 0
    MALE = 1
    FEMALE = 2
    GENDERS = (
     (OTHER, 'other'),
     (MALE, 'male'),
     (FEMALE, 'female'),
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
    gender = models.PositiveSmallIntegerField(
        choices=GENDERS, null=True, blank=True)
    citizenship = models.CharField(_('citizenship'), max_length=40, blank=True)
    dowod = models.CharField(_('dowod'), max_length=20, blank=True)
    passport = models.CharField(_('passport'), max_length=20, blank=True)
    telephone = models.CharField(_('telephone'), max_length=20, blank=True)
    street = models.CharField(_('street'), max_length=30, blank=True)
    building_no = models.CharField(_('building_no'), max_length=15, blank=True)
    local_no = models.CharField(_('local_no'), max_length=10, blank=True)
    postcode = models.CharField(_('postcode'), max_length=7, blank=True)
    city = models.CharField(_('city'), max_length=25, blank=True)
    album = models.CharField(_('album'), max_length=25, blank=True)

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
    personal_data = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    dowod = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    warning_f = models.CharField(max_length=50)
    tel_mandatory = models.CharField(max_length=50)
    defaul_t = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    preferences = models.CharField(max_length=50)
    match_prefs = models.CharField(max_length=250)
    see_map = models.CharField(max_length=50)
    choose = models.CharField(max_length=50)
    i_ask = models.CharField(max_length=50)
    time_in_sh = models.CharField(max_length=100)
    adress_data = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building_no = models.CharField(max_length=50)
    local_no = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    click_map = models.CharField(max_length=50)
    search = models.CharField(max_length=50)
    check_search = models.CharField(max_length=100)
    check_mandatory = models.CharField(max_length=200)
    search_failed = models.CharField(max_length=250)
    pref_as_stud = models.CharField(max_length=100)
    faculty = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    deangroup = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    additional_info = models.CharField(max_length=50)
    spouse_cohabitant = models.CharField(max_length=100)
    special_case_docs = models.CharField(max_length=100)
    statement = models.CharField(max_length=50)
    agree = models.CharField(max_length=50)
    disagree = models.CharField(max_length=50)
    mail_join = models.TextField()
    data_processing = models.TextField()
    appendix = models.CharField(max_length=50)
    sendme = models.CharField(max_length=50)
    ufile = models.CharField(max_length=50)
    browse = models.CharField(max_length=50)
    appendix_name = models.CharField(max_length=50)
    del_file = models.CharField(max_length=50)
    down_file = models.CharField(max_length=50)
    nofile_chosen = models.CharField(max_length=50)
    nought = models.CharField(max_length=50)
    male = models.CharField(max_length=50)
    female = models.CharField(max_length=50)
    other = models.CharField(max_length=50)
    app_for_sh = models.CharField(max_length=50)
    app_no = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    created = models.CharField(max_length=50)
    spouseID = models.CharField(max_length=50)
    stays = models.CharField(max_length=50)
    show_by = models.CharField(max_length=50)
    results = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    agree_international = models.CharField(max_length=100)
    or_if = models.CharField(max_length=50)
    change_man = models.CharField(max_length=50)


# Wszystkie domy studenckie - nazwy i być może atrybuty.
class StudentHouse(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


# Czy chce zmienić pokój czy zostać.
class IfRoomChange(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


# Czas przyznania pobytu.
class TimePeriod(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


# Lista wszystkich wydziałów.
class StudyFaculty(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


# Lista wszystkich rodzajów studiów.
class StudyDegree(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


# Czy chce mieszkać z małżonkiem
class SpouseCohabitant(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


# Podanie o szczególne okoliczności
class SpecialCase(models.Model):
    name = models.CharField(max_length=150)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


class ApplicationStatus(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']


class ApplicationFormFields(models.Model):
    # Klasa do wypełniania pól formularza przez Userów.
    application_no = models.UUIDField(
     primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
     AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Preferencje akademików 1-3
    sh_choice1 = models.CharField(max_length=2, blank=True)
    sh_choice2 = models.CharField(max_length=2, blank=True)
    sh_choice3 = models.CharField(max_length=2, blank=True)
    # Czy zmiana pokoju?
    if_room_change = models.CharField(max_length=2, blank=True)
    duration = models.CharField(max_length=2, blank=True)
    location = models.CharField(max_length=50, blank=True)
    faculty = models.CharField(max_length=2, blank=True)
    degree = models.CharField(max_length=2, blank=True)
    deangroup = models.CharField(max_length=50, blank=True)
    semester = models.CharField(max_length=2, blank=True)
    spouse_cohabitant = models.CharField(max_length=2, blank=True)
    special_case_docs = models.CharField(max_length=2, blank=True)
    international_placement = models.BooleanField(blank=True, null=True)
    mailinglist = models.BooleanField(blank=True, null=True)
    dataprocessing = models.BooleanField(blank=True, null=True)
    attachment = models.FileField(upload_to='userdocs', null=True, blank=True)

    class Meta:
        ordering = ['owner', 'application_no']

    def __str__(self):
        return str(self.application_no) + ' ' + str(self.owner)


class QuarterClassB(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    class Meta:
        ordering = ['position', 'id']

    def __str__(self):
        return self.name
