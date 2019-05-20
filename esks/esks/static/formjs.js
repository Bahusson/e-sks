$(document).ready(function(){
        var unlock
        // Dla funkcji są w sumie cztery. Dwie dla elementów posiadających wartość.
        // Kwestia zerowania po zmianie zdania.
        function radioon(name) {
          var x = document.getElementById(name);
            x.style.display = "block";
            x.val("1");
        }

        function radiooff(name) {
          var x = document.getElementById(name);
            x.style.display = "none";
            x.val("0");
        }

        // Włącza widok zgody.
        function checkboxon() {
          var x = document.getElementById("#agreecheck");
            x.style.display = "block";
        }

        // Funkcja ukrywająca i pokazująca przycisk "send"
        function togglesend() {
          var x = document.getElementById("#send");
          if (x.style.display === "none") {
            x.style.display = "block";
          }
          else {
            x.style.display = "none";
          }
        }

        // Resetuje zgodę po zmianie zdania.
        function checkboxoff() {
           document.getElementById("#checkbox").checked = false;
           document.getElementById("#send").style.display = "none";
           document.getElementById("#agreecheck").style.display = "none";
        }

          //Na początku wszystkie "radia" mają wartość "0" czyli "nie",
          //aby można było wysłać formularz w różnym formacie.
        $('input[type="radio"]').val("0");

          // Tu się zaczyna drzewko zależności, które dynamicznie odblokowuje poszczególne elementy.

          // Ścieżka decyzyjna 1:
        $('#rad0A').click(function (e) { //Student Tak
          e.checkboxoff()
          e.radioon("#rad1");
          e.rafiooff("#rad2");
          e.rafiooff("#rad3");
          e.rafiooff("#rad4");
          e.rafiooff("#rad5");
          e.rafiooff("#rad6");
          unlock === True
        });

        $('#rad0B').click(function (e) { //Student Nie
          e.checkboxoff(); // Zresetuj zgody
          e.radioon("#rad2");
          e.radiooff("#rad1");
          unlock === False
        });

        $('#rad1A').click(function (e) { //Obywatelstwo Tak (switch)
          if (unlock === True) {
            e.chechboxon();
            e.radiooff("#rad3");
            e.radiooff("#rad4");
        }
          else {
            e.checkboxoff();
            e.radioon("#rad3");
          }
        });

        $('#rad1B').click(function (e) { //Obywatelstwo Nie (switch)
          if (unlock === True) {
            e.checkboxon(); // Włącz zgody końcowe
            e.radiooff("#rad5");
            e.radiooff("#rad6");
        }
          else {
            e.checkboxoff(); // Zresetuj zgody
            e.radioon("#rad5");
          }
        });

        $('#rad2A').click(function (e) { // Doktorant Tak
          e.checkboxon(); // Włącz zgody końcowe
          e.radiooff("#rad1");
          e.radiooff("#rad3");
          e.radiooff("#rad4");
        });

        $('#rad2B').click(function (e) { // Doktorant Nie
          e.checkboxoff(); // Wyłącz zgody końcowe
          e.radioon("#rad1");
        });

        $('#rad3A').click(function (e) { // Zamiar Tak
          e.checkboxoff();
          e.radioon("#rad4");
        });

        $('#rad3B').click(function (e) { // Zamiar Nie
          e.checkboxon(); // Włącz zgody końcowe
          e.radiooff("#rad4");
        });

        $('#rad4A').click(function (e) { // Pierwszy Stopień Tak
          e.checkboxon(); // Włącz zgody końcowe
        });

        $('#rad4B').click(function (e) { // Pierwszy Stopień Nie
          e.checkboxon(); // Włącz zgody końcowe
        });

        $('#rad5A').click(function (e) { // Pelnywymiar Tak
          e.checkboxon(); // Włącz zgody końcowe
          e.radiooff("rad6");
        });

        $('#rad5B').click(function (e) { // Pełnywymiar Nie
          e.checkboxoff();
          e.radioon("#rad6");
        });

        $('#rad6A').click(function (e) { // Erazmus Tak
          e.checkboxon(); // Włącz zgody końcowe
        });

        $('#rad6B').click(function (e) { // Erazmus Nie
          e.checkboxon(); // Włącz zgody końcowe
        });


        $('#checkbox').click(function (e) {
          e.togglesend(); // Po zaznaczeniu zgody udostępnij przycisk wyślij.
        });

        console.log()
});
