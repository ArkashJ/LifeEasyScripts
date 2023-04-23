#!/bin/bash

# Check if a search term is provided
if [ -z "$1" ]; then
  echo "Please provide a search term."
  exit 1
fi

# Set the search term
search_term=$1

# Find files and directories matching the search term recursively from the current directory
find . -iname "*${search_term}*" -print
