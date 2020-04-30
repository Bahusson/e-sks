# E-SKS (Elektroniczny system kwaterunkowy studentów) - THE ELECTRONIC STUDENT ACCOMMODATION SYSTEM.

Technology stack: Python 3.6, Django 2.2, JavaScript, JQuery, CSS3 , Bootstrap 4, HTML5, PostgreSQL.

funkcjonalności:

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


Jakub Kozdrowicz & Maciej Fleiszfreser 2019
