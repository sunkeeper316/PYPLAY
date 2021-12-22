from pyscreeze import center
import pos
import threading
import displaymap
import time
import math
import pyautogui
import direction
from targetpath import TargetPath, TargetProcess ,TargetPos

class MoveHandler : 
    #移動程序 (起始點檢查修正)->路徑->(1.找尋目標點擊 ,2.目標修正座標)
    #center 視窗正中央 所有移動必須跟視窗正中央去做基準點
    # TargetProcess 流程來執行整體移動 teleport 是否能傳送
    def __init__(self  ,targetprocess,teleport = False,current = "",targetname = "",targetPathList = [], target = (0,0) , center = pos.found_center()):
        self.center = center
        self.targetprocess = targetprocess
        self.target = target
        self.targetname = targetname
        self.dist = -1
        self.isSearch = False
        self.targetPathList = targetPathList
        self.direction = None
        self.current = current
        self.teleport = teleport 


    def adjust(self ,target) :
        print("修正目的地位子")
        while 1 :
            _pos = pos.found_pos(target.target , .7)
            time.sleep(0.1)
            if  _pos :
                current_pos = (_pos[0]-self.center[0],_pos[1]-self.center[1])
                print(f"_pos:{_pos}")
                print(f"center{self.center}")
                adjust_x =  current_pos[0] - target.postion[0]
                adjust_y =  current_pos[1] - target.postion[1]
                print(f"adjust_ {(adjust_x , adjust_y)}")
                if adjust_x > 30 or adjust_y > 30 or adjust_x < -30 or adjust_y < -30:
                    pyautogui.moveTo(self.center)
                    time.sleep(0.3)
                    pyautogui.moveRel((adjust_x , adjust_y))
                    time.sleep(0.3)
                    pyautogui.press('e')
                    # time.sleep(0.3)
                    # self.test(target)
                else :
                    print("差距過小不需要修正")
                    break
            
            time.sleep(0.5)
        return

    def test(self,target) :
        _pos = pos.found_pos(target.target , .7)
        print(f"test center{self.center}")
        print(f"test _pos:{_pos}")
        pyautogui.moveTo(_pos)
        print((_pos[0]-self.center[0],_pos[1]-self.center[1]))

    def search(self) :
        self.isSearch = False
        count = 60
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
                count = 60
                
        time.sleep(1)
        return
    def getTarget(self) :
        print("sreach")
        newpos = pos.found_pos(self.targetprocess.search , .7)
        
        if newpos :
            print(f"sreach 確定{newpos}")
            # self.target = newpos
            self.isSearch = True
            time.sleep(0.2)
            pyautogui.moveTo((newpos[0] , newpos[1] + 50))
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(0.5)
            # t = threading.Timer(1 , self.movesreach)
            # t.start()
        return
    # def movesreach(self) :
    #     print("點擊 sreach")
        
    #     return

    def runTargetProcess(self , teleport = False) :
        start_target = self.targetprocess.start_target
        self.adjust(start_target)
        self.current = start_target
        print(f"當前位子{self.current}")
        for index , pos in enumerate(self.targetprocess.poslist) :
            pyautogui.moveTo(self.center)
            time.sleep(0.1)
            pyautogui.moveRel(pos)
            if teleport :
                pyautogui.press('f3')
            pyautogui.press('e')
            time.sleep(1.5)

        end_target = self.targetprocess.end_target
        self.adjust(end_target)

        self.current = end_target
        print(f"當前位子{self.current}")
        if self.targetprocess.search :
            print(f"尋找目標{self.targetprocess.search}")
            time.sleep(0.3)
            self.search()
        time.sleep(0.3)
        return True
    def atk(self,timeout , key , interval) :
        start = time.time()
        while ( time.time() - start ) > timeout :
            pyautogui.press(f'{key}')
            time.sleep(interval)
        self.pickitems(10,0.1)
    def pickitems(self,timeout , interval) :
        pyautogui.press('alt')
        time.sleep(0.5)
        items = displaymap.read_directory("assets/items/")
        start = time.time()
        while ( time.time() - start ) > timeout :
            for item in items :
                a_pos = pyautogui.locateCenterOnScreen(f'{item}',grayscale=True, confidence=.7 )
                if a_pos :
                    pyautogui.moveTo()
                    time.sleep(0.1)
                    pyautogui.click()
            
            time.sleep(interval)
    def putstore() :
        return



