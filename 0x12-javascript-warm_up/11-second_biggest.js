#!/usr/bin/node
const newArgv = argv.slice(2, argv.length);

if (argv.length <= 3) {
  console.log(0);
} else {
  const { argv } = require('process');
  newArgv.sort();
  newArgv.reverse();
  console.log(newArgv[1]);
}
