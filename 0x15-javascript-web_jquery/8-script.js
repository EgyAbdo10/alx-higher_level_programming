const element = $('UL#list_movies');

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (data) => {
      $.each(data.results, (idx, rec) => {
        element.append(`<li>${rec.title}</li>`);
      });
    }
  });
});
