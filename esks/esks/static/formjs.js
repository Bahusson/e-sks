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
          } else {
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
        $('#rad0A').click(function (e) {  //Student Tak
          e.checkboxoff();
          e.togglevalue("#rad1");
          unlock === True
        });

        $('#rad1A').click(function (e) {  //Obywatelstwo Tak (ze switchem)
          e.checkboxoff();
          if (unlock === True) {
          e.toggleelement("#agreecheck");
        }
          else {
            ////
          }

        });
        $('#rad1B').click(function (e) {  //Obywatelstwo Nie (ze switchem)
          if (unlock === True) {
            e.checkboxon(); // Włącz zgody końcowe
        }
          else {
            e.checkboxoff();
            /////
          }

        });

        $('#rad0B').click(function (e) { //Student Nie
          e.checkboxoff();
          e.radioon("#rad2");
          unlock === False
        });

        $('#rad2A').click(function (e) { //Doktorant Tak
          e.novalon("#agreecheck"); // Włącz zgody końcowe
          e.radiooff("#rad2");
        });

        $('#rad2B').click(function (e) {
          e.checkboxoff();
          e.radioon("#rad2");
        });

        $('#checkbox').click(function (e) {
          e.togglesend() // Po zaznaczeniu zgody udostępnij przycisk wyślij.
        });

});
