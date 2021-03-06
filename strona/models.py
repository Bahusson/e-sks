from django.db import models
from esks.settings import AUTH_USER_MODEL


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
    login = models.CharField(max_length=200)  # zaloguj
    panel_user = models.CharField(max_length=200)
    panel_council = models.CharField(max_length=200)
    panel_staff = models.CharField(max_length=200)
    panel_translator = models.CharField(max_length=200)
    backtouserpanel = models.CharField(max_length=200)
    see_more = models.CharField(max_length=200)
    pagemap = models.CharField(max_length=200)
    addblog = models.CharField(max_length=200)
    addinfo = models.CharField(max_length=200)
    addfile = models.CharField(max_length=200)
    editme = models.CharField(max_length=200)

    def akamap_c(self):
        return self.akamap.upper()

    def mainpage_c(self):
        return self.mainpage.upper()


# Aktualności widoczne na głównych kafelkach na stronie.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data widoczności w publikacji
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.CharField(max_length=500, blank=True, null=True)
    lastmod = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(
     AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


# Bardziej permanentne "ważne informacje" ze strony E-SKS.
class Info (models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data widoczności w publikacji
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    lastmod = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(
     AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


# Ważne pliki do pobrania ze strony.
class Fileserve(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data widoczności w publikacji
    body = models.TextField()
    file = models.FileField(upload_to='docs', blank=True, null=True)
    lastmod = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(
     AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


# Klasa skórek do naszej apki. Pola nienulowalne.
class PageSkin(models.Model):
    themetitle = models.CharField(max_length=200)
    position = models.IntegerField()
    blogimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    infoimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    fileimagedefault = models.ImageField(
     upload_to='skins', blank=True, null=True)
    infosideimage = models.ImageField(
     upload_to='skins', blank=True, null=True)
    filesideimage = models.ImageField(
     upload_to='skins', blank=True, null=True)
    welcomebanner = models.ImageField(
     upload_to='skins', blank=True, null=True)
    welcomebanner_small = models.ImageField(
     upload_to='skins', blank=True, null=True)
    eskslogo_main = models.ImageField(
     upload_to='skins', blank=True, null=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.themetitle


# klasa tłumaczeniowa dla Blog, Info, Fileserve.
class FormElement(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    lastmod = models.CharField(max_length=200)
    by = models.CharField(max_length=200)
    blog = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    file = models.CharField(max_length=200)
    new = models.CharField(max_length=200)
    change = models.CharField(max_length=200)
