#!/usr/bin/python3
"""url lib 0"""

import urllib
import urllib.request


def alxstatus(url):
    """the function to get the repsonse"""
    with urllib.request.urlopen(url) as response:
        data = response.read()
        data_utf = data.decode('utf8')

    print("Body response:")
    print(f"\t - type: {type(data)}")
    print(f"\t - content : {data}")
    print(f"\t - utf8 content : {data_utf}")


if __name__ == "__main__":
    alxstatus('https://alx-intranet.hbtn.io/status')
