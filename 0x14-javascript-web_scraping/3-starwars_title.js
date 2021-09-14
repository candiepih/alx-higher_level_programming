#!/usr/bin/node
/**
 * Script that prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 */

const request = require('request');
const process = require('process');
const episodeNumber = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episodeNumber}`;

request.get(url, (err, response, body) => {
  if (err === null) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log(err);
  }
});
