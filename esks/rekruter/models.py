from django.db import models

# Create your models here.
class Zapis(models.Model):
    formlang_id = models.IntField(max_length=1) #Tu wpisz id jezyka po ktorym beda one uszeregowane w programie i wywolywane.
    formlang_name = models.CharField(max_length=20) #To sie wyswietla w polu wybory dostepnych jezykow.
    imie = models.CharField(max_length=50) #Imie w danym jezyku (np. "name" po angielsku)
    nazwisko = models.CharField(max_length=50) #Nazwisko w danym jezyku (np. "surname" po angielsku)
#Kontynuuj tak dalej ze wszystkimi elementami na stronie. ^^

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title
