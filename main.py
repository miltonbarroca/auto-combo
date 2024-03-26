import threading
import pyautogui as pg
import time
from pynput import keyboard as kb
import random
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

class MeuPrograma:
    def __init__(self):
        self.executando = False
        self.pausado = False
        self.listener = None

    def iniciar(self):
        self.listener = kb.Listener(on_press=self.on_press)
        self.listener.start()

        print("Pressione '=' para iniciar o programa.")

    def loop_kill_box(self):
        while self.executando:
            if not self.pausado:
                kill_box()
            time.sleep(1)

    def mana_check_loop(self, image_path):
        while self.executando:
            if not self.pausado:
                mana_check(image_path)
            time.sleep(1)

    def on_press(self, key):
        try:
            if key.char == '=' and not self.executando:
                self.executando = True
                print("Programa iniciado")

                threading.Thread(target=self.loop_kill_box).start()
                threading.Thread(target=self.mana_check_loop, args=('img/mana_cheia.jpg',)).start()
            elif key.char == 'p':
                self.pausado = not self.pausado
                print("Programa pausado" if self.pausado else "Programa retomado")
            elif key.char == 'o':
                self.encerrar()
                print("Programa encerrado")
        except AttributeError:
            pass

    def encerrar(self):
        self.executando = False
        self.pausado = False
        self.listener.stop()

def kill_box():
    if programa.pausado:
        return
    pg.press('9')
    if programa.pausado:
        return
    time.sleep(random.uniform(2, 2.5))
    pg.press('space')
    pg.press('8')
    if programa.pausado:
        return
    time.sleep(random.uniform(2, 2.5))
    pg.press('9')
    if programa.pausado:
        return
    time.sleep(random.uniform(2, 2.5))
    pg.press('0')
    if programa.pausado:
        return
    pg.press('space')
    time.sleep(random.uniform(2, 2.5))

if __name__ == "__main__":
    programa = MeuPrograma()
    programa.iniciar()
    programa.listener.join()
