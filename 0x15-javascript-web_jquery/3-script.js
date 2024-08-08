const element = $('DIV#red_header');
const header = $('header');

element.on('click', () => {
  header.addClass('red');
});
