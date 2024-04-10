#!/usr/bin/node
// add me maybe

exports.addMeMaybe = function (number, theFunction) {
  const newVal = number + 1;
  theFunction(newVal);
};
