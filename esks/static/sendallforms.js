// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function allformssend()
{
  var x = document.getElementsByClassName("serialform");
  x.submit()
}

$(document).ready(function()
{
  $('#sendtrans').click(function()
 {
  allformssend()
  });
});
