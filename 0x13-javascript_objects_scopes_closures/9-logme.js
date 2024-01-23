#!/usr/bin/node
let co = 0;
exports.logMe = function (item) {
  console.log(`${co}: ${item}`);
  co++;
};
