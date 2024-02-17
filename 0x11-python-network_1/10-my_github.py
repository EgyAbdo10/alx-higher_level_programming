#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""


import requests
from sys import argv

if __name__ == "__main__":
    response = requests.post(url=f"https://api.github.com/{argv[1]}",
                             auth=(argv[2]))
    print(response.json().get("id"))
