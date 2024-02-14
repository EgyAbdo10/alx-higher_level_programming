#!/bin/bash
# get the content size in bytes in a header of a response
curl -si "$1" | grep -E "Content-Length: ([0-9]+)" | grep -oE "[0-9]+"