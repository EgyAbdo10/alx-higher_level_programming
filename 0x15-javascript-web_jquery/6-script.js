const element = $('DIV#update_header');
const header = $('header');

element.on('click', () => {
    header.text("New Header!!!");
});
