#!/usr/bin/node
/*  Script that prints a message depending of the number of arguments passed */
const args = process.argv.length;
if (args <= 2) {
  console.log('No argument');
} 
if (args === 3) {
  console.log('Argument found');
}
else if (args > 3) {
  console.log('Arguments found');
}
