import pyautogui
import time
import pos
import threading
from pos import wincenter

class Task:
    def __init__(self) :
        pass
    
    pos.found_d2rwin()

    def moveSouth() :
        pyautogui.moveTo(wincenter)
        pyautogui.moveRel(0 , 100)
        pyautogui.keyDown('e')
        time.sleep(0.03)
        pyautogui.keyUp()
        return

        # moveSouth()



