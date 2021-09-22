# JavaScript - Web jQuery

Aim of this topic is to understand the following concepts:-

* Why JQuery make front-end programming so easy
* How to select HTML elements in JavaScript
* How to select HTML elements with JQuery
* What are differences between ID, class and tag name selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a GET request with JQuery Ajax
* How to make a POST request with JQuery Ajax
* How to listen/bind to DOM events
* How to listen/bind to user events

# Files

The following task files are used to test understanding on the various topic concepts

[0-script.js](./0-script.js)

JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`)

Requirements:-

* You must use document.querySelector to select the HTML tag

[1-script.js](./1-script.js)

JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`)

Requirements:

* You must use the JQuery API

[2-script.js](./2-script.js)

JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`

Requirements:

* You must use the JQuery API

[3-script.js](./3-script.js)

JavaScript script that adds the class red to the `<header>` element when the user clicks on the tag `DIV#red_header`

Requirements:

* You must use the JQuery API

[4-script.js](./4-script.js)

JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`

Requirements:

* You must use the JQuery API
* The `<header>` element must always have one class: red or green, never both in the same time and never empty.
* If the current class is red, when the user click on `DIV#toggle_header`, the class must be updated to green; and the reverse.
* You must use the JQuery API

[5-script.js](./5-script.js)

JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`

Requirements:-

* The new element must be: `<li>Item</li>`
* The new element must be added to `UL.my_list`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API

[6-script.js](./6-script.js)

JavaScript script that updates the text of the `<header>` element to New Header!!! when the user clicks on `DIV#update_header`

Requirements:

* You must use the JQuery API

[7-script.js](./7-script.js)

JavaScript script that fetches the character name from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

Requirements:

* You must use the JQuery API
* The name must be displayed in the HTML tag `DIV#character`

[8-script.js](./8-script.js)

JavaScript script that fetches and lists the title for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

Requirements:

* You must use the JQuery API
* All movie titles must be list in the HTML tag `UL#list_movies`

[9-script.js](./9-script.js)

JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag `DIV#hello`.

Requirements:

* You must use the JQuery API
* The translation of “hello” must be displayed in the HTML tag `DIV#hello`
* Script must work when it is imported from the `<head>` tag

[100-script.js](./100-script.js)

JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`)

Requirements:

* You must use the JQuery API
* Script must be imported from the `<head>` tag, not at the end of the HTML

[101-script.js](./101-script.js)

JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks

Requirements:

* You must use the JQuery API
* The new element must be: `<li>Item</li>`
* The new element must be added to `UL.my_list`
* When the user clicks on `DIV#add_item`: a new element is added to the list
* When the user clicks on `DIV#remove_item`: the last element is removed from the list
* When the user clicks on `DIV#clear_list`: all elements of the list are removed
* Script must work when it imported from the `HEAD` tag

[102-script.js](./102-script.js)

JavaScript script that fetches and prints how to say “Hello” depending on the language

Requirements:

* You must use the JQuery API
* You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
* The language code will be the value entered in the tag `INPUT#language_code` (`ex: es, fr, en etc.`)
* The translation must be fetched when the user clicks on `INPUT#btn_translate`
* The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
* Script must work when it imported from the `HEAD` tag

[103-script.js](./103-script.js)

JavaScript script that fetches and prints how to say “Hello” depending on the language

* You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
* The language code will be the value entered in the tag `INPUT#language_code` (ex: `es, fr, en etc`.)
* The translation must be fetched when the user clicks on `INPUT#btn_translate`
* The translation of “Hello” must be displayed in the `HTML` tag `DIV#hello`
* You can’t use `document.querySelector` to select the `HTML` tag
* You must use the JQuery API
