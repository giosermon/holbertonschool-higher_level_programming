#!/usr/bin/node
// Write a script that prints the addition of 2 integers
function add (a, b) {
  return (a + b);
}
const args = process.argv;
const x = parseInt(args[2]);
const y = parseInt(args[3]);

if (isNaN(parseInt(args[2]))) {
  console.log('NaN');
} else {
  console.log(add(x, y));
}
