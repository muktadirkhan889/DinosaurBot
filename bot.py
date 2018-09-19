from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *
from timeit import default_timer as timer

speed = 0
class Coordinates():
    replayBtn = (479,454)
    dinosaur = (189,490)#461
    #271,489 = coordinate to check for the tree
    #474 = y coordinate

def restartGame():
    pyautogui.click(Coordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.09)
    print("Jump")
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    #60
    box = (Coordinates.dinosaur[0]+80+speed,Coordinates.dinosaur[1],Coordinates.dinosaur[0]+170+speed,Coordinates.dinosaur[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    # print(a.sum())
    return (a.sum())

def main():
    start = time.time()
    restartGame()
    while True:
        end = time.time()
        # print(int(end-start))
        if int(end-start)==4 :
            start = time.time()
            global speed
            speed+=3
            print("speed increased")
        print(speed)
        if(imageGrab()!=697):
            pressSpace()


main()


