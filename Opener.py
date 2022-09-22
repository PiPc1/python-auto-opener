import os
import pyautogui
import time

userinput = input("pick 1 or 2: ")
option1 = "https://www.youtube.com/watch?v=jn2oVULHz_M"
option2 = "https://www.youtube.com/shorts/mBNnvVt2POQ"

if userinput == "1":
    os.system('start microsoft-edge://')
    time.sleep(0.9)
    pyautogui.typewrite(option1)
    pyautogui.press('enter')
    

if userinput == "2":
    os.system('start microsoft-edge://')
    time.sleep(0.9)
    pyautogui.typewrite(option2)
    pyautogui.press('enter')