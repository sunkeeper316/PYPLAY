# from PIL.Image import NONE

import pyautogui
from displaymap import DisplayMap
import pos
import time
import displaymap
from task import Task
from movehandler import MoveHandler 
from targetpath import TargetProcess

class Player: #主要控制開遊戲前的選單 在用moveHandler控制遊戲內路徑跟操作
    normal = "assets/templates/hell_btn.png"
    nightmare = "assets/templates/nightmare_btn.png"
    hell = "assets/templates/hell_btn.png"
    def __init__(self  , difficulty  ) :
        # fself.tasks.append()
        self.difficulty = difficulty
        
        self.moveHandler = MoveHandler()

    def start(self) :
        print("開始遊戲")
        play = pos.found_pos("assets/templates/play_btn_gray.png" , .7)
        # assets/templates/play_btn_gray.png
        pyautogui.moveTo(play)
        time.sleep(0.3)
        pyautogui.click()
        # if difficulty == "norm"
        difficulty_pos = pos.found_pos(self.difficulty , .7)
        pyautogui.moveTo(difficulty_pos)
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(0.3)
        self.runprocess()
        # pos.found_d2rwin() 
        # checkTownTask = Task()
        # self.displaymap = checkTownTask.checTOWNSTART()

        # checkTownTask.a5_moveToRedWp()

    
    def runprocess(self) :
        print('執行遊戲流程')
        processList = Player.a5_reddoor_process()
        for p in processList :
            self.moveHandler.targetprocess = p
            result = self.moveHandler.runTargetProcess()
            if result :
                print('下一個流程')
                continue
            
        self.moveHandler.atk( 20 ,'f1' ,0.5)
            

    def checkTask(self) :
        Task.checkDisPlay()

    # def moveSouth(self) :
    #     pyautogui.moveTo(pos.wincenter)
    #     pyautogui.moveRel(None , 100)
    #     pyautogui.keyDown('e')
    #     time.sleep(0.03)
    #     pyautogui.keyUp()
    #     return

    
    def end_game(self) :
        print("離開遊戲")
        time.sleep(0.1)
        pyautogui.keyDown('esc')
        time.sleep(0.1)
        exit_pos = pos.found_pos_list(["templates/save_and_exit_highlight","templates/save_and_exit_no_highlight"] , .7)
        pyautogui.moveTo(exit_pos)
        time.sleep(0.1)
        pyautogui.click()
    
    @staticmethod
    def a5_reddoor_process() :
        start = TargetProcess.a5_malah_to_start()
        to_malah = TargetProcess.a5_malah_to_start()
        malah_back = TargetProcess.a5_malah_to_start()
        return []

# assets/templates/hell_btn.png
# assets/templates/nightmare_btn.png
# assets/templates/normal_btn.png

if __name__ == "__main__" : 
    _player = Player(difficulty = Player.hell)
    _player.start()
# pos.found_d2rwin



# pos.end_game()


# time.sleep(1)
# pyautogui.moveRel(NONE , 375 , duration= 0.5)
# time.sleep(1)




                

    
    
