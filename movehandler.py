from pyscreeze import center
import pos
import threading
import displaymap
import time
import math
import pyautogui
import direction
from targetpath import TargetPath, TargetProcess ,TargetPos
import random

class MoveHandler : 
    #移動程序 (起始點檢查修正)->路徑->(1.找尋目標點擊 ,2.目標修正座標)
    #center 視窗正中央 所有移動必須跟視窗正中央去做基準點
    # TargetProcess 流程來執行整體移動 teleport 是否能傳送
    def __init__(self  ,targetprocess = None,teleport = False,current = "" , center = pos.found_center()):
        self.center = center
        self.targetprocess = targetprocess
        
        self.isSearch = False
        self.direction = None
        self.current = current
        self.teleport = teleport 


    def adjust(self ,target ) :
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
                if adjust_x > target.adjust or adjust_y > target.adjust or adjust_x < -target.adjust or adjust_y < -target.adjust:
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
            else :
                print("卡住了")
                return False
            
            time.sleep(0.5)
        return True
    def atk_adjust(self ,target ) :
        print("修正目的地位子")
        start = time.time()
        while 1 :
            _pos = pyautogui.locateCenterOnScreen(target.target , grayscale=True, confidence=.7)
            # _pos = pos.found_pos(target.target , .7)
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
                    time.sleep(0.1)
                    pyautogui.moveRel((adjust_x , adjust_y))
                    time.sleep(0.1)
                    pyautogui.press('f3')
                    time.sleep(0.1)
                    pyautogui.press('f1')
                    time.sleep(0.1)
                    pyautogui.press('f1')
                    # time.sleep(0.3)
                    # self.test(target)
                else :
                    print("差距過小不需要修正")
                    break
            else :
                pyautogui.moveTo(self.center)
                time.sleep(0.1)
                pyautogui.moveRel((random.randint(-50,50) , random.randint(-50,50)))
                time.sleep(0.1)
                pyautogui.press('f3')
                time.sleep(0.1)
                pyautogui.press('f1')
                time.sleep(0.1)
                pyautogui.press('f1')
            time.sleep(0.05)
            if (time.time() - start) > 60 :
                print("卡點")
                return False
        return True

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
        start = time.time()
        while 1 :
            
            pyautogui.moveRel((count , 0) , duration = 0.2)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , count) , duration = 0.2)
            if self.isSearch :
                break
            pyautogui.moveRel((-count , 0) , duration = 0.2)
            if self.isSearch :
                break
            pyautogui.moveRel((-count , 0) , duration = 0.2)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , -count) , duration = 0.2)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , -count) , duration = 0.2)
            if self.isSearch :
                break
            pyautogui.moveRel((count , 0) , duration = 0.2)
            if self.isSearch :
                break
            pyautogui.moveRel((count , 0) , duration = 0.2)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , count) , duration = 0.2)
            if self.isSearch :
                break
            pyautogui.moveTo(self.center , duration = 0.2)
            if self.isSearch :
                break
            count += 30
            if count > 150 :
                count = 60
            if (time.time() - start) > 60 :
                print("卡點")
                return False
        time.sleep(1)
        return True
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

    def runTargetProcess(self ) :
        if self.targetprocess.atk :
            pyautogui.press('f5')
            time.sleep(0.05)
            pyautogui.press('f2')
        start_target = self.targetprocess.start_target
        print("start_target")
        if not self.adjust(start_target) :
            return False
        self.current = start_target
        print(f"當前位子{self.current}")
        for index , pos in enumerate(self.targetprocess.poslist) :
            pyautogui.moveTo(self.center)
            time.sleep(0.1)
            pyautogui.moveRel(pos)
            if self.targetprocess.teleport :
                pyautogui.press('f3')
            else :
                pyautogui.press('e')
                time.sleep(1.5)
            
        if self.targetprocess.end_target :
            end_target = self.targetprocess.end_target
            print("end_target")
            if self.targetprocess.atk :
                if not self.atk_adjust(end_target) :
                    return False
            else :
                if not self.adjust(end_target ) :
                    return False
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
        while ( time.time() - start ) < timeout :
            print(time.time() - start)
            pyautogui.press(f'{key}')
            time.sleep(interval)
        time.sleep(0.05)
        pyautogui.press('f6')
        # self.pickitems(10,0.1)
    def pickitems(self,timeout , interval) :
        pyautogui.press('alt')
        time.sleep(0.5)
        items = displaymap.read_directory("assets/items/")
        start = time.time()
        while ( time.time() - start ) < timeout :
            for item in items :
                print(item)
                a_pos = pyautogui.locateCenterOnScreen(f'{item}',grayscale=True, confidence=.7 )
                if a_pos :
                    time.sleep(0.1)
                    pyautogui.moveTo(a_pos)
                    time.sleep(0.1)
                    pyautogui.click()
            
            time.sleep(interval)
        time.sleep(0.05)
        pyautogui.press('alt')
    def putstore() :
        return
    
    def funnd_grid( row ) :
        center = pos.found_center()
        pyautogui.keyDown('ctrl')
        for i in range(0 , row) :
            for j in range(0 , 4) :
                print((center[0] + 305 + i * 40,center[1] - 13 + j * 40))
                grid = pyautogui.locateOnScreen('assets/templates/grid.png',grayscale=False, confidence=.75 , region=( center[0] + 305 + i * 37 , center[1] - 13 + j * 37 , 45 , 45))
                print(grid)
                if not grid :
                    pyautogui.moveTo((center[0] + 305 + i * 40 + 19 ,center[1] - 13 + j * 40 + 19) , duration = 0.2)
                    time.sleep(0.3)
                    pyautogui.click()
                    time.sleep(0.3)
                    
        pyautogui.keyUp('ctrl')



