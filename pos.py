import pyautogui
from queue import Queue

wincenter : tuple = ()

def found_start():
    
        while 1 :
            play_pos = pyautogui.locateOnScreen('assets/templates/play_btn.png',grayscale=True, confidence=.8 )
            play_gary_pos = pyautogui.locateOnScreen('assets/templates/play_btn_gray.png' ,grayscale=True, confidence=.8)

            if  play_pos or  play_gary_pos :
                print(play_pos)

                print(play_gary_pos)
                if play_pos :
                    return  pyautogui.center(play_pos)
                elif play_gary_pos :
                    return pyautogui.center(play_gary_pos)

def found_pos(img):
    
        while 1 :
            play_pos = pyautogui.locateOnScreen(f'assets/templates/{img}.png',grayscale=True, confidence=.8 )

            if  play_pos  :
                return  pyautogui.center(play_pos)
                    
def found_d2rwin():
    
        while 1 :
            play_pos = pyautogui.locateOnScreen(f'assets/win/d2wintitle.png',grayscale=True, confidence=.8 )

            if  play_pos  :
                global wincenter
                center = pyautogui.center(play_pos)
                wincenter = (center.x, center.y + 375)
                print(wincenter)
                pyautogui.moveTo(wincenter)
                break
                # return  pyautogui.center(play_pos)

def funnd_get(args:list , q:Queue) :

    while 1 :
        for a in args :
            a_pos = pyautogui.locateOnScreen(f'assets/{a}.png',grayscale=True, confidence=.8 )
            if a_pos :
                print(F"發現座標 {a_pos}")
                q.put(pyautogui.center(a_pos))
                return pyautogui.center(a_pos)
            
def found_twon(list:list) :
    while 1 :
        for l in list :
            l_pos = pyautogui.locateOnScreen(f'{l}',grayscale=True, confidence=.8 )
            if l_pos :
                return {"path":l , "pos":l_pos}