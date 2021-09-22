/**
 * script that adds, removes and clears LI elements
 * from a list when the user clicks
 */
$(document).ready(() => {
  $('DIV#add_item').bind('click', () => {
    const li = $('<li></li>').text('Item');
    $('UL.my_list').append(li);
  });
  $('DIV#remove_item').bind('click', () => {
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').bind('click', () => {
    $('UL.my_list').empty();
  });
});
