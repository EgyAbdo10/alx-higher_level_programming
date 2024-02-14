#!/bin/bash
# show all available methods allowed by a server
curl -sX OPTIONS "$1" | grep "Allow: " | grep -oE "\b [a-zA-Z]+\b"
