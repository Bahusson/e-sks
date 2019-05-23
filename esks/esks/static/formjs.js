var unlock
// Dla funkcji są w sumie cztery. Dwie dla elementów posiadających wartość.
// Kwestia zerowania po zmianie zdania.

var radio = function(type)
{
  if (type === "on")
    return function(name) {
      var x = document.getElementById(name);
      x.style.display = "block";
      //x.val("1");
    };
  else if (type === "off")
    return function(name) {
      var x = document.getElementById(name);
      x.style.display = "none";
      //x.val("0");
    };
};


/*function radioon(name)
{
  var x = document.getElementById(name);
  x.style.display = "block";
  //x.val("1");
}

function radiooff(name)
{
  var x = document.getElementById(name);
    x.style.display = "none";
    x.val("0");
} */

// Włącza widok zgody.
function checkboxon()
{
  var x = document.getElementById("#agreecheck");
    x.style.display = "block";
}

// Funkcja ukrywająca i pokazująca przycisk "send"
function togglesend()
{
  var x = document.getElementById("#send");
  if (x.style.display === "none") {
    x.style.display = "block";
  }
  else {
    x.style.display = "none";
  }
}

// Resetuje zgodę po zmianie zdania.
function checkboxoff()
{
   document.getElementById("#checkbox").checked = false;
   document.getElementById("#send").style.display = "none";
   document.getElementById("#agreecheck").style.display = "none";
}

$(document).ready(function()
{
  $('#rad0A').click(function()
 {
    var radioon = radio("on");
    radioon("rad1");
  /*  radiooff("#rad2");
    radiooff("#rad3");
    radiooff("#rad4");
    radiooff("#rad5");
    radiooff("#rad6");
    unlock === True */
  });

  $('#rad0B').click(function()
 {
   var radiooff = radio("off");
   radiooff("rad1");
   /* radioon("#rad2");
   radiooff();
   unlock === False */
  });

});


/* $(document).ready(function(){

          //Na początku wszystkie "radia" mają wartość "0" czyli "nie",
          //aby można było wysłać formularz w różnym formacie.
        $('input[type="radio"]').val("0");

          // Tu się zaczyna drzewko zależności, które dynamicznie odblokowuje poszczególne elementy.

          // Ścieżka decyzyjna 1:
        $('#rad0A').click(function() { //Student Tak
          //checkboxoff();
          radioon("#rad1");
          radiooff("#rad2");
          radiooff("#rad3");
          radiooff("#rad4");
          radiooff("#rad5");
          radiooff("#rad6");
          unlock === True
        });

        $('#rad0B').click(function() { //Student Nie
          //checkboxoff(); // Zresetuj zgody
          radioon("#rad2");
          radiooff("#rad1");
          unlock === False
        });

        $('#rad1A').click(function() { //Obywatelstwo Tak (switch)
          if (unlock === True) {
            chechboxon();
            radiooff("#rad3");
            radiooff("#rad4");
        }
          else {
            checkboxoff();
            radioon("#rad3");
          }
        });

        $('#rad1B').click(function() { //Obywatelstwo Nie (switch)
          if (unlock === True) {
            checkboxon(); // Włącz zgody końcowe
            radiooff("#rad5");
            radiooff("#rad6");
        }
          else {
            checkboxoff(); // Zresetuj zgody
            radioon("#rad5");
          }
        });

        $('#rad2A').click(function() { // Doktorant Tak
          checkboxon(); // Włącz zgody końcowe
          radiooff("#rad1");
          radiooff("#rad3");
          radiooff("#rad4");
        });

        $('#rad2B').click(function() { // Doktorant Nie
          checkboxoff(); // Wyłącz zgody końcowe
          radioon("#rad1");
        });

        $('#rad3A').click(function() { // Zamiar Tak
          checkboxoff();
          radioon("#rad4");
        });

        $('#rad3B').click(function() { // Zamiar Nie
          checkboxon(); // Włącz zgody końcowe
          radiooff("#rad4");
        });

        $('#rad4A').click(function() { // Pierwszy Stopień Tak
          chenameckboxon(); // Włącz zgody końcowe
        });

        $('#rad4B').click(function() { // Pierwszy Stopień Nie
          checkboxon(); // Włącz zgody końcowe
        });

        $('#rad5A').click(function() { // Pelnywymiar Tak
          checkboxon(); // Włącz zgody końcowe
          radiooff("rad6");
        });

        $('#rad5B').click(function() { // Pełnywymiar Nie
          checkboxoff();
          radioon("#rad6");
        });

        $('#rad6A').click(function() { // Erazmus Tak
          checkboxon(); // Włącz zgody końcowe
        });

        $('#rad6B').click(function() { // Erazmus Nie
          checkboxon(); // Włącz zgody końcowe
        });


        $('#checkbox').click(function() {
          togglesend(); // Po zaznaczeniu zgody udostępnij przycisk wyślij.
        });
}); */
