#!/usr/bin/node
//
const args = process.argv;
if (isNaN(parseInt(args[2]))) {
  console.log('Missing number of ocurrences');
} else {
  const num = args[2];
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
