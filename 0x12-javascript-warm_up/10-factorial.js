#!/usr/bin/node
// computes a factorial

function factorial (n) {
  if (n === 0) {
    return (1);
  }
  if (n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

const n = Number(process.argv[2]);
if (!Number(process.argv[2])) {
  console.log('1');
} else {
  console.log(factorial(n));
}
