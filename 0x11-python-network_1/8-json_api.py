#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
from sys import argv

if __name__ == "__main__":
    data = {"q": argv[1]}
    if len(argv) > 2:
        data = {"q": ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        res_dict = response.json()
        if res_dict == {}:
            print("No result")
        else:
            print(f"[{res_dict.get("id")}] {res_dict.get("name")}")
    except TypeError:
        print("Not a valid JSON")
