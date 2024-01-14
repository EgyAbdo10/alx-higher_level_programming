#!/usr/bin/node
const newModule = require('node:process');
const args = newModule.argv;
switch (args.length) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
    break;
}
