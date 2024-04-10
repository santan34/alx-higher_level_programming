#!/usr/bin/node
// second biggest integer from a a list

const num = [];
let j = 0;
for (let i = 2; i < process.argv.length; i++) {
  num[j] = Number(process.argv[i]);
  j++;
}
const secondLargest = function (arr) {
  if (arr.length === 0 || arr.length === 1) {
    return 0;
  }
  return arr.sort()[arr.length - 2];
};

console.log(secondLargest(num));
