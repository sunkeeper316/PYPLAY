import pos
import threading
import sched
import time
import math
import pyautogui

class MoveHandler :

    def __init__(self  ,targetname, target = pos.found_d2rwin() , center = pos.found_d2rwin()  ):
        self.center = center
        self.target = target
        self.targetname = targetname
        self.dist = -1
        self.isSearch = False

    def getDist(self) :

        while 1 :
            self.center = pos.found_d2rwin()
            print(f"target {self.target}")
            print(f"center {self.center}")
            self.target = pos.found_get(self.targetname , .6)
            self.dist = math.dist(self.center , self.target)
            print(self.dist)
            time.sleep(0.5)
        return
    def move(self) :
        
        # self.target = pos.found_get(["assets/templates/a5_town/a5_town_0.png"] , .7)

        # s = sched.scheduler(time.time ,time.sleep)
        # s.enter(2,1,)
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
    
    



if __name__ == "__main__" : 
    # target = pos.found_get(["assets/templates/a5_town/a5_town_0.png"] , .7)
    # m = MoveHandler(targetname = ["assets/npc/malah/malah_name_tag_white.png" ])
    m = MoveHandler(targetname = ["assets/templates/a5_town/a5_town_1.png" ])
    # malah_name_tag_white
    # m = MoveHandler(targetname = ["assets/npc/malah/malah_45.png" , "assets/npc/malah/malah_back.png" , "assets/npc/malah/malah_front.png" , "assets/npc/malah/malah_side.png" , "assets/npc/malah/malah_side_2.png"])
    # m.search()
    m.move()
