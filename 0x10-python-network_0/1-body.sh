#!/bin/bash
# get the body of a 200 response
if [ $(curl -si "$1" | head -n 1 | grep -oE " [0-9]+") -eq " 200" ]; then curl -s --GET "$1"; else curl -si "$1"; fi
