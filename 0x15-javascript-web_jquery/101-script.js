$(function () {
  const list = $('UL.my_list');
  $('DIV#add_item').on('click', () => {
    list.append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', () => {
    $('UL.my_list li').last().remove();
  });
  $('DIV#clear_list').on('click', () => {
    list.empty();
  });
});
