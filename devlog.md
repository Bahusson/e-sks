# Devlog projektu E-SKS.
#
# 05.06.2019 - Jakub
# 0. Wrzucenie na serwer testowy wersji demo minimum pod PostgreSQL,
#    do testów i prezentacji. Demo zawiera:
#       a.) Podstawową funkcję responsywnego layoutu strony pod Bootstrap 4.
#       bi.) Automatyczne wykrywanie języka przeglądarki dla tłumaczenia strony.
#       bii.) Dodatek Django-modeltranslation służący do tłumaczenia strony.
#       biii.) Nakładkę JS umożliwiającą ręczne zmienianie języka tłumaczenia.
#       c.) Interaktywny formularz switchowy pod JS przydzielający akcję
#           kwaterunkową.
#
# 09.07.2019 - Jakub
# 1. Update wersji o panel admina i poziomy dostępów:
#       a.) Tworzenie grup o różnych poziomach dostępu do treści.
#       b.) Podstawowy User z przydzieloną akcją kwaterunkową.
#       c.) Dodano Sesje i testujemy CACHE bazodanowy.
#       d.) Fix problemu z Nginx PID po aktualizacji systemu.
#
* Pracuję jeszcze nad specjalnym uprawieniem dla opiekuna grupy pt. "dodaj do grupy adminów", więc jeśli ktoś się już zarejestrował a nie dostał jeszcze uprawnień a chce testować panel administracji Rady, to roboczy użytkownik ma Login: Cadmin i hasło: Passwd1234!.
