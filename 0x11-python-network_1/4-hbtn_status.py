#!/usr/bin/python3
"""requests 0"""

import requests
import sys


def alxstatus(url):
    """the function to get the repsonse"""
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")


if __name__ == "__main__":
    alxstatus('https://alx-intranet.hbtn.io/status')
