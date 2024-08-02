#!/usr/bin/node

const args = process.argv;
const id = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const request = require('request');
function getMovieName (url) {
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(response.body).title);
    }
  });
}

getMovieName(url);
