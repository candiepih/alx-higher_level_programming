#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const newArgv = argv.slice(2, argv.length);
  newArgv.sort();
  newArgv.reverse();
  console.log(newArgv[1]);
}
