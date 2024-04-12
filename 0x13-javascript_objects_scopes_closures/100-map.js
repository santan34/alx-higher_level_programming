#!/usr/bin/node

const list = require('100-data.js').list;
const nlist = list.map((num, i) => num * i);
console.log(list);
console.log(nlist);
