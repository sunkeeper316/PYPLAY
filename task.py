from sys import displayhook
import pyautogui
import time
import displaymap
from pyscreeze import center
import pos
import threading

from queue import Queue
from displaymap import DisplayMap, ImgPath

class Task:
    def __init__(self,level = 0) :
        self.level = level
    
        pos.found_d2rwin()

    def take_items(self) :
        pyautogui.press('alt')
        time.sleep(0.5)
        items = displaymap.read_directory("assets/items/")
        while 1 :

            for a in items :
                a_pos = pyautogui.locateOnScreen(f'{a}',grayscale=True, confidence=.7 )
                if a_pos : 
                    print('發現可以撿取物品')
                    center = pyautogui.center(a_pos)
                    pyautogui.moveTo(center)
                    time.sleep(0.5)
                    pyautogui.click()
                    time.sleep(0.5)
                    continue
            
            print('沒有發現')
            break
    def a5_wpATK(self) :
        
        
        wincenter = pos.found_d2rwin()
        pyautogui.moveTo(wincenter)
        pyautogui.moveRel(400 , -300)
        pyautogui.press('f3')
        time.sleep(0.5)
        pyautogui.press('f3')
        time.sleep(0.5)
        pyautogui.press('f3')
        time.sleep(0.5)
        pyautogui.moveTo(wincenter)
        pyautogui.moveRel(200 , -100)
        pyautogui.press('f2')
        time.sleep(1.5)
        pyautogui.press('f2')
        time.sleep(1.5)
        pyautogui.press('f2')
        time.sleep(1.5)
        pyautogui.press('f2')
        time.sleep(1.5)
        pyautogui.press('f2')
        time.sleep(1.5)
        self.take_items()

    def a5_moveToRedWp(self) :
        pyautogui.press('f5')
        time.sleep(0.3)
        wincenter = pos.found_d2rwin()
        pyautogui.moveTo(wincenter)
        pyautogui.moveRel(-100 , 100)
        pyautogui.keyDown('e')
        time.sleep(3)
        pyautogui.keyUp('e')
        pyautogui.moveTo(wincenter)
        pyautogui.moveRel(0 , 100)
        pyautogui.keyDown('e')
        time.sleep(1.5)
        pyautogui.keyUp('e')
        pyautogui.moveTo(wincenter)
        pyautogui.moveRel(-100 , 0)
        pyautogui.keyDown('e')
        time.sleep(1)
        pyautogui.keyUp('e')
        time.sleep(0.5)
        redwp = pos.found_getLV8(["assets/templates/a5_town/a5_town_7.png"])
        pyautogui.moveTo(redwp)
        time.sleep(1.5)
        redwp = pos.found_getLV8(["assets/templates/a5_red_portal_text.png"])
        pyautogui.click()
        print("進入洪門")
        # pos.found_getLV8(["assets/templates/a5_redwp_in_0.png"])
        print("確定已經洪門")
        time.sleep(1.5)
        self.a5_wpATK()


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
        wincenter = pos.found_d2rwin()
        pyautogui.moveTo(wincenter)
        pyautogui.moveRel(0 , 100)
        pyautogui.keyDown('e')
        time.sleep(0.03)
        pyautogui.keyUp('e')
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
        print("現在城鎮")
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
        
        

        
        

        



