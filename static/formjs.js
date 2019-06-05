var unlock

//Przełącznik elementów typu radiowego.

var radio = function(type)
{
  if (type === "on")
    return function(name) {
      var x = document.getElementById(name);
      x.style.display = "block";
    };
  else if (type === "off")
    return function(name) {
      var x = document.getElementById(name);
      x.style.display = "none";
    };
};

var radioon = radio("on");
var radiooff = radio("off");

// Włącza widok zgody.
function checkboxon()
{
  var x = document.getElementById("agreecheck");
    x.style.display = "block";
}

// Funkcja ukrywająca i pokazująca przycisk "send"
function togglesend()
{
  var x = document.getElementById("send");
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
   document.getElementById("checkbox").checked = false;
   document.getElementById("send").style.display = "none";
   document.getElementById("agreecheck").style.display = "none";
}

// Na spokojnie przesuwa stronę na sam dół.
function hop()
{
  var WH = $(window).height();
  var SH = $('body').prop("scrollHeight");
  $('html, body').stop().animate({scrollTop: SH-WH}, 1000);
}

// Tutaj zaczyna się programowanie przycisków

$(document).ready(function()
{
  $('#rad0A').click(function() // Student Tak
 {
    checkboxoff();
    radioon("rad1");
    radiooff("rad2");
    radiooff("rad3");
    radiooff("rad4");
    radiooff("rad5");
    radiooff("rad6");
    hop();
    unlock = true;
  });

  $('#rad0B').click(function() // Student Nie
 {
   checkboxoff();
   radiooff("rad1");
   radioon("rad2");
   hop();
   unlock = false;
  });

  $('#rad1A').click(function() // Obywatelstwo Tak (switch)
 {
   if (unlock === true)
   {
     checkboxon();
     radiooff("rad3");
     radiooff("rad4");
     hop();
   }
   else
   {
     checkboxoff();
     radioon("rad3");
     radiooff("rad5");
     radiooff("rad6");
     hop();
   }
  });

  $('#rad1B').click(function() // Obywatelstwo Nie (switch)
 {
   if (unlock === true)
   {
     checkboxon();
     radiooff("rad5");
     radiooff("rad6");
     hop();
   }
   else
   {
     checkboxoff();
     radioon("rad5");
     radiooff("rad3");
     hop();
   }
  });

  $('#rad2A').click(function() // Doktorant Tak
 {
   checkboxon();
   radiooff("rad1");
   radiooff("rad3");
   radiooff("rad4");
   hop();
  });

  $('#rad2B').click(function() // Doktorant Nie
 {
   checkboxoff();
   radioon("rad1");
   hop();
  });

  $('#rad3A').click(function() // Zamiar Tak
 {
   checkboxoff();
   radioon("rad4");
   hop();
  });

  $('#rad3B').click(function() // Zamiar Nie
 {
   checkboxon();
   radiooff("rad4");
   hop();
  });

  $('#rad4A').click(function() // Pierwszy stopień Tak
 {
   checkboxon();
   hop();
  });

  $('#rad4B').click(function() // Pierwszy stopień Nie
 {
   checkboxon();
   hop();
  });

  $('#rad5A').click(function() // Pierwszy stopień Nie
 {
   checkboxon();
   radiooff("rad6");
   hop();
  });

  $('#rad5B').click(function() // Pierwszy stopień Nie
 {
   checkboxoff();
   radioon("rad6");
   hop();
  });

  $('#rad6A').click(function() // Erazmus Tak
 {
   checkboxon();
   hop();
  });

  $('#rad6B').click(function() // Erazmus Nie
 {
   checkboxon();
   hop();
  });

  $('#checkbox').click(function() // Po zaznaczeniu zgody udostępnij przycisk wyślij.
  {
    togglesend();
    hop();
  });

});
