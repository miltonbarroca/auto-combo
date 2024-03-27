import pyautogui as pg
import time
from pynput.keyboard import Key, Controller

def teste():
    while True:
        box = pg.locateOnScreen('img/mana_region.jpg')
        print(box)

teste()