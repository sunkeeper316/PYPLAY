import pyautogui
import time
import pos
import threading
from pos import wincenter
from queue import Queue
from displaymap import DisplayMap, ImgPath

class Task:
    def __init__(self,level = 0) :
        self.level = level
    
    pos.found_d2rwin()

    def commond(self , commond) :
        pyautogui.press('enter')
        pyautogui.write(f'\{commond}' , interval=0.3)
        pyautogui.press('enter')
        return

    def pickItem(self) :
        return

    def fix(self) :
        return

    def buy(self) :
        return

    def atk(self) : 
        return

    def moveSouth(self) :
        pyautogui.moveTo(wincenter)
        pyautogui.moveRel(0 , 100)
        pyautogui.keyDown('e')
        time.sleep(0.03)
        pyautogui.keyUp()
        return

        # moveSouth()
    
    def checkDisPlay(self,list:list)  :
        q = Queue
        t = threading.Thread( target=pos.funnd_get , ages = (list,q))
        t.daemon = True
        t.start()
        t.join()

        return q.get() 

    def checTOWNSTART(self) : 
        townpaths = [ImgPath.A1_TOWN_START,ImgPath.A2_TOWN_START,ImgPath.A3_TOWN_START,ImgPath.A4_TOWN_START,ImgPath.A5_TOWN_START]
        reslut = pos.found_twon(townpaths)
        if reslut["path"] == townpaths[0] :
            return DisplayMap.A1_TOWN_START
        elif reslut["path"] == townpaths[1] :
            return DisplayMap.A2_TOWN_START
        elif reslut["path"] == townpaths[2] :
            return DisplayMap.A3_TOWN_START
        elif reslut["path"] == townpaths[3] :
            return DisplayMap.A4_TOWN_START
        elif reslut["path"] == townpaths[4] :
            return DisplayMap.A5_TOWN_START
        
        

        
        

        



