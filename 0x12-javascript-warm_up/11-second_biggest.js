#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
const args = process.argv;
if (args.lenght <= 3) {
  console.log(0);
} else {
  args.sort((a, b) => a - b);
  args.pop();
  console.log(args.pop());
}
