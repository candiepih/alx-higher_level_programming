#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """

import requests


if __name__ == "__main__":
    res = requests.get("https://intranet.hbtn.io/status")
    res = res.text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
