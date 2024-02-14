#!/bin/bash
# show all available methods allowed by a server
curl -siX OPTIONS "$1" | grep "Allow: " | cut -d" " -f2-
