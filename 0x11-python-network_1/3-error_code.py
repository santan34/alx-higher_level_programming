#!/usr/bin/python3
"""url lib 3"""

import sys
import urllib.error
import urllib.request


def reqmail(url):
    """the function reqs a url handles errors"""
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            page = response.read().decode('utf-8')
            print(page)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    reqmail(sys.argv[1])
