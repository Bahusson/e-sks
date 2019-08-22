from django.db import models
# W tej klasie będą elementy wspólne dla wszystkich paneli.


# Ta klasa jest klasą tłumaczeniową wspólna dla wszystkich portali.
class PortalItem(models.Model):
    PORTAL_CHOICES = [
        (1, 'User'),
        (2, 'Council'),
        (3, 'Hotel'),
        (4, 'Translator'), ]
    portal = models.CharField(max_length=1, choices=PORTAL_CHOICES)
    menus =

    def __str__(self):
        return self.portal

    class Meta:
        ordering = ['Portal']


# Ta klasa jest klasą tłumaczeniową dla Akademika.
class CouncilItem(models.Model):
    title = models.CharField(max_length=200)


# Ta klasa jest klasą tłumaczeniową dla Akademika.
class TranslatorItem(models.Model):
    title = models.CharField(max_length=200)


# Ta klasa jest klasą tłumaczeniową dla Akademika.
class UserItem(models.Model):
    title = models.CharField(max_length=200)
