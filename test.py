import math
import keyboard
import os
# import displaymap
# import cv2
# import numpy as np
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

if __name__ == "__main__" :
    testCallback(3,callback =testRun)
    keyboard.add_hotkey('e', lambda: testRun("got key e"))

    while 1 :
        a = 1
    # zero = (0,0)
    # a_pos = (640,360)
    # b_pos = (54,80)
    # _hypot =eee math.hypot(30,40)
    # d = math.dist(a_pos , b_pos)
    
    # print(f"a_pos 距離 {math.dist(a_pos,zero)}")
    # print(math.hypot(a_pos[0] ,a_pos[1] ))
    # print(math.hypot(b_pos[0] ,b_pos[1] ))

    # getMouse()

    # center = found_zero()
    # while 1 :
    #     square_pos = pyautogui.locateCenterOnScreen('tests/Square.png')
    #     if square_pos :
    #         print(f"square_pos {square_pos}")
    #         break

    
    



# def jop() :
#     now = datetime.datetime.now()
#     ts = now.strftime('%Y/%m/%d %H:%M:%S')
#     print(f"now {ts}")

# def loopTest() :
#     s = sched.scheduler(time.time , time.sleep)
#     s.enter(2,1,jop , ())
#     s.run()
    
# def timerGO() :
#     timer = threading.Timer(2 , jop)
#     timer.start()
# if __name__ == "__main__" :
#     count = 0
#     while count < 5 :
#         count += 1
#         loopTest()
    # timerGO()
    


# # displaymap.read_directory("assets/wp/")

# # 開啟網路攝影機
# cap = cv2.VideoCapture(0)

# # 設定影像尺寸
# width = 1280
# height = 960

# # 設定擷取影像的尺寸大小
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# # 計算畫面面積
# area = width * height

# # 初始化平均影像
# ret, frame = cap.read()
# avg = cv2.blur(frame, (4, 4))
# avg_float = np.float32(avg)

# while(cap.isOpened()):
#   # 讀取一幅影格
#   ret, frame = cap.read()

#   # 若讀取至影片結尾，則跳出
#   if ret == False:
#     break

#   # 模糊處理
#   blur = cv2.blur(frame, (4, 4))

#   # 計算目前影格與平均影像的差異值
#   diff = cv2.absdiff(avg, blur)

#   # 將圖片轉為灰階
#   gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

#   # 篩選出變動程度大於門檻值的區域
#   ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

#   # 使用型態轉換函數去除雜訊
#   kernel = np.ones((5, 5), np.uint8)
#   thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
#   thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

#   # 產生等高線
#   cntImg, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#   for c in cnts:
#     # 忽略太小的區域
#     if cv2.contourArea(c) < 2500:
#       continue

#     # 偵測到物體，可以自己加上處理的程式碼在這裡...

#     # 計算等高線的外框範圍
#     (x, y, w, h) = cv2.boundingRect(c)

#     # 畫出外框
#     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#   # 畫出等高線（除錯用）
#   cv2.drawContours(frame, cnts, -1, (0, 255, 255), 2)

#   # 顯示偵測結果影像
#   cv2.imshow('frame', frame)

#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

#   # 更新平均影像
#   cv2.accumulateWeighted(blur, avg_float, 0.01)
#   avg = cv2.convertScaleAbs(avg_float)

# cap.release()
# cv2.destroyAllWindows()v
