#!/bin/bash
# script that takes in a URL, sends a POST request to the
# passed URL, and displays the body of the response

email_value='hr@holbertonschool.com'
subject_value='I will always be here for PLD'

curl -s -d "email=$email_value&subject=$subject_value" -H "Content-Type: application/x-www-form-urlencoded" -X POST "$1"
