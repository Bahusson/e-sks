
function setCookie(cvalue)
{
  document.cookie = "esks_language = " + cvalue;
}

$(document).ready(function()
{
  $('#langpl').click(function() // Ustaw Język Polski
 {
   setCookie("pl")
  });

  $('#langen').click(function() // Ustaw Język Angielski
 {
    setCookie("en")
  });

  $('#langde').click(function() // Ustaw Język Niemiecki
 {
   setCookie("de")
  });

  $('#langfr').click(function() // Ustaw Język Francuski
 {
   setCookie("fr")
  });

  $('#langru').click(function() // Ustaw Język Rosyjski
 {
    setCookie("ru")
  });

  $('#languk').click(function() // Ustaw Język Ukraiński
 {
   setCookie("uk")
  });

  $('#langes').click(function() // Ustaw Język Hiszpański
 {
    setCookie("es")
  });

  $('#langhi').click(function() // Ustaw Język Hindi
 {
   setCookie("hi")
  });
});
