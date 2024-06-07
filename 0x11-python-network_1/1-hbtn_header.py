#!/usr/bin/python3
"""url lib 1"""

import sys
import urllib.request


def Xrequest(url):
    """the function to gets the x request header"""
    with urllib.request.urlopen(url) as response:
        data = response.getheader("X-Request-Id")
    print(data)


if __name__ == "__main__":
    Xrequest(sys.argv[1])
