import pyautogui
import time
import pos
from pos import wincenter

pos.found_d2rwin()

def moveSouth() :
    pyautogui.moveTo(wincenter)
    pyautogui.moveRel(None , 100)
    pyautogui.keyDown('e')
    time.sleep(0.03)
    pyautogui.keyUp()
    return

moveSouth()