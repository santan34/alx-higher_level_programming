#!/usr/bin/python3
"""request 3"""

import requests
import sys


def reqmail(url):
    """the function reqs a url handles errors"""
    try:
        req = requests.get(url)
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    reqmail(sys.argv[1])
