#!/usr/bin/node

const args = process.argv;
const fs = require('node:fs');

// const file_content = fs.readFileSync(`${file_name}`, "utf-8")
// console.log(file_content)
const fileName = args[2];
fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
