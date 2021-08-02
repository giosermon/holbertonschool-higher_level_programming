#!/usr/bin/node
//
const args = process.argv;
const num = parseInt(args[2]);
function factorial (x) {
  if (isNaN(x)) { return ('NaN' | 1); }
  if (x <= 1) { return (1); }
  return (x * factorial(x - 1));
}
console.log(factorial(num));
