from django.db import models

# Create your models here.
class Pageitem(models.Model):
#    lang_id = models.CharField(max_length=10, blank=True, null=True) #id Języka.
    lang_flag = models.ImageField(upload_to='images') #Mały obrazek języka
    headtitle = models.CharField(max_length=200) #Nagłówek strony w tym języku
    mainpage = models.CharField(max_length=200) #Strona główna w tym języku
    information = models.CharField(max_length=200) #Informacje w tym języku
    akamap = models.CharField(max_length=200) #Mapa akademików w tym języku
    contact = models.CharField(max_length=200) #Kontakty w tym języku
    logout = models.CharField(max_length=200) #Wyloguj
    news = models.CharField(max_length=200) #Aktualności
    docs = models.CharField(max_length=200) #Ważne pliki

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.CharField(max_length=500, blank=True, null=True)

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

    #Ta funkcja ogranicza długość tekstu na stronie wpisów, żeby nie było zbyt rozlegle i każdy mógł sobie wybrać...
    def summary(self):
        return self.body[:110]

    #Funkcja formatująca datę w ludzki sposób...
    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')

class Info (models.Model): #Katalog "informacje" ze strony SEKS
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

class Fileserve(models.Model): #serwowanie plików statycznych
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
#?    image = models.ImageField(upload_to='images', blank=True, null=True)
    file = models.FileField(upload_to='assets', blank=True, null=True) # Chyba się konfiguruje jak obrazki ale się nie zdziw jak wybuchnie Ci w twarz...
#?    link = models.CharField(max_length=500, blank=True, null=True)

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

    #Funkcja formatująca datę w ludzki sposób...
    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')
