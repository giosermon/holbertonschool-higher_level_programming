#!/usr/bin/node
//
const _Square = require('./5-square.js');
module.exports = class Square extends _Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let j = 0; j < this.width; j++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
