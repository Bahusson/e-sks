from django.db import models
# W tej klasie będą elementy wspólne dla wszystkich paneli.


# Ta klasa jest klasą tłumaczeniową dla panelu Akademika.
class HotelBaseItem(models.Model):
    title = models.CharField(max_length=200)
    descr = models.CharField(max_length=400)


class HotelMenuItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()


class HotelLinkItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()


# Ta klasa jest klasą tłumaczeniową dla panelu Rady
class CouncilBaseItem(models.Model):
    title = models.CharField(max_length=200)
    descr = models.CharField(max_length=400)


class CouncilMenuItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()


class CouncilLinkItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()


# Ta klasa jest klasą tłumaczeniową dla panelu Tłumacza
class TranslatorItemBase(models.Model):
    title = models.CharField(max_length=200)
    descr = models.CharField(max_length=400)


class TranslatorMenuItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()


class TranslatorLinkItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()


# Ta klasa jest klasą tłumaczeniową dla panelu Użytkownika
class UserBaseItem(models.Model):
    title = models.CharField(max_length=200)
    descr = models.CharField(max_length=400)


class UserMenuItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()


class UserLinkItem(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()
