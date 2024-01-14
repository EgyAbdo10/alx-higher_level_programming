#!/usr/bin/node
function factorial (number) {
  if (Number(number) === 0 || isNaN(number)) {
    return (1);
  }
  return (Number(number) * factorial(Number(number) - 1));
}
console.log(factorial(process.argv[2]));
