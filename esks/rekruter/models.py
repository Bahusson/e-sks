from django.db import models

class Sito(models.Model):
    ### Część wspólna także dla klasy "Zapis", więc się upewnij, że dobrze wpisałeś ID języka.
    # Zaczynasz od 0, gdzie 0 to Polski, a 1 to Angielski.
    # Na sicie zawsze można podejrzeć który język jest który i TEN obowiązuje!
    formlang_id = models.IntField(max_length=1) #Tu wpisz id jezyka po ktorym beda one uszeregowane w programie i wywolywane.
    formlang_name = models.CharField(max_length=20) #To sie wyswietla w polu wybory dostepnych jezykow.
    ### Koniec części wspólnej z klasą zapisu.
    obywatelstwo = models.CharField(max_length=100)
    obywatelstwo = models.CharField(max_length=100)


class Zapis(models.Model):
    ### Część wspólna dla klasy "Sito". Po tym klasy się odnajdują.
    # Szczegóły patrz wyżej w klasie "Sito".
    formlang_id = models.IntField(max_length=1) #ID języka takie samo jak w Sicie!!
    formlang_name = models.CharField(max_length=20) #Nazwa języka jak w Sicie. W programie jest tylko do orientacji, żeby w administracji nie przełączać się między klasami.
    ### Koniec części wspólnej z klasą sita.
    imie = models.CharField(max_length=50) #Imie w danym jezyku (np. "name" po angielsku)
    imie_instrukcja = models.TextField() # Instrukcja dot wprowadzania imienia, nazwiska i znakow.
    nazwisko = models.CharField(max_length=50) #Nazwisko w danym jezyku (np. "surname" po angielsku)

#Kontynuuj tak dalej ze wszystkimi elementami na stronie. ^^

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title
