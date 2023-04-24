# LifeEasyScripts
Useful bash scripts to save time

-----------------------------
1. filefind.sh

- Script iterates through my computer (directories and subdirectories), finds all the files and folders that match the name 
   I input and returns their path
- Case insensitive, so lowercase, UPPERCASE and camelCase all work
- Should be made executable using $ "chmod +x find_lecture.sh" before running it.
- Does NOT require root privileges, but it might not be able to access certain directories due to permission restrictions
- In case of permission restriction, the terminal prompts the user for password access

2. custom_screenshot_mac.sh

- Script makes a graphical interface using an applescript command to prompt the user for the name of the screenshot
- One has 2 seconds to go to the window they want to take a screenshot of
- The screenshot is story on the desktop in the format "CustomName Year-Month-Day"
- Make executable my running $ "chmod +x custom_screenshot_mac.sh"

3. sleep.sh

- Script to sleep mac
- $ "chmod +x sleep.sh"

4. lock.sh

- Script to lock mac screen
- $ "chmod +x lock.sh"

5. empty_trash.sh

- Script to empty the trash

6. colored_test.sh

- Script to print colored welcome in my terminal everytime I open it

-----------------------------
## Setting Aliases

$ cd ~
$ code ~/.zshrc
 
### alias find='~/ENTER_YOUR_PATH//filefind.sh'
### alias ss='~/ENTER_YOUR_PATH/custom_screenshot_mac.sh'
### alias slp='~/ENTER_YOUR_PATH/sleep.sh'
### alias lck='~/ENTER_YOUR_PATH/lock.sh'
### alias empty='~/ENTER_YOUR_PATH/empty_trash.sh'

In the .zshrc file, at the end of the file write
### source ~/ENTER_YOUR_PATH/colored_text.sh 
-----------------------------
 # Example Execution
 
$ ss
### Output: "Enter screenshot name:" Github
 
 $ find lifeeasyscripts 
### Output: ./Desktop/LifeEasyScripts

$ find lifeEASYscripts
### Output: ./Desktop/LifeEasyScripts
-----------------------------
### Note: Run $ 'source ~/.zshrc' after saving your changes on a text editor
