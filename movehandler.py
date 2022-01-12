from pyscreeze import center
import pos
import threading
import displaymap
import time
import math
import pyautogui
import common
from targetpath import TargetPath, TargetProcess ,TargetPos
import random


class MoveHandler : 
    #移動程序 (起始點檢查修正)->路徑->(1.找尋目標點擊 ,2.目標修正座標)
    #center 視窗正中央 所有移動必須跟視窗正中央去做基準點
    # TargetProcess 流程來執行整體移動 teleport 是否能傳送
    def __init__(self  ,targetprocess = None,teleport = False,current = "" , center = pos.found_center() ):
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
        while (time.time() - start) > 60 :
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
                    time.sleep(0.2)
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
                time.sleep(0.2)
                pyautogui.press('f1')
                
            time.sleep(0.05)
            if (time.time() - start) > 60 :
                print("卡點")
                return False
        return True

    def noAdjust(self , targetpos):
        tpos = pos.found_pos(targetpos.target , confidence = .6)
        if tpos :
            pyautogui.moveTo(tpos , duration = 0.1)
            time.sleep(0.3)
            if targetpos.targetclick :
                clickpos = pos.found_pos(targetpos.targetclick , confidence = .6)
                if clickpos :
                    pyautogui.moveTo(clickpos , duration = 0.1)
                    time.sleep(0.3)
                    pyautogui.click()
                    return True
                else :
                    return False
            else :
                pyautogui.click()
                return True
        else :
            return False

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
            
            pyautogui.moveRel((count , 0) , duration = 0.3)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , count) , duration = 0.3)
            if self.isSearch :
                break
            pyautogui.moveRel((-count , 0) , duration = 0.3)
            if self.isSearch :
                break
            pyautogui.moveRel((-count , 0) , duration = 0.3)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , -count) , duration = 0.3)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , -count) , duration = 0.3)
            if self.isSearch :
                break
            pyautogui.moveRel((count , 0) , duration = 0.3)
            if self.isSearch :
                break
            pyautogui.moveRel((count , 0) , duration = 0.3)
            if self.isSearch :
                break
            pyautogui.moveRel((0 , count) , duration = 0.3)
            if self.isSearch :
                break
            pyautogui.moveTo(self.center , duration = 0.3)
            if self.isSearch :
                break
            count += 30
            if count > 150 :
                count = 60
            if (time.time() - start) > 20 :
                
                print("卡點")
                common.infoLog(f"未尋找到{self.targetprocess.search},卡點")
                return False
        time.sleep(1)
        return True
    def getTarget(self) :
        print("sreach")
        newpos = pos.found_pos(self.targetprocess.search , .6 , timeout=20)
        
        if newpos :
            print(f"sreach 確定{newpos}")
            # self.target = newpos
            self.isSearch = True
            time.sleep(1)
            pyautogui.moveTo((newpos[0] , newpos[1] + 50))
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(0.5)
            # t = threading.Timer(1 , self.movesreach)
            # t.start()
        
        
    # def movesreach(self) :
    #     print("點擊 sreach")
        
    #     return

    def runTargetProcess(self ) :
        
        if self.targetprocess.start_target :
            start_target = self.targetprocess.start_target
            if self.targetprocess.atk :
                if pos.found_pos(start_target.target , confidence = .8) :
                    self.addbuff('f5')
                    
            print("start_target")
            if not self.adjust(start_target) :
                return False
        
            self.current = start_target
        print(f"當前位子{self.current}")
        for index , _pos in enumerate(self.targetprocess.poslist) :
            pyautogui.moveTo(self.center)
            time.sleep(0.1)
            pyautogui.moveRel(_pos)
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
                if self.targetprocess.end_target.adjust :
                    if not self.adjust(end_target ) :
                        return False
                else :
                    if not self.noAdjust(end_target ) :
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
            pyautogui.moveTo(self.center)
            time.sleep(0.05)
            pyautogui.moveRel((250,-200))
            time.sleep(0.05)
            pyautogui.press(f'{key}')
            time.sleep(interval)
        time.sleep(0.05)
        pyautogui.press('f6')
        # self.pickitems(10,0.1)
    def addbuff(self , buffclick , ctabuff = None) :
        time.sleep(0.3)
        pyautogui.press(buffclick)
        time.sleep(0.3)

        if ctabuff :
            pyautogui.press('w')
            time.sleep(0.2)
            pyautogui.press('f6')
            time.sleep(0.2)
            pyautogui.press('f7')
            time.sleep(0.2)
            pyautogui.press('w')
            time.sleep(0.2)
        
    def pickitems(self,timeout , interval) :
        pyautogui.press('alt')
        time.sleep(0.5)
        items = displaymap.read_directory("assets/pickitem/")
        start = time.time()
        while ( time.time() - start ) < timeout :
            for item in items :
                print(item)
                a_pos = pyautogui.locateCenterOnScreen(f'{item}',grayscale=False, confidence=.75 )
                if a_pos :
                    time.sleep(0.1)
                    pyautogui.moveTo(a_pos)
                    time.sleep(0.1)
                    pyautogui.click()
            
            time.sleep(interval)
        time.sleep(0.05)
        pyautogui.press('alt')
    
    def put_store(self,benchmark, row ) :

        # center = pos.found_center()
        pyautogui.keyDown('ctrl')
        for i in range(0 , row) :
            for j in range(0 , 4) :
                print((benchmark[0] + 305 + i * 40,benchmark[1] - 13 + j * 40))
                grid = pyautogui.locateOnScreen('assets/templates/grid.png',grayscale=False, confidence=.75 , region=( benchmark[0]  + i * 37 , benchmark[1]  + j * 37 , 45 , 45))
                print(grid)
                if not grid :
                    print("放入倉庫")
                    pyautogui.moveTo((benchmark  + i * 40 + 19 ,benchmark  + j * 40 + 19) , duration = 0.2)
                    time.sleep(0.3)
                    pyautogui.click()
                    time.sleep(0.3)
                    
        pyautogui.keyUp('ctrl')
        time.sleep(0.3)
        pyautogui.press('esc')
        time.sleep(0.3)
        return True
    
    def getCorpse(self) :
        center = pos.found_center()
        pyautogui.moveTo(center)
        time.sleep(0.3)
        postion = pyautogui.locateCenterOnScreen('assets/templates/corpse.png' ,grayscale=False, confidence=.75)
        if postion :
            pyautogui.click()
        
    def checkCurrent(img , confidence ,timeout = 20):
        pos.found_pos(img , confidence ,timeout)




if __name__ == "__main__" : 

    # target = pos.found_get(["assets/templates/a5_town/a5_town_0.png"] , .7)
    # m = MoveHandler(targetname = ["assets/npc/malah/malah_name_tag_white.png" ])
    # m = MoveHandler(targetname = "assets/templates/a5_town/a5_town_4.png")
    testTargetPos = TargetPos("assets/templates/a5_town/a5_town_3.png" , (51,135))
   
    # a5_start_to_malah  a5_malah_to_start  a5_start_to_redDoor  assets/templates/pindle/pindle_8.pnge
    
    # m.adjust(testTargetPos)
    m = MoveHandler(targetprocess= TargetProcess.a5_store_to_redDoor())
    print(m.targetprocess.start_target)
    # m = MoveHandler(targetprocess= TargetProcess.a5_start_to_store())
    m.pickitems(20 , 0.2)
    # t1 = m.runTargetProcess()
    # if t1 :
    #     t2 = m.put_store(2)
    #     if t2 :
    #         m.targetprocess = TargetProcess.a5_store_to_redDoor()
    #         t3 = m.runTargetProcess()
    # m.test(testTargetPos)
    # m.test(testTargetPos)
    # m.pickitems(20,0.2)
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
