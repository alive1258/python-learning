import pyautogui
from time import sleep
sleep(5)
for i in range(5):
    pyautogui.write("Hello, World!",interval=0.1)
    pyautogui.press("enter")