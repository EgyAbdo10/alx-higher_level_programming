#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""


import requests
from sys import argv

if __name__ == "__main__":
    headers = {"Authorization": 'token ' + argv[2]}
    response = requests.get(url="https://api.github.com/user",
                            headers=headers)
    print(response.json().get("id"))