if __name__ == "__main__" : 

    # target = pos.found_get(["assets/templates/a5_town/a5_town_0.png"] , .7)
    # m = MoveHandler(targetname = ["assets/npc/malah/malah_name_tag_white.png" ])
    # m = MoveHandler(targetname = "assets/templates/a5_town/a5_town_4.png")
    testTargetPos = TargetPos("assets/templates/a5_town/a5_town_0.png" , (51,135))
   
    # a5_start_to_malah  a5_malah_to_start  a5_start_to_redDoor  assets/templates/pindle/pindle_8.pnge
    
    # m.adjust(testTargetPos)
    m = MoveHandler(targetprocess= TargetProcess.a5_start_to_malah())
    # m.runTargetProcess()
    # m.test(testTargetPos)
    m.pickitems(20,0.2)
    # malah_name_tag_white   
    # m = MoveHandler(targetname = ["assets/npc/malah/malah_45.png" , "assets/npc/malah/malah_back.png" , "assets/npc/malah/malah_front.png" , "assets/npc/malah/malah_side.png" , "assets/npc/malah/malah_side_2.png"])
    # m.search()

    # m = MoveHandler(targetprocess= TargetProcess.a5_start_to_malah())
    # t1 = m.runTargetProcess()
    # if t1 :
    #     print("t1 ok")
    #     m.targetprocess = TargetProcess.a5_malah_to_start()
    #     t2 = m.runTargetProcess()
    #     if t2 :
    #         print("t2 ok")
    #         m.targetprocess = TargetProcess.a5_start_to_redDoor()
    #         t3 = m.runTargetProcess()
    #         if t3 :
    #             print("t3 ok")
    #             m.targetprocess = TargetProcess.a5_reddoor_to_pindle()

    #             t4 = m.runTargetProcess()
    #             if t4 :
    #                 print("t4 ok")
    #                 m.atk(10 , 'f1' , 0.05)
    #                 time.sleep(0.05)
    #                 pyautogui.press('f6')

    # m = MoveHandler(targetprocess= TargetProcess.a5_reddoor_to_pindle())
    # t4 = m.runTargetProcess()
    # if t4 :
    #     print("t4 ok")
    #     m.atk(5 , 'f1' , 0.2)
    
    # m.atk(20 , 'f1' , 0.2)
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