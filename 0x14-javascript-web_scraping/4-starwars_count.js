#!/usr/bin/node
/**
 * Script that prints the number of movies where
 * the character Wedge Antilles is present..
 */

const request = require('request');
const process = require('process');
const apiUrl = process.argv[2];
const characterUrl = 'https://swapi-api.hbtn.io/api/people/18/';

request.get(apiUrl, (err, response, body) => {
  if (err === null) {
    const data = JSON.parse(body);
    let films = data.results;
    films = films.filter(
      film => film.characters.includes(characterUrl)
    );
    console.log(films.length);
  } else {
    console.log(err);
  }
});
