#!/usr/bin/node
module.exports = function (list, searchElement) {
  let co = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      co++;
    }
  }
  return (co);
};
