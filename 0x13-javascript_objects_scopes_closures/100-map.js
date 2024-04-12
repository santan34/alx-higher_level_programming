#!/usr/bin/node

const list = require('100-data.js').list;
let nlist = list.map((num, i) => num * i );
console.log(list);
console.log(nlist);
