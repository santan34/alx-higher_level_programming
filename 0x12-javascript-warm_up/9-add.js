#!/usr/bin/node

const sum = Number(process.argv[2] + process.argv[3]);
if (!Number(sum)) {
  console.log('NaN');
} else {
  console.log(sum);
}
