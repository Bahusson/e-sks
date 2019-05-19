$(document).ready(function(){

        // Funkcja ukrywająca i pokazująca element oraz zmieniająca jego Wartość na 0
        // w razie zmiany decyzji powodującej schowanie elementu, żeby nie było dziwnych akcji.
        function togglevalue(name) {
          var x = document.getElementById(name);
          if (x.style.display === "none") {
            x.style.display = "block";
          } else {
            x.style.display = "none";
          }
          if (x.style.display === "none") {
            x.val("0");
          }
        }
        // Funkcja po prostu ukrywa i pokazuje element.
        // Nie zmienia wartości, żeby nie było niepotrzebnego błędu.
        function toggleelement(name) {
          var x = document.getElementById(name);
          if (x.style.display === "none") {
            x.style.display = "block";
          } else {
            x.style.display = "none";
          }
        }
          //Na początku wszystkie "radia" mają wartość "0" czyli "nie",
          //aby można było wysłać formularz w różnym formacie.
        $('input[type="radio"]').val("0");

          // Tu się zaczyna drzewko zależności, które dynamicznie odblokowuje poszczególne elementy.

          // Ścieżka decyzyjna 1:
        $('#rad0A').click(function (e) {  //Student
          e.togglevalue("#rad1");
          var unlock === True
        });

        $('#rad1A').click(function (e) {  //Obywatelstwo
          if (unlock === True) {
          e.toggleelement("#agreecheck");
        }
          else {
            ////
          }

        });
        $('#rad1B').click(function (e) {  //Obywatelstwo
          if (unlock === True) {
          e.toggleelement("#agreecheck");
        }
          else {
            /////
          }

        });

        $('#rad0B').click(function (e) {
          e.togglevalue("#rad2");
          var unlock === False
        });

        $('#rad2AB').click(function (e) {
          e.togglevalue("#rad2");
        });

        $('#rad2B').click(function (e) {
          e.togglevalue("#rad2");
          var unlock === False
        });

        $('#checkbox').click(function (e) {
          e.toggleelement("#send")
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
