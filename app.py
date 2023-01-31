import os
import sys
import time
import tempfile
import datetime

import pyautogui

def take_screenshot():
    # Take screenshot using PyAutoGUI
    image = pyautogui.screenshot()
    
    # Define file location on the desktop
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/images' )
    now = datetime.datetime.now()
    file_name = f'screenshot_{now.strftime("%Y%m%d_%H%M%S")}.png'
    file_path = os.path.join(desktop, file_name)
    
    # Save the screenshot to the defined file location
    image.save(file_path)

    
if __name__ == '__main__':
    while True: # loop indefinitely
        take_screenshot()
        time.sleep(5) # delay for 5 seconds
