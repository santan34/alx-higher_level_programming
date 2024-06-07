#!/usr/bin/python3
"""requests 4"""

import requests
import sys


def postapi(letter=""):
    """the function tpost an emaol i think"""
    url = "http://0.0.0.0:5000/search_user"
    val = {'q': len}
    data = requests.post(url, data=val)
    new_data = data.json()
    if new_data:
        print(f"[{new_data.get('id')}] {new_data.get('name')}")
    else:
        print('No result')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        postapi(sys.argv[1])
    else:
        postapi()
