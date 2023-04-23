#!/bin/bash

# Prompt for custom screenshot name using AppleScript
custom_name=$(osascript -e 'text returned of (display dialog "Enter screenshot name:" default answer "" with title "Screenshot Name")')

# Check if the user clicked cancel or didn't provide a name
if [[ -z "$custom_name" ]]; then
    exit 1
fi

# Set custom screenshot name format
filename="${custom_name}_$(date +%Y-%m-%d).png"
filepath="$HOME/Desktop/$filename"

# Add a delay (e.g., 5 seconds) and take a screenshot, saving it to the Desktop
sleep 2
screencapture -x "$filepath"
