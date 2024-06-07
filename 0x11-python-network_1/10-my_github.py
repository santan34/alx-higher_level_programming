#!/usr/bin/python3
"""more requests"""
import requests
import sys
try:
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
except BaseException:
    print("None")
