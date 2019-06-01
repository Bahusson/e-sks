
function setCookie(cvalue)
{
  document.cookie = "esks_language = " + cvalue;
}

$(document).ready(function()
{
  $('#pl').click(function() // Ustaw Język Polski
 {
   setCookie("pl")
  });

  $('#en').click(function() // Ustaw Język Angielski
 {
    setCookie("en")
  });

  $('#de').click(function() // Ustaw Język Niemiecki
 {
   setCookie("de")
  });

  $('#fr').click(function() // Ustaw Język Francuski
 {
   setCookie("fr")
  });

  $('#ru').click(function() // Ustaw Język Rosyjski
 {
    setCookie("ru")
  });

  $('#uk').click(function() // Ustaw Język Ukraiński
 {
   setCookie("uk")
  });

  $('#es').click(function() // Ustaw Język Hiszpański
 {
    setCookie("es")
  });

  $('#hi').click(function() // Ustaw Język Hindi
 {
   setCookie("hi")
  });
});
