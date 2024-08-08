const element = $('DIV#add_item');
const list = $('UL.my_list');

element.on('click', () => {
  list.append('<li>Item</li>');
});
