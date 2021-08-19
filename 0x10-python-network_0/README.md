# Python - Network #0

Aim of this topic was to understand the following concepts:-

* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)

# FILES

The following task files were used to test understanding on various concepts:-

All the bash scripts use curl to perform various tasks

[0-body_size.sh](./0-body_size.sh)

Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

[1-body.sh](./1-body.sh)

Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

[2-delete.sh](./2-delete.sh)

Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

[3-methods.sh](./3-methods.sh)

Bash script that takes in a URL and displays all HTTP methods the server will accept.

[4-header.sh](./4-header.sh)

Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

Requirements:

* A header variable `X-HolbertonSchool-User-Id` must be sent with the value `98`

[5-post_params.sh](./5-post_params.sh)

Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

Requirements:

* A variable `email` must be sent with the value `hr@holbertonschool.com`
* A variable `subject` must be sent with the value `I will always be here for PLD`

[6-peak.py](./6-peak.py)

function that finds `a peak` in a list of unsorted integers.

* Prototype: `def find_peak(list_of_integers):`
* You are not allowed to import any module
* Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
* `6-peak.py` must contain the function
* `6-peak.txt` must contain the complexity of your algorithm: `O(log(n)), O(n), O(nlog(n)) or O(n2)`

Solution details:

One of the ways to find peak in a list would be to sort it, then get the largest item.  
If a list is sorted in ascending order then the peak is the last element. If list is sorted in descending order then the peak is the first element.

Since python's own builtin sort method implements `Timsort` algorithm to perform sort which basically is a hybrid stable sorting algorithm derived from merge sort and insertion sort, we then use the python's sort method to sort the list in descending order and get first item in list at index 0 which will serve as our peak.

This has a time complexity of O(log(n))

Test file: [6-main.py](./6-main.py)

[6-peak.txt](./6-peak.txt) file contains time complexity of finding the peak in a list.

[100-status_code.sh](./100-status_code.sh)

Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

Requirements:

* You are not allowed to use any pipe, redirection, etc.
* You are not allowed to use `;` and `&&`

[101-post_json.sh](./101-post_json.sh)

Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.

Requirements:

* Your script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request

[102-catch_me.sh](./102-catch_me.sh)

Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.

Requirements:

* You are not allow to use `echo`, `cat`, etc. to display the final result
