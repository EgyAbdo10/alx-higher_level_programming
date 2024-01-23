#!/usr/bin/node
exports.converter = function (base) {
  function newBase (num) {
    return (num.toString(base));
  }
  return (newBase);
};
