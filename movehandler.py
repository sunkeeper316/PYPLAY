import pos
import threading
import sched
import time
import math
import pyautogui
import direction
from targetpath import TargetPath

class MoveHandler : 
    #移動程序 (起始點檢查修正)->路徑->(1.找尋目標點擊 ,2.目標修正座標)
    #center 視窗正中央 所有移動必須跟視窗正中央去做基準點
    def __init__(self  ,targetname = "",targetPathList = [], target = (0,0) , center = pos.found_center()):
        self.center = center
        self.target = target
        self.targetname = targetname
        self.dist = -1
        self.isSearch = False
        self.targetPathList = targetPathList
        self.direction = None

    def getDist(self) : #取得距離另外線程處理
        if self.targetname == "" :
            return
        while 1 :
            self.center = pos.found_center()
            print(f"target {self.target}")
            print(f"center {self.center}")
            if self.direction :
                direction.getDirection(self.direction)
            
            pyautogui.keyDown('e')
            time.sleep(0.02)
            pyautogui.keyUp('e')
            a_pos = pyautogui.locateOnScreen(f'{self.targetname}',grayscale=True, confidence=.7 )

            # self.target = pos.found_get([self.targetname] , .6)
            if a_pos : 
                self.target = pyautogui.center(a_pos)
                self.dist = math.dist(self.center , self.target)

                print(self.dist)

                if self.dist < 150 :
                    print(f"目標已到 {self.targetname}準備下一個目標")
                    # pyautogui.keyUp('e')

                    
                    index = len(self.targetPathList) - 1
                    if self.targetname == self.targetPathList[index].target :
                        self.targetname = ""
                        break
                    self.targetname = ""
                    time.sleep(0.05)
                else  :
                    self.direction = None
                    time.sleep(0.02)
                    a_pos = pyautogui.locateOnScreen(f'{self.targetname}',grayscale=True, confidence=.7 )
                    if a_pos :
                        pyautogui.moveTo(pyautogui.center(a_pos))
                        time.sleep(0.02)
                        pyautogui.click()
                   
                    
                    print(f"目標靠近了")
                   
            else :

                time.sleep(0.02)
                # pyautogui.keyDown('e')
                # time.sleep(0.02)
                # pyautogui.keyUp('e')
            
                
            time.sleep(0.05)
        return
    def moveTargetPathList(self) : #路徑實行
        
        # self.target = pos.found_get(["assets/templates/a5_town/a5_town_0.png"] , .7)

        # s = sched.scheduler(time.time ,time.sleep)
        # s.enter(2,1,)
        # t = threading.Thread(target=self.getDist)
        # t.start()
        # center = pos.found_center()
        for index , t in enumerate(self.targetPathList)  :
            print(f"index{index}")
            self.targetname = t.target
            pyautogui.moveTo(self.center)
            time.sleep(0.1)
            pyautogui.moveRel(t.postion)
            pyautogui.press('e')
            # direction.getDirection(t.direction)
            # pyautogui.keyDown('e')
            time.sleep(1.5)
        
        
            # pyautogui.keyUp('e')
            # if index == len(self.targetPathList) - 1 :
            #     print("已到目的地")
            #     return
            # else :
            #     print("還有下一個目標")
            #     while  1 :
            #         if not self.targetname == t.target :
            #             break
           
    def move(self) :
        t = threading.Thread(target=self.getDist)
        t.start()
        
        

    def search(self) :
        self.isSearch = False
        count = 30
        pyautogui.moveTo(self.center)
        t = threading.Thread(target=self.getTarget)
        t.start()
        
        while 1 :
            
            pyautogui.moveRel((count , 0) , duration = 0.15)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , count) , duration = 0.15)
            if self.isSearch :
                break
            pyautogui.moveRel((-count , 0) , duration = 0.15)
            if self.isSearch :
                break
            pyautogui.moveRel((-count , 0) , duration = 0.15)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , -count) , duration = 0.15)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , -count) , duration = 0.15)
            if self.isSearch :
                break
            pyautogui.moveRel((count , 0) , duration = 0.15)
            if self.isSearch :
                break
            pyautogui.moveRel((count , 0) , duration = 0.15)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , count) , duration = 0.15)
            if self.isSearch :
                break
            pyautogui.moveTo(self.center , duration = 0.15)
            if self.isSearch :
                break
            count += 30
            if count > 200 :
                break
        return
    def getTarget(self) :
        newpos = pos.found_get(self.targetname , .7)
        if newpos :
            self.target = newpos
            self.isSearch = True
            t = threading.Timer(1 , self.moveTotargetNPC)
            t.start()

            
        return
    def moveTotargetNPC(self) :

        pyautogui.moveTo((self.target.x , self.target.y + 50))
        pyautogui.click()
        return

    def adjust(self ,target) :
        cur_pos = pos.found_pos(target.target)
        if not cur_pos :
            _pos = target.postion
            adjust_x =  _pos[0] - cur_pos[0] 
            adjust_y =  _pos[1] - cur_pos[1] 
            pyautogui.moveTo((adjust_x , adjust_y))
            pyautogui.press('e')
        
        return

if __name__ == "__main__" : 

    # target = pos.found_get(["assets/templates/a5_town/a5_town_0.png"] , .7)
    # m = MoveHandler(targetname = ["assets/npc/malah/malah_name_tag_white.png" ])
    # m = MoveHandler(targetname = "assets/templates/a5_town/a5_town_4.png")
    m = MoveHandler(targetPathList= TargetPath.a5_malah())
    # malah_name_tag_white
    # m = MoveHandler(targetname = ["assets/npc/malah/malah_45.png" , "assets/npc/malah/malah_back.png" , "assets/npc/malah/malah_front.png" , "assets/npc/malah/malah_side.png" , "assets/npc/malah/malah_side_2.png"])
    # m.search()
    m.moveTargetPathList()
    # m.move()
