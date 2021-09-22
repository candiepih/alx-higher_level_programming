/**
 * script that toggles the class of the <header>
 * element when the user clicks on the tag DIV#toggle_header
 */
$('DIV#toggle_header').bind('click', () => {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red').addClass('green');
  } else {
    $('header').removeClass('green').addClass('red');
  }
});
