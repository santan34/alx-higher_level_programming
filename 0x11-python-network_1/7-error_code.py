#!/usr/bin/python3
"""request 3"""

import requests
import sys


def reqmail(url):
    """the function reqs a url handles errors"""
    req = requests.get(url)
    if req.status_code > 399:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)


if __name__ == "__main__":
    reqmail(sys.argv[1])
