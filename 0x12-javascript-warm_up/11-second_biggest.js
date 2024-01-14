#!/usr/bin/node
function secondBiggestNum (arr) {
  if (arr.length < 2) {
    return (0);
  }
  arr = arr.map(item => Number(item));
  const arrMax = Math.max(...arr);
  const arrMaxIdx = arr.indexOf(arrMax);
  arr.splice(arrMaxIdx, 1);
  return (Math.max(...arr));
}
console.log(secondBiggestNum(process.argv.slice(2)));
