# E-SKS (Elektroniczny system kwaterunkowy studentów) - Aplikacja kwaterunkowa dla domów studenckich PW.

Technologie: Python 3.6, Django 2, JavaScript, CSS3 ,Bootstrap 4, HTML5, PostgreSQL.

adres strony: http://esks.pl/

Dostęp do funkcjonalności z poziomu administratora:

admin: cadmin@pw.edu.pl

password: Politechnika_1!

funkcjonalności:

- aplikacja jest połączona z bazą danych PostgreSQL.

- strona opiera się na serwerze i  CDN umieszczonym na DigitalOcean.com

- zawiera midlleware który wymaga logowania (django-login-required-middleware)

- logowanie na różne role i poziomy, wymusza konkretne uprawienia.

- rozwijane menu językowe

- zarządzanie poprzez panel admina django.

- z poziomu super-usera można nadawać dowolne stopnie uprawnień.

- dla poprawienia jakości i przejrzystości kodu zostały użyte dekoratory.

- dzięki django-model translation możliwy jest swobodny wybór języków (domyślny angielski)

- panel tłumacza umożliwia tłumaczenie elementów strony.

- dodawanie i zarządzanie akcjami kwaterunkowymi.

- możliwość zamieszczania ogłoszeń i plików z poziomu admina.

- rozbudowane wielowarstwowe sortowanie akcji kwaterunkowej względem ich statusu/aktualności.

- wyszukiwarka użytkowników z możliwością sortowania.

plany na przyszłość:

- możliwość zmiany skórek

- intuicyjna mapa akademików z rozbudowanym interaktywnym interfejsem graficznym

- obsługa maili przez postfix

- rozbudowany panel tłumacza


Autorzy: Jakub Kozdrowicz & Maciej Fleiszfreser



