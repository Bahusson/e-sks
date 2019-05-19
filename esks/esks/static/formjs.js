$(document).ready(function(){

        // Funkcja ukrywająca i pokazująca element oraz zmieniająca jego Wartość na 0
        // w razie zmiany decyzji powodującej schowanie elementu, żeby nie było dziwnych akcji.
        // Dla checkboxa to jedna funkcja bo śledzimy jeden element.
        function checkbox(name) {
          var x = document.getElementById(name);
          if (x.style.display === "none") {
            x.style.display = "block";
          } else {
            x.style.display = "none";
          }
        }
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

        // I dwie dla niepisoadających wartości. Aby uniknąć błędów.
        function novalon(name) {
          var x = document.getElementById(name);
            x.style.display = "block";
        }

        function novaloff(name) {
          var x = document.getElementById(name);
            x.style.display = "none";
        }

          //Na początku wszystkie "radia" mają wartość "0" czyli "nie",
          //aby można było wysłać formularz w różnym formacie.
        $('input[type="radio"]').val("0");

          // Tu się zaczyna drzewko zależności, które dynamicznie odblokowuje poszczególne elementy.

          // Ścieżka decyzyjna 1:
        $('#rad0A').click(function (e) {  //Student Tak
          e.togglevalue("#rad1");
          var window.unlock === True
        });

        $('#rad1A').click(function (e) {  //Obywatelstwo Tak (ze switchem)
          if (unlock === True) {
          e.toggleelement("#agreecheck");
        }
          else {
            ////
          }

        });
        $('#rad1B').click(function (e) {  //Obywatelstwo Nie (ze switchem)
          if (unlock === True) {
          e.novalon("#agreecheck"); // Włącz zgody końcowe
        }
          else {
            /////
          }

        });

        $('#rad0B').click(function (e) { //Student Nie
          e.togglevalue("#rad2");
          var window.unlock === False
        });

        $('#rad2A').click(function (e) { //Doktorant Tak
          e.novalon("#agreecheck"); // Włącz zgody końcowe
          e.togglenull("#rad2")
        });

        $('#rad2B').click(function (e) {
          e.togglevalue("#rad2");
          e.
        });

        $('#checkbox').click(function (e) {
          e.checkbox("#send") // Po zaznaczeniu zgody udostępnij przycisk wyślij.
        });

        //## Od tego momentu jest stary kod do poprawy.
        //## Czy chcę, aby mi się wizualizowała akcja przed wysłaniem?

        $('#generate').click(function(e) {
          e.preventDefault()

           $.ajax({
                    url: "/lotto/generate/",
                    type: "POST",
                    data: {
/*Numer gry*/         gamesel:$('input:radio[name=gamesel]:checked').val(),
/*Data Od:*/          datefrom:$("#date1").val(),
/*Data Do:*/          dateto:$("#date2").val(),
/*Cała baza*/         dateall:$("#checkboxG1").val(),
/*Skrajne numery*/    numhilow:$("#checkboxG2").val(),
/*Pomiń losowania*/   norolls:$("#checkboxG3").val(),
/*Skrajne numery*/    mostoften:$("#numinput").val(),
/*Średnie wyników*/   avgscores:$("#checkboxG4").val(),
/*Generuj wykres*/    graphgen:$("#checkboxG5").val(), /*Ten można by alternatywnie zrobic jako button z oddzielną funkcją*/
                      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                          },
                    success:function(data){
                //    var jdata = data['hilow','often',"avgsc","rolls"];
                  //  var finaldata = jdata.join("\n\n");
                    $('#textarea1').val(data['hilow'] + "\n\n" + data['often'] + "\n\n" + data['avgsc'] + "\n\n" + data['rolls']);
                    console.log(data)
                                      }
                  });
        });
});
