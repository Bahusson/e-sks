# E-SKS (Elektroniczny system kwaterunkowy studentów) - THE ELECTRONIC STUDENT ACCOMMODATION SYSTEM.

Technology stack: Python 3.6, Django 2.2, JavaScript, JQuery, CSS3 , Bootstrap 4, HTML5, PostgreSQL.


- application is based on PostgreSQL and on CDN located on DigitalOcean.com.

- special middleware forcing logging into most sites (django-login-requiredmiddleware).

- logging into different roles and levels enforces specific permissions -  esks/special/decorators.py

- language drop-down menu after selecting a language changes language (cookie)

- management via admin panel

- level 2+ users can grant and revoke privileges for users from lower levels

- Tłumaczenie strony za pomocą django-model-translation tool.

- website translation using the djangomodel-translation tool

- separate translator panel

- sorted user search engine

--------------------------------------------------

- aplikacja jest oparta na PostgreSQL, oraz na CDN umieszczonym na DigitalOcean.com
- specjalny middleware wymuszający logowanie na większość serwisu (djangologin-required-middleware)
- logowanie na różne role i poziomy, wymusza konkretne uprawienia
- rozwijane menu językowe po wybraniu języka zmienia ciastko językowe (cookie).
- zarządzanie poprzez panel admina użytkownik poziomu 2+ może nadawać i odbierać uprawnienia użytkownikom zniższych poziomów.
- tłumaczenie strony za pomocą djangomodel-translation tool.
- oddzielny panel tłumacza możliwość zamieszczania ogłoszeń i plików z poziomu użytkownika lvl 2+
- rozbudowane wielowarstwowe sortowanie akcji kwaterunkowej, oraz użytkowników systemu
- wyszukiwarka użytkowników z sortowaniem


Jakub Kozdrowicz & Maciej Fleiszfreser 2019
