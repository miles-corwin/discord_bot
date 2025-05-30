# imports
import pyautogui
import time
import sys
import json
# open config.json
with open("config.json") as f:
    config = json.load(f)

user = sys.argv[1]

# this line opens the chat menu
pyautogui.press(config["chat_open_key"])
time.sleep(1)

# and then this line enter the bot command inside the chat menu
invite_cmd = config["invite_command_template"].format(username=user)
pyautogui.typewrite(invite_cmd)
pyautogui.press("enter")

# after that it waits a bit to join; it is done to prevent server crash or overload or whatever you call it
time.sleep(config["launch_delay"])

# it then uses pyautogui to simulate clicks
# logic for start_button and leave_button.... DONE
pyautogui.click(config["destiny2_coords"]["start_button"])
time.sleep(config["leave_delay"])
pyautogui.click(config["destiny2_coords"]["leave_button"])
