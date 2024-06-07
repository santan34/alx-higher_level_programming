#!/usr/bin/python3
"""lets do this git"""

import requests
from sys import argv


def thefunc(repo, name):
    req = requests.get(
        f"https://api.github.com/repos/{name}/{repo}/commits").json()

    try:
        for i in range(10):
            j = req[i].get("sha")
            k = req[i].get("commit").get("author").get('name')
            print(f"{j}: {k}")
    except BaseException as e:
        pass


if __name__ == "__main__":
    thefunc(argv[1], argv[2])
