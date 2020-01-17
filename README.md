# E-SKS (Elektroniczny system kwaterunkowy studentów) - Aplikacja kwaterunkowa dla domów studenckich PW.

Technologie: Python 3.6, Django 2.2, JavaScript, JQuery, CSS3 ,Bootstrap 4, HTML5, PostgreSQL.

adres strony: http://esks.pl/

Dostęp do funkcjonalności z poziomu administratora:

admin: cadmin@pw.edu.pl

password: Politechnika_1!

funkcjonalności:

- Aplikacja jest oparta na PostgreSQL, oraz na CDN umieszczonym na DigitalOcean.com (programowanie identyczne jak Amazon AWS).

- Specjalny middleware wymuszający logowanie na większość serwisu (django-login-required-middleware) - patrz: settings.py.

- Logowanie na różne role i poziomy, wymusza konkretne uprawienia - patrz: esks/special/decorators.py

- Rozwijane menu językowe po wybraniu języka zmienia ciastko językowe (cookie), które z kolei ustala użytkownikowi jego wersję strony. W przeciwnym wypadku system próbuje ustalić język domyślny z jego języka przeglądarki.

- Zarządzanie poprzez spersonalizawany panel admina (domyślny panel django pozostawiony jeszcze w celach serwisowych - docelowo do usunięcia).

- Użytkownik poziomu 2+ może nadawać i odbierać uprawnienia użytkownikom z niższych poziomów.

- Tłumaczenie strony za pomocą django-model-translation tool.

- Oddzielny panel tłumacza (funkcjonalność zapożyczona z oryginalnego SEKS3 i usprawniona podobnie do tłumacza AMARA)

- Dodawanie i zarządzanie akcjami kwaterunkowymi (oś aplikacji) w formie modułowej - użytkownik składa formularze jak klocki lego, co potem jest odzwierciedlone na wszystkich kolejnych widokach.

- Możliwość zamieszczania ogłoszeń i plików z poziomu użytkownika lvl 2+.

- Rozbudowane wielowarstwowe sortowanie akcji kwaterunkowej, oraz użytkowników systemu.

- Wyszukiwarka użytkowników z sortowaniem (eksperymentalna)

plany na przyszłość:

- Możliwość wgrywania i zmiany skórek. User widzi tylko tę którą sam wybrał (cookie lub atrybut w db). Tryb nocny dla lepszej widoczności.

- Intuicyjna mapa akademików z rozbudowanym interaktywnym interfejsem graficznym

- Obsługa maili przez postfix lub serwer poczty na rzecz klienta (z rekomendowaniem pierwszego rozwiązania).

- Cała strona dostępna do tłumaczenia w panelu

(...)


Autorzy: Jakub Kozdrowicz & Maciej Fleiszfreser
