from django.db import models
from esks.settings import AUTH_USER_MODEL


# W tej klasie będą elementy wspólne dla wszystkich paneli.
class PortalBaseItem(models.Model):
    PORTAL_CHOICES = [
        ('1', 'User'),
        ('2', 'Council'),
        ('3', 'Hotel'),
        ('4', 'Translator'), ]
    portal = models.CharField(
     max_length=1, unique=True, choices=PORTAL_CHOICES)
    title = models.CharField(max_length=200)
    descr = models.CharField(max_length=400)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['portal']


# To zestaw klas tłumaczeniowych dla panelu Akademika.
class HotelMenuItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['position']


class HotelLinkItem(models.Model):
    title = models.CharField(max_length=200)
    menu = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['menu', 'position']


# To zestaw klas tłumaczeniowych dla panelu Rady
class CouncilMenuItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['position']


class CouncilLinkItem(models.Model):
    title = models.CharField(max_length=200)
    menu = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['menu', 'position']


# To zestaw klas tłumaczeniowych dla panelu Tłumacza
class TranslatorMenuItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['position']


class TranslatorLinkItem(models.Model):
    title = models.CharField(max_length=200)
    menu = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['menu', 'position']


# To zestaw klas tłumaczeniowych dla panelu Użytkownika
class UserMenuItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['position']


class UserLinkItem(models.Model):
    title = models.CharField(max_length=200)
    menu = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['menu', 'position']


# Ta klasa tworzy i porządkuje akcje kwaterunkowe
# Dodaje też ogłoszenie w wielu językach.
class HousingParty(models.Model):
    title = models.CharField(blank=True, max_length=200)
    quarter = models.IntegerField()
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True)
    announcement = models.TextField(blank=True)
    userdata1 = models.BooleanField(default=False)
    sh_preferences = models.BooleanField(default=False)
    userdata2 = models.BooleanField(default=False)
    formmap = models.BooleanField(default=False)
    faculty_data = models.BooleanField(default=False)
    extra_info = models.BooleanField(default=False)
    agreements1 = models.BooleanField(default=False)
    agreements2 = models.BooleanField(default=False)
    agreements3 = models.BooleanField(default=False)
    owner = models.ForeignKey(
     AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_start', 'date_end', 'quarter']


# Klasa tłumaczeniowa związana z akcjami kwaterunkowymi
class HousingPartyItems(models.Model):
    party_title = models.CharField(blank=True, max_length=200)
    choose_party = models.CharField(blank=True, max_length=200)
    time_start = models.CharField(blank=True, max_length=200)
    time_end = models.CharField(blank=True, max_length=200)
    comment = models.CharField(blank=True, max_length=200)
    announce = models.CharField(blank=True, max_length=200)
    tick_form = models.CharField(blank=True, max_length=200)
    p_from = models.CharField(blank=True, max_length=200)
    p_to = models.CharField(blank=True, max_length=200)
    changeme = models.CharField(blank=True, max_length=200)
    all_parties = models.CharField(blank=True, max_length=200)
    active_parties = models.CharField(blank=True, max_length=200)
    past_parties = models.CharField(blank=True, max_length=200)
    future_parties = models.CharField(blank=True, max_length=200)
    new_party_view = models.CharField(blank=True, max_length=200)
    owner = models.CharField(blank=True, max_length=200)
    userinfo = models.CharField(blank=True, max_length=250)
    housing_party = models.CharField(blank=True, max_length=200)
    change_and_apply = models.CharField(blank=True, max_length=200)
