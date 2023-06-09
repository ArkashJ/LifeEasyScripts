#!/bin/bash

# ANSI escape codes for text colors
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
MAGENTA="\033[0;35m"
CYAN="\033[0;36m"
RESET="\033[0m"

uptime_info=$(uptime)
uptime_pretty=$(echo "$uptime_info" | awk -F'up ' '{print $2}' | awk -F',' '{print $1}')

echo -e "${RED}#   _      _____ _     ____  ____  _      _____              ${RESET}"        
echo -e "${RED}#  / \\  /|/  __// \\   /   _\\/  _ \\/ \\__/|/  __/       ${RESET}" "${CYAN}Hello, Arkash!${RESET}"
echo -e "${YELLOW}#  | |  |||  \\  | |   |  /  | / \\|| |\\/|||  \\         ${RESET}"
echo -e "${YELLOW}#  | |/\\|||  /_ | |_\\|  \\_ | \\_/|| |  |||  /_           ${RESET}" "${RED}System uptime: $uptime_pretty${RESET}"
echo -e "${MAGENTA}#  \\_/  \\|\\____\\\\____/\\____/\\____/\\_/  \\|\\____\\       "
echo -e "${MAGENTA}#                                                           ${RESET}" "${YELLOW}Current date and time: $(date)${RESET}"

osascript <<EOD
tell application "Warp"
    activate
end tell
EOD

python3 ~/Desktop/LifeEasyScripts/hackerNews.py
python3 ~/Desktop/LifeEasyScripts/stocksToFollow.py
python3 ~/Desktop/LifeEasyScripts/tasks.py list