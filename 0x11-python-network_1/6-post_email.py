#!/usr/bin/python3
"""url lib 2"""

import requests
import sys


def postmail(url, mail):
    """the function tpost an emaol i think"""
    val = {'email': mail}
    data = requests.post(url, data=val)
    print(data.text)


if __name__ == "__main__":
    postmail(sys.argv[1], sys.argv[2])
