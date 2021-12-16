import pyautogui
import time

def shootImg(imgname,imgpos) :
    img = pyautogui.screenshot(f'{imgname}_{time.strftime("%Y%m%d_%H%M%S")}.png',region=imgpos)