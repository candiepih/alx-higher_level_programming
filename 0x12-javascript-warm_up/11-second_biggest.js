#!/usr/bin/node
const { argv } = require('process');
const newArgv = argv.slice(2, argv.length);

if (argv.length <= 2 || argv.length === 3) {
  console.log(0);
} else {
  newArgv.sort();
  newArgv.reverse();
  console.log(newArgv[1]);
}
