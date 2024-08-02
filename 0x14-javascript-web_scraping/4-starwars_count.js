#!/usr/bin/node

const request = require('request');
//     "characters": [
// "https://swapi-api.alx-tools.com/api/people/1/",
function getMoviesChar (callback) {
  let numOccerances = 0;
  const url = 'https://swapi-api.alx-tools.com/api/films/1';
  const charRecord = 'https://swapi-api.alx-tools.com/api/people/18/';
  let id = 1;
  function requestNext (url) {
    request(url, (err, response, body) => {
      if (err) {
        console.log(err, 0);
        return;
      }
      if (response.statusCode === 404) {
        callback(null, numOccerances);
      } else {
        const data = JSON.parse(body);
        if (data.characters.includes(charRecord)) {
          numOccerances += 1;
        }
        id += 1;
        url = `https://swapi-api.alx-tools.com/api/films/${id}/`;
        requestNext(url);
      }
    });
  }
  requestNext(url);
}

getMoviesChar((err, numOccerances) => {
  if (err) {
    console.log('error: ' + err);
  } else {
    console.log(numOccerances);
  }
});
