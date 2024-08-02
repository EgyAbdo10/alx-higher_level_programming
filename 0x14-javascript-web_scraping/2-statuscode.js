#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];

function getData (url) {
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    console.log('code: ' + response.statusCode);
  });
}

getData(url);
