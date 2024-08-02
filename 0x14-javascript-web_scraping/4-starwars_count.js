#!/usr/bin/node

const request = require('request');
//     "characters": [
// "https://swapi-api.alx-tools.com/api/people/1/",
function getMoviesChar () {
  const url = process.argv[2];
  const charRecord = 'https://swapi-api.alx-tools.com/api/people/18/';
  let numOcc = 0;
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
    }
    try {
      const results = JSON.parse(response.body).results;
      results.forEach((record) => {
        if (record.characters.includes(charRecord)) {
          numOcc += 1;
        }
      }
      );
      console.log(numOcc);
    } catch (parseError) {
      console.error(parseError);
    }
  });
}
getMoviesChar();
