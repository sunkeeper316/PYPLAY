# from PIL.Image import NONE
import pyautogui
import pos
import time

pos.found_d2rwin
pos.funnd_get("a")

pos.funnd_get(["ff","gg"])

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

                
def end_game() :
    pyautogui.keyDown('esc')
    time.sleep(0.03)
    
    