if __name__ == "__main__" : 

    # target = pos.found_get(["assets/templates/a5_town/a5_town_0.png"] , .7)
    # m = MoveHandler(targetname = ["assets/npc/malah/malah_name_tag_white.png" ])
    # m = MoveHandler(targetname = "assets/templates/a5_town/a5_town_4.png")
    testTargetPos = TargetPos("assets/templates/a5_town/a5_town_0.png" , (51,135))
    m = MoveHandler(targetprocess= TargetProcess.a5_start_to_malah())
    # a5_start_to_malah  a5_malah_to_start  a5_start_to_redDoor
    # m.test(testTargetPos)
    # m.adjust(testTargetPos)
    # m = MoveHandler(targetPathList= TargetPath.a5_malah())
    # malah_name_tag_white   
    # m = MoveHandler(targetname = ["assets/npc/malah/malah_45.png" , "assets/npc/malah/malah_back.png" , "assets/npc/malah/malah_front.png" , "assets/npc/malah/malah_side.png" , "assets/npc/malah/malah_side_2.png"])
    # m.search()
    t1 = m.runTargetProcess()
    if t1 :
        
        m.targetprocess = TargetProcess.a5_malah_to_start()
        t2 = m.runTargetProcess()
        if t2 :
            m.targetprocess = TargetProcess.a5_start_to_redDoor()
            t3 = m.runTargetProcess()
    # threading.Event
    # m.move()



    # def getDist(self) : #取得距離另外線程處理
    #     if self.targetname == "" :
    #         return
    #     while 1 :
    #         self.center = pos.found_center()
    #         print(f"target {self.target}")
    #         print(f"center {self.center}")
    #         if self.direction :
    #             direction.getDirection(self.direction)
            
    #         pyautogui.keyDown('e')
    #         time.sleep(0.02)
    #         pyautogui.keyUp('e')
    #         a_pos = pyautogui.locateOnScreen(f'{self.targetname}',grayscale=True, confidence=.7 )

    #         # self.target = pos.found_get([self.targetname] , .6)
    #         if a_pos : 
    #             self.target = pyautogui.center(a_pos)
    #             self.dist = math.dist(self.center , self.target)

    #             print(self.dist)

    #             if self.dist < 150 :
    #                 print(f"目標已到 {self.targetname}準備下一個目標")
    #                 # pyautogui.keyUp('e')

                    
    #                 index = len(self.targetPathList) - 1
    #                 if self.targetname == self.targetPathList[index].target :
    #                     self.targetname = ""
    #                     break
    #                 self.targetname = ""
    #                 time.sleep(0.05)
    #             else  :
    #                 self.direction = None
    #                 time.sleep(0.02)
    #                 a_pos = pyautogui.locateOnScreen(f'{self.targetname}',grayscale=True, confidence=.7 )
    #                 if a_pos :
    #                     pyautogui.moveTo(pyautogui.center(a_pos))
    #                     time.sleep(0.02)
    #                     pyautogui.click()
                   
                    
    #                 print(f"目標靠近了")
                   
    #         else :

    #             time.sleep(0.02)
    #             # pyautogui.keyDown('e')
    #             # time.sleep(0.02)
    #             # pyautogui.keyUp('e')
            
                
    #         time.sleep(0.05)
    #     return
    
    # def moveTargetPathList(self) : #路徑實行

    #     for index , t in enumerate(self.targetPathList)  :
    #         print(f"index{index}")
    #         self.targetname = t.target
    #         pyautogui.moveTo(self.center)
    #         time.sleep(0.1)
    #         pyautogui.moveRel(t.postion)
    #         pyautogui.press('e')
    #         # direction.getDirection(t.direction)
    #         # pyautogui.keyDown('e')
    #         time.sleep(1.5)
        
           
    # def move(self) :
    #     t = threading.Thread(target=self.getDist)
    #     t.start()