# JavaScript - Web scraping

This project aim was to understand the following concepts:-

* How to manipulate JSON data
* How to use `request` and fetch API
* How to read and write a file using `fs` module

# File

The following task files were used to help the above concepts:-

[0-readme.js](./0-readme.js)

Script that reads and prints the content of a file.

Requirements:-

* The first argument is the file path
* The content of the file must be read in `utf-8`
* If an error occurred during the reading, print the error object

[1-writeme.js](./1-writeme.js)

Script that writes a string to a file.

Requirements:-

* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in `utf-8`
* If an error occurred during while writing, print the error object

[2-statuscode.js](./2-statuscode.js)

Script that display the status code of a `GET` request.

Requirements:-

* The first argument is the URL to request (`GET`)
The status code must be printed like this: `code: <status code>`
You must use the module `request`

[3-starwars_title.js](./3-starwars_title.js)

Script that prints the title of a Star Wars movie where the episode number matches a given integer.

Requirements:-

* The first argument is the movie ID
* You must use the `[Star wars API](https://swapi-api.hbtn.io/)` with the endpoint `https://swapi-api.hbtn.io/api/films/:id`
* You must use the module `request`

[4-starwars_count.js](./4-starwars_count.js)

Script that prints the number of movies where the character “Wedge Antilles” is present.

Requirements:-

* The first argument is the API URL of the `[Star wars API](https://swapi-api.hbtn.io/)`: `https://swapi-api.hbtn.io/api/films/`
* Wedge Antilles is character ID `18` - your script must use this ID for filtering the result of the API
* You must use the module `request`
