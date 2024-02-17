#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don't need to check arguments passed to the script (number or type)
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    headers = {"Authorization":
               'token ' + "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"}
    response = requests.get(
        url=f"https://api.github.com/repos/{owner}/{repo}/commits",
            headers=headers
        )
    for i in range(10):
        sha = response.json()[i].get("sha")
        author = response.json()[i].get("commit").get("author").get("name")
        # date = response.json()[i].get("commit").get("author").get("date")
        print(sha + " " + author)
