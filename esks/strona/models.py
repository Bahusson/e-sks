from django.db import models

# Create your models here.
class Pageitems(models.Model):
    lang_id = models.IntField(max_length=2) #ID języka
    lang_name = models.CharField(max_length=50) #Nazwa języka
    headtitle = models.CharField(max_length=200) #Nagłówek strony w tym języku
    mainpage = models.CharField(max_length=200) #Strona główna w tym języku
    info = models.CharField(max_length=200) #Informacje w tym języku
    akamap = models.CharField(max_length=200) #Mapa akademików w tym języku
    contact = models.CharField(max_length=200) #Kontakty w tym języku
    logout = models.CharField(max_length=200) # Wyloguj
 

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title
