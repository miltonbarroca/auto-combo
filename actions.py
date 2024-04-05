import pyautogui as pg
import Constants
from pynput.keyboard import Key, Controller
import time

def check_battle():
    try:
        pg.locateOnScreen('img/battle_vazio.png')
        print('Battle vazio,indo para proxima box...')
        return False 
    except pg.ImageNotFoundException:
        print('Monstros encontrados')
        return True

def hole_up(shloud_up,img_anchor,plus_x,plus_y):
    if shloud_up:
        box = pg.locateOnScreen(img_anchor, confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x + plus_x, y + plus_y)
            pg.press('F1')
            pg.click()

#hole_up('img/anchor_GT_alt_up.png',270,130)
def hole_down(should_down):
    if should_down:
        box = pg.locateOnScreen('hole_down.png',confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x,y)
            pg.click()
            pg.sleep(3)

def next_box(path,wait):
    flag = pg.locateOnScreen(path, confidence= 0.7,region=Constants.MINIMAP)
    if flag:
        x,y = pg.center(flag)
        pg.moveTo(x,y)
        pg.click()
        pg.sleep(wait)

loot_coordinates = [

    (891, 432),
    (835, 432),
    (778, 432),
    (778, 374),
    (778, 315),
    (835, 315),
    (891, 315),
    (891, 374)
]

def get_loot():
    print('Coletando loot...')
    keyboard = Controller()
    keyboard.press(Key.shift)
    time.sleep(0.1)  # Aguarda um curto período de tempo
    for coord in loot_coordinates:
        pg.click(x=coord[0], y=coord[1], button='right')
    time.sleep(0.1)  # Aguarda um curto período de tempo
    keyboard.release(Key.shift)
