#!/usr/bin/node
exports.esrever = function (list) {
  const length = list.length;
  const arey = [];
  for (let i = 0; i < length; i++) {
    arey[i] = list[length - (1 + i)];
  }
  return arey;
};
