import pyautogui as pg
import time
from pynput.keyboard import Key, Controller

loot_coordinates = [
    (857, 382),
    (921, 389),
    (986, 389),
    (991, 459),
    (990, 520),
    (917, 516),
    (860, 520),
    (857, 452)
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
