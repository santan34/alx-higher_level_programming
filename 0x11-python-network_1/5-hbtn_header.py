#!/usr/bin/python3
"""requests 1"""

import requests
import sys


def Xrequest(url):
    """the function to gets the x request header"""
    response = requests.get(url)
    data = response.headers.get("X-Request-Id")
    print(data)


if __name__ == "__main__":
    Xrequest(sys.argv[1])
