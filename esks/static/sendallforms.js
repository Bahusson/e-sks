// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function allformssend(num)
{
  //alert("Hello! I am an alert box!!");
  var x = document.getElementsByClassName(num);
  x[0].submit();
}

$(document).ready(function()
{
  $('#sendtrans').click(function()
 {
  allformssend('serialform0');
  allformssend('serialform1');
 });
});
