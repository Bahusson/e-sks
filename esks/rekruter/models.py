from django.db import models

class Sito(models.Model): #Sito pytań do akcji kwaterunkowej
    intro = models.CharField(max_length=500)
    oswiadczenie = models.TextField()
    obywatelstwo = models.CharField(max_length=150)
    student = models.CharField(max_length=150)
    doktorant = models.CharField(max_length=150)
    zamiar = models.CharField(max_length=150)
    zadnezpow = models.CharField(max_length=150)
    pelnywym = models.CharField(max_length=150)
    erasmus = models.CharField(max_length=150)
    bilateral = models.CharField(max_length=150)
    buttondalej = models.CharField(max_length=100)

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

#class Zapis(models.Model):

#    imie = models.CharField(max_length=50) #Imie w danym jezyku (np. "name" po angielsku)
#    imie_instrukcja = models.TextField() # Instrukcja dot wprowadzania imienia, nazwiska i znakow.
#    nazwisko = models.CharField(max_length=50) #Nazwisko w danym jezyku (np. "surname" po angielsku)

#Kontynuuj tak dalej ze wszystkimi elementami na stronie. ^^

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
#    def __str__(self):
#        return self.title
