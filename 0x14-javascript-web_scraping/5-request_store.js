#!/usr/bin/node

const fs = require('node:fs');
const request = require('request');
const args = process.argv;

const url = args[2];
const filePath = args[3];

function saveResponse () {
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
    }
    try {
      fs.writeFileSync(filePath, response.body);
    } catch (err) {
      console.error(err);
    }
  });
}

saveResponse();
