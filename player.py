# from PIL.Image import NONE

import pyautogui
import pos
import time

pos.found_d2rwin

def moveSouth() :
    pyautogui.moveTo(pos.wincenter)
    pyautogui.moveRel(None , 100)
    pyautogui.keyDown('e')
    time.sleep(0.03)
    pyautogui.keyUp()
    return

def end_game() :
    print("離開遊戲")
    pyautogui.keyDown('esc')
    time.sleep(0.03)
    exit_pos = pos.funnd_get(["templates/save_and_exit_highlight","templates/save_and_exit_no_highlight"])
    pyautogui.moveTo(exit_pos)
    time.sleep(0.03)
    pyautogui.click()

end_game()


time.sleep(1)
# pyautogui.moveRel(NONE , 375 , duration= 0.5)
time.sleep(1)

play = pos.found_start()

pyautogui.moveTo(play)
time.sleep(0.03)
pyautogui.click()

difficulty = pos.found_pos("nightmare_btn")

pyautogui.moveTo(difficulty )
time.sleep(0.03)
pyautogui.click()

pos.found_d2rwin()


                

    
    
