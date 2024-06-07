#!/usr/bin/python3
# lets do this git
import requests
from sys import argv


def thefunc(repo, name):
    req = requests.get(
        f"https://api.github.com/repos/{name}/{repo}/commits").json()

    try:
        for i in range(10):
            print(f"{req[i].get("sha")}: {req[i].get("commit").get("author").get('name')}")
    except BaseException as e:
        print("error in fetching")
