#!/usr/bin/python3
""" Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to
    display your id
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)
    res = requests.get(url).json()
    for i in range(0, 10):
        sha = res[i].get('sha')
        author = res[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
