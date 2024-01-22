#!/usr/bin/node
const oldSquare = require('./5-square');

module.exports = class Square extends oldSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
};
