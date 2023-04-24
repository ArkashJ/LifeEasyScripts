#!/bin/bash

#Empty the trash
osascript <<EOD
tell application "Finder"
    empty trash
end tell
EOD
