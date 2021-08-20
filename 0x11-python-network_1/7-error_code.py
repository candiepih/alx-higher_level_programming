#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """

import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    code = res.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(res.text)
