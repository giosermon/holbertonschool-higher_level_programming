#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
const args = process.argv;
if (args <= 3) {
  console.log(0);
} else {
  const list = args.sort();
  console.log(list.reverse()[1]);
}
