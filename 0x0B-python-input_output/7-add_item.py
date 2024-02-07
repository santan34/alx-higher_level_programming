#!/usr/bin/python3
"""
Create object from a JSON file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        item = load_from_json_file('add_item.json')
    except FileNotFoundError:
        item = []
    item.extend(sys.argv[1:])
    save_to_json_file(item, 'add_item.json')
