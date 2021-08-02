#!/usr/bin/node
// Write a script that prints a square x times
const args = process.argv;
if (isNaN(parseInt(args[2]))) {
  console.log('Missing size');
} else {
  const num = args[2];
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
