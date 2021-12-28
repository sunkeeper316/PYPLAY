import pyautogui
from queue import Queue
import time

def found_pos(img , confidence ,timeout = 20):
    start = time.time()
    while (time.time() - start) < timeout:
        _pos = pyautogui.locateCenterOnScreen(
            f'{img}', grayscale=True, confidence=confidence)

        if _pos:
            return _pos
        time.sleep(0.01)
    return None

def found_pos_list(imgs , confidence):
    start = time.time()
    while (time.time() - start) < 20:
        for img in imgs :
            _pos = pyautogui.locateCenterOnScreen(f'{img}', grayscale=True, confidence=confidence)
            if _pos:
                return _pos
        time.sleep(0.01)
    return None

def found_center():
    print("尋找D2視窗中心")
    while 1:
        _pos = pyautogui.locateCenterOnScreen(
            f'assets/win/d2wintitle.png', grayscale=True, confidence=.8)
        if _pos:
            return (_pos.x, _pos.y + 375)


def found_twon(list: list):
    while 1:
        for l in list:
            l_pos = pyautogui.locateOnScreen(
                f'{l}', grayscale=True, confidence=.8)
            if l_pos:
                return {"path": l, "pos": l_pos}
