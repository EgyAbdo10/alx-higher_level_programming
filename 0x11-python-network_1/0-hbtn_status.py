#!/usr/bin/python3
"""this module fetches https://alx-intranet.hbtn.io/status resources"""


import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        charset = response.headers.get_content_charset()
        content_b = response.read()
        content = content_b.decode("utf-8")
        print("Body response:")
        print(f"\t- type: {type(content_b)}")
        print(f"\t- content: {content_b}")
        print(f"\t- utf8 content: {content}")
