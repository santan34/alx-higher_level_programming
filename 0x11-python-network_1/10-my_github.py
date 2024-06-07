#!/usr/bin/python3
"""git tish"""
import requests
from sys import argv
try:
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
except BaseException:
    print("None")
