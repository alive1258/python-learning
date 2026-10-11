


import pyautogui
from time import sleep

n = int(input("Enter a number: "))

sleep(5)

for i in range(1, n + 1):
    pyautogui.write("#" * i)
    pyautogui.press("enter")