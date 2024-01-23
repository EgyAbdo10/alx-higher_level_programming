#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  const len = list.length;
  for (let i = 0; i < len; i++) {
    arr.push(list.splice(-1)[0]);
  }
  return arr;
};
