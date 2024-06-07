#!/usr/bin/python3
"""url lib 2"""

import sys
import urllib.parse
import urllib.request


def postmail(url, mail):
    """the function tpost an emaol i think"""
    val = {'email': mail}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read().decode('utf-8')
    print(page)


if __name__ == "__main__":
    postmail(sys.argv[1], sys.argv[2])
