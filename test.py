import math
import random
from cv2 import TermCriteria_COUNT
import cv2
import keyboard
import os
import mss
from PIL import Image
# import displaymap
import cv2
import numpy as np
import pytesseract
import pyautogui
import threading
# import datetime
# from itertools import count
import time
# import sched
# from numpy import datetime64
import pos
# import task

# pos.found_d2rwin

# t = task.Task()

# t.a5_wpATK()
def found_zero():
        print("尋找原點")
        while 1 :
            play_pos = pyautogui.locateCenterOnScreen(f'tests/zero.png',grayscale=True, confidence=.8 )

            if  play_pos  :
                print("找到D2視窗中心")
                
                # pyautogui.moveTo(wincenter)
                return play_pos
                # return  pyautogui.center(play_pos)

def getPosition() :
    while 1 :
        print(f"found_center{pos.found_center()}")
        center = pos.found_center()
        m_p = pyautogui.position()
        print(( m_p[0] - center[0]  , m_p[1] - center[1]))
        # pyautogui.press('e')
        time.sleep(0.5)
    
def main() :
    while 1 :
        if keyboard.is_pressed('e') :
            print("keyboard press e")
            # play[1] += 1
            # print(play)
        elif keyboard.is_pressed('w') :
            print("keyboard press w")
            # play[0] += 1
            # print(play)
        elif keyboard.is_pressed('d') :
            print("keyboard press d")
            
            # print(f"d show :{Player.dist}")
        elif keyboard.is_pressed('q') :
            os._exit(1)
        time.sleep(0.1)   


def getMouse() :
    t = threading.Thread(target=getPosition)
    t.start()

def testRun(show):
    print(f"testRun show: {show}")

def testCallback( run ,callback) :
    for r in range(1,run) :
        callback(r)
def methodT1(a ,*b , **c) :
    print(a)
    print(b)
    print(c)
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
def show(imgarray) :
    cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input", imgarray)
    hsv = cv2.cvtColor(imgarray, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([0,43,46])
    high_hsv = np.array([10,255,255])
    mask = cv2.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
    cv2.imshow("test",mask)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
            
def getColor() :
    sct = mss.mss()
    imgarray = np.array(sct.grab((0 , 0 , 300 , 400)))
    # img = pyautogui.screenshot()
    # imgarray = np.array(img)

    # cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
    # cv2.imshow("input", imgarray)
    hsv = cv2.cvtColor(imgarray, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([0,43,46])
    high_hsv = np.array([10,255,255])
    mask = cv2.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
    cv2.imshow("test",mask)
    # t = threading.Thread(target=show ,args=(imgarray,))
    # t.start()
    cv2.imshow("test",mask)
    cv2.waitKey(1)
    # print(mask)
    for pixels in mask :
        # check = False
        # shows = []
        if 255 in pixels :
            return True
        
    return False




def found_img(img , confidence ,timeout = 20):
        start = time.time()
        while (time.time() - start) < timeout:
            print(f"搜尋{img}")
            _pos = pyautogui.locateOnScreen(
                f'{img}', grayscale=True, confidence=confidence)

            if _pos:
                print(f"找到目標")
                return _pos
            # time.sleep(0.03)
        return None

def put_store(benchmark, row ) :

        # center = pos.found_center()
        pyautogui.keyDown('ctrl')
        for i in range(0 , row) :
            for j in range(0 , 4) :
                print((benchmark[0]  + i * 40,benchmark[1]  + j * 40))
                grid = pyautogui.locateOnScreen('assets/templates/grid.png',grayscale=False, confidence=.75 , region=( benchmark[0]  + i * 37 , benchmark[1]  + j * 37 , 45 , 45))
                print(grid)
                if not grid :
                    print("放入倉庫")
                    pyautogui.moveTo((benchmark[0]  + i * 35  ,benchmark[1]  + j * 35 ) , duration = 0.2)
                    time.sleep(0.3)
                    pyautogui.click()
                    time.sleep(0.3)
                    
        pyautogui.keyUp('ctrl')
        time.sleep(0.3)
        pyautogui.press('esc')
        time.sleep(0.3)
        return True
def testGetColor():
    while 1 :
        getpos = pyautogui.position()

def found_color(img , low , high) :
    imgarray = np.array(img)
    imgarray = cv2.cvtColor(imgarray, cv2.COLOR_RGB2BGR)
    cv2.namedWindow("input" , cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input" , imgarray)
    hsv = cv2.cvtColor(imgarray , cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv , lowerb=np.array(low) , upperb=np.array(high) )

    cv2.imshow("mask" , mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    count = 0
    for pixels in mask :
        if 255 in pixels :
            count += 1
            
    print(f"funod {count}")
    if count > 20 :
        return True
    
    return False


if __name__ == "__main__" :
    # img = Image.open('assets/items/bl__magic_boneweave.png')
    # text = pytesseract.image_to_string(img, lang='eng')

    
    # print(text)

    for i in range(1 , 10000) :
        if i % 2 == 0 :
            print(i)
    # print(getColor())
    # for x in range(0,1280) :
    #     for y in range(0,720) :
    #         print(f"{x},{y}")

    # sct = mss.mss()
    # sct.grab()
    # for i in range(0 , 2) :
    #     # print(f"x:{i * 42}")