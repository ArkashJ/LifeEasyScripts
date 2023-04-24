#!/bin/bash

# ANSI escape codes for text colors
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
MAGENTA="\033[0;35m"
CYAN="\033[0;36m"
RESET="\033[0m"

echo -e "${RED}#   _      _____ _     ____  ____  _      _____ ${RESET}"
echo -e "${GREEN}#  / \\  /|/  __// \\   /   _\\/  _ \\/ \\__/|/  __/ ${RESET}"
echo -e "${YELLOW}#  | |  |||  \\  | |   |  /  | / \\|| |\\/|||  \\   ${RESET}"
echo -e "${BLUE}#  | |/\\|||  /_ | |_\\|  \\_ | \\_/|| |  |||  /_  ${RESET}"
echo -e "${MAGENTA}#  \\_/  \\|\\____\\\\____/\\____/\\____/\\_/  \\|\\____\\"
echo -e "${CYAN}#                                              ${RESET}"

# Display my name
echo -e "${CYAN}Hello, Arkash!${RESET}"

# Display current date and time
echo -e "${YELLOW}Current date and time: $(date)${RESET}"

# Display system uptime
uptime_info=$(uptime)
uptime_pretty=$(echo "$uptime_info" | awk -F'up ' '{print $2}' | awk -F',' '{print $1}')
echo -e "${GREEN}System uptime: $uptime_pretty${RESET}"

osascript <<EOD
tell application "Warp"
    activate
end tell
EOD