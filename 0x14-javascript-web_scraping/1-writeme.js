#!/usr/bin/node

const args = process.argv;
const fs = require('node:fs');

// const file_content = fs.readFileSync(`${file_name}`, "utf-8")
// console.log(file_content)
const fileName = args[2];
const content = args[3];

fs.writeFile(fileName, content, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
