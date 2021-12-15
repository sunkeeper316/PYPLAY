import pyautogui

wincenter : tuple

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
                
                wincenter = (play_pos.x, play_pos.y + 375)
                print(wincenter)
                pyautogui.moveTo(wincenter)
                break
                # return  pyautogui.center(play_pos)

def funnd_get(*args) :

    for a in args :
        print(a)