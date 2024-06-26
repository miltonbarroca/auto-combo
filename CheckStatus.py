import pyautogui as pg
import time
import cv2
import numpy as np

def encontrar_imagem(image_path):
    screen = pg.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    
    if loc[0].size > 0:
        return True
    else:
        return False

def mana_check(image_path):
    if encontrar_imagem(image_path):
        print("Mana está cheia!")
    else:
        print("Mana não está cheia. Pressionando 3...")
        pg.press('3')

