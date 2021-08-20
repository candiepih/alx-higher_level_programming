#!/usr/bin/python3
""" script that takes 2 arguments in order to solve this challenge."""

import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)
    res = requests.get(url)
    json = res.json()
    for i, v in enumerate(json):
        if i >= 10:
            break
        sha = v.get('sha')
        author = v.get('author').get('login')
        print("{}: {}".format(sha, author))
