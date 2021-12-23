
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
        difficulty_pos = pos.found_pos(self.difficulty , .8)
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
            else :
                print('卡住重開')
                
                self.end_game()
            
        self.moveHandler.atk( 10 ,'f1' ,0.1)
        time.sleep(2)
        self.end_game()
  
    def end_game(self) :
        print("離開遊戲")
        time.sleep(0.3)
        pyautogui.moveTo(self.moveHandler.center)

        time.sleep(0.3)
        pyautogui.moveRel(400,400)
        time.sleep(0.3)
        pyautogui.press('esc')
        time.sleep(0.3)
        exit_pos = pos.found_pos("assets/templates/save_and_exit_highlight.png" , .8)
        if exit_pos :
            pyautogui.moveTo(exit_pos)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(0.3)
            self.start()
        else :
            self.end_game()
    
    @staticmethod
    def a5_reddoor_process() :
        p1 = TargetProcess.a5_start_to_malah()
        p2 = TargetProcess.a5_malah_to_start()
        p3 = TargetProcess.a5_start_to_redDoor()
        p4 = TargetProcess.a5_reddoor_to_pindle()
        return [p1 , p2 , p3 , p4]

# assets/templates/hell_btn.png
# assets/templates/nightmare_btn.png
# assets/templates/normal_btn.png

if __name__ == "__main__" : 
    _player = Player(difficulty = Player.hell)
    _player.start()
# pos.found_d2rwin
