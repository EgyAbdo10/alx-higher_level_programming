$(function () {
  // let lang = $("INPUT#language_code").val();

  $('INPUT#language_code').on('keydown', (event) => {
    if (event.key == 'Enter') {
      const lang = $('INPUT#language_code').val();
      $.ajax({
        type: 'GET',
        url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
        success: (data) => {
          $('DIV#hello').text(`${data.hello}`);
        }
      });
    }
  });

  $('INPUT#btn_translate').on('click', () => {
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      success: (data) => {
        $('DIV#hello').text(`${data.hello}`);
      }
    });
  });
});
