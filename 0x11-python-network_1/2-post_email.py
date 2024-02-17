#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    data = {"email": argv[2]}
    data = urllib.parse.urlencode(data)
    encoded_data = data.encode("utf-8")
    req = urllib.request.Request(url=argv[1], data=encoded_data, method="POST")
    with urllib.request.urlopen(req) as response:
        body_response = response.read().decode("utf-8")
        print(body_response)
