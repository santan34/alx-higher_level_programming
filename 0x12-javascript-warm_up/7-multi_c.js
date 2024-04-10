#!/usr/bin/node
// a script that prints x times “C is fun”

const x = Number(process.argv[2]);
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
