import pyautogui as pg
import time
from pynput.keyboard import Key, Controller

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
