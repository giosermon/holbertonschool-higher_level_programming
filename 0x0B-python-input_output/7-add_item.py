#!/usr/bin/python3
""" Module for storing script to save argv[] as a text file and append.  """
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    json_obj = load_from_json_file("add_item.json")
except:
    save_to_json_file(sys.argv[1:], "add_item.json")
else:
    json_obj = json_obj + sys.argv[1:]
    save_to_json_file(json_obj, "add_item.json")
