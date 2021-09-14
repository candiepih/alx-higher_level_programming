#!/usr/bin/node
/**
 * Script that reads and prints the content of a file.
 */

const request = require('request');
const process = require('process');
const url = process.argv[2];

request.get(url, (err, response) => {
  if (err == null) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.log(err);
  }
});
