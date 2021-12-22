import pyautogui
from queue import Queue
import time

wincenter: tuple = ()


def found_start():

    while 1:
        play_pos = pyautogui.locateOnScreen(
            'assets/templates/play_btn.png', grayscale=True, confidence=.8)
        play_gary_pos = pyautogui.locateOnScreen(
            'assets/templates/play_btn_gray.png', grayscale=True, confidence=.8)

        if play_pos or play_gary_pos:
            print(play_pos)

            print(play_gary_pos)
            if play_pos:
                return pyautogui.center(play_pos)
            elif play_gary_pos:
                return pyautogui.center(play_gary_pos)


# def found_pos(img , confidence):
#     start = time.time()
#     while (time.time() - start) < 20:
#         _pos = pyautogui.locateCenterOnScreen(
#             f'{img}', grayscale=True, confidence=confidence)

#         if _pos:
#             return _pos
#         time.sleep(0.05)
#     return None
def found_pos(img , confidence ,timeout = 20):
    start = time.time()
    while (time.time() - start) < timeout:
        _pos = pyautogui.locateCenterOnScreen(
            f'{img}', grayscale=True, confidence=confidence)

        if _pos:
            return _pos
        time.sleep(0.05)
    return None

def found_pos_list(imgs , confidence):
    start = time.time()
    while (time.time() - start) < 20:
        for img in imgs :
            _pos = pyautogui.locateCenterOnScreen(f'{img}', grayscale=True, confidence=confidence)
            if _pos:
                return _pos
        time.sleep(0.05)
    return None

def found_center():
    print("尋找D2視窗中心")
    while 1:
        _pos = pyautogui.locateCenterOnScreen(
            f'assets/win/d2wintitle.png', grayscale=True, confidence=.8)
        if _pos:
            return (_pos.x, _pos.y + 375)

def found_d2rwin():
    print("尋找D2視窗中心")
    while 1:
        play_pos = pyautogui.locateOnScreen(
            f'assets/win/d2wintitle.png', grayscale=True, confidence=.8)

        if play_pos:
            global wincenter
            center = pyautogui.center(play_pos)
            wincenter = (center.x, center.y + 375)
            print(wincenter)
            print("找到D2視窗中心")

            # pyautogui.moveTo(wincenter)
            return wincenter
            # return  pyautogui.center(play_pos)





def funnd_get(list: list, q: Queue):

    while 1:
        for a in list:
            a_pos = pyautogui.locateOnScreen(
                f'assets/{a}.png', grayscale=True, confidence=.8)
            if a_pos:
                print(F"發現座標 {a_pos}")
                if q:
                    q.put(pyautogui.center(a_pos))

                return pyautogui.center(a_pos)


def found_get(list: list):

    while 1:
        for a in list:
            a_pos = pyautogui.locateOnScreen(
                f'{a}', grayscale=True, confidence=.7)
            if a_pos:
                print(F"發現座標 {a_pos}")

                return pyautogui.center(a_pos)


def found_get(list: list, confidence):
    while 1:
        for a in list:
            a_pos = pyautogui.locateOnScreen(
                f'{a}', grayscale=True, confidence=confidence)
            if a_pos:
                print(F"發現座標 {a_pos}")

                return pyautogui.center(a_pos)


def found_twon(list: list):
    while 1:
        for l in list:
            l_pos = pyautogui.locateOnScreen(
                f'{l}', grayscale=True, confidence=.8)
            if l_pos:
                return {"path": l, "pos": l_pos}
