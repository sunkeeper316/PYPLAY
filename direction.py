import pos
import pyautogui



def goLeftDown():
    wincenter = pos.found_d2rwin()
    pyautogui.moveTo(wincenter)
    pyautogui.moveRel(-100, 100)


def goRightDown():
    wincenter = pos.found_d2rwin()
    pyautogui.moveTo(wincenter)
    pyautogui.moveRel(100, 100)


def goLeft():
    wincenter = pos.found_d2rwin()
    pyautogui.moveTo(wincenter)
    pyautogui.moveRel(-100, 0)


def goRight():
    wincenter = pos.found_d2rwin()
    pyautogui.moveTo(wincenter)
    pyautogui.moveRel(100, 0)


def goDown():
    wincenter = pos.found_d2rwin()
    pyautogui.moveTo(wincenter)
    pyautogui.moveRel(0, 100)


def goUp():
    wincenter = pos.found_d2rwin()
    pyautogui.moveTo(wincenter)
    pyautogui.moveRel(0, -100)

def getDirection(direction) :
    if direction == "goLeftDown" :
        goLeftDown() 
    elif direction == "goRightDown" :
        goRightDown()
    elif direction == "goLeft" :
        goLeft()
    elif direction == "goRight" :
        goRight()
    elif direction == "goDown" :
        goDown()
    elif direction == "goUp" :
        goUp()