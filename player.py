# from PIL.Image import NONE

import pyautogui
from displaymap import DisplayMap
import pos
import time
import displaymap
from task import Task

class Player:
    def __init__(self , displaymap  = None , tasks = []) :
        self.tasks.append()
        self.displaymap = displaymap
        self.tasks = tasks

    def start(self) :
        play = pos.found_start()

        pyautogui.moveTo(play)
        time.sleep(0.03)
        pyautogui.click()
        difficulty = pos.found_pos("nightmare_btn")
        pyautogui.moveTo(difficulty)
        time.sleep(0.03)
        pyautogui.click()

        pos.found_d2rwin()
        
        checkTownTask = Task()
        self.displaymap = checkTownTask.checTOWNSTART()

        

    def checkTask(self) :
        Task.checkDisPlay()

    def moveSouth(self) :
        pyautogui.moveTo(pos.wincenter)
        pyautogui.moveRel(None , 100)
        pyautogui.keyDown('e')
        time.sleep(0.03)
        pyautogui.keyUp()
        return

    def end_game(self) :
        print("離開遊戲")
        pyautogui.keyDown('esc')
        time.sleep(0.03)
        exit_pos = pos.funnd_get(["templates/save_and_exit_highlight","templates/save_and_exit_no_highlight"])
        pyautogui.moveTo(exit_pos)
        time.sleep(0.03)
        pyautogui.click()
pos.found_d2rwin



pos.end_game()


# time.sleep(1)
# pyautogui.moveRel(NONE , 375 , duration= 0.5)
# time.sleep(1)




                

    
    
