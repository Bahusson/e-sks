from django.db import models


class Pageitem(models.Model):
    lang_flag = models.ImageField(upload_to='images')  # Mały obrazek języka
    headtitle = models.CharField(max_length=200)  # Nagłówek strony w tym j
    mainpage = models.CharField(max_length=200)  # Strona główna w tym języku
    information = models.CharField(max_length=200)  # Informacje w tym języku
    akamap = models.CharField(max_length=200)  # Mapa akademików w tym języku
    contact = models.CharField(max_length=200)  # Kontakty w tym języku
    logout = models.CharField(max_length=200)  # Wyloguj
    news = models.CharField(max_length=200)  # Aktualności
    docs = models.CharField(max_length=200)  # Ważne pliki
    login = models.CharField(max_length=200, blank=True, null=True)  # zaloguj


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:110]

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


class Info (models.Model):  # Katalog "informacje" ze strony SEKS
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title


class Fileserve(models.Model):  # serwowanie plików niestatycznych
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    file = models.FileField(upload_to='assets', blank=True, null=True)

    def __str__(self):
        return self.title

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')
