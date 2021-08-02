#!/usr/bin/node

/* Write a script that prints two arguments passed to it, in the following format: “ is ” */
const args = process.argv;
if (args <= 2) {
  console.log('undefined is undefined');
} else {
  console.log(args[2] + [' is '] + args[3]);
}
