const element = $('DIV#toggle_header');
const header = $('header');

element.on('click', () => {
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.removeClass('green');
    header.addClass('red');
  }
});
