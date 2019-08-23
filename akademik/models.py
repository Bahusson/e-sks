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
