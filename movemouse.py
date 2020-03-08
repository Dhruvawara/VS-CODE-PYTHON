import pyautogui
import time

while True:
    pyautogui.moveTo(200, 200)   # moves mouse to X of 200, Y of 200.
    time.sleep(1)
    pyautogui.moveTo(None, 500)  # moves mouse to X of 200, Y of 500.
    time.sleep(3)
# pyautogui.moveTo(600, None)  # moves mouse to X of 600, Y of 500.