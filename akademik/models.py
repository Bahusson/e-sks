from django.db import models


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
    title = models.CharField(max_length=200)
    quarter = models.IntegerField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
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

    def __str__(self):
        return self.title

    def get_startdate(self):
        return self.date_start.date

    def get_enddate(self):
        return self.date_end.date

    class Meta:
        ordering = ['date_start', 'date_end', 'quarter']
