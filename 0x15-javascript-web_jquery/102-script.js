$(function () {
  // let lang = $("INPUT#language_code").val();
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
