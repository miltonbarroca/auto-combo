import threading
import pyautogui as pg
import time
from pynput import keyboard as kb
import random
import cv2
import numpy as np
from pynput.keyboard import Key, Controller

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
        print("Mana está vazia! Pressionando 3...")
        pg.press('3')
    else:
        print("Mana está cheia")
        
def vida_check(image_path):
    if encontrar_imagem(image_path):
        print("Vida não está cheia! Pressionando 1...")
        pg.press('1')
    else:
        print("Vida está cheia. ")
        
def exura_check(image_path):
    if encontrar_imagem(image_path):
        print("Vida não está cheia! Pressionando 2...exec exura")
        pg.press('2')
    else:
        print("Vida está cheia. ...sem exura")     

def ring_check(image_path):
    if encontrar_imagem(image_path):
        print("Sem Ring. Colocando ring..press 5")
        pg.press('5')
    else:
        print("Ring OK!") 
        
def colar_check(image_path):
    if encontrar_imagem(image_path):
        print("Sem Colar. Colocando Colar..press 6")
        pg.press('6')
    else:
        print("Colar OK!") 

class MeuPrograma:
    def __init__(self):
        self.executando = False
        self.pausado = False
        self.listener = None
        self.pausadocombo = False

    def iniciar(self):
        self.listener = kb.Listener(on_press=self.on_press)
        self.listener.start()

        print("Pressione '=' para iniciar o programa.")

    def loop_kill_box(self):
        while self.executando:
            if not self.pausadocombo:
                kill_box()
            time.sleep(1)

    def mana_check_loop(self, image_path):
        while self.executando:
            if not self.pausado:
                mana_check(image_path)
            time.sleep(0.9)

    def vida_check_loop(self, image_path):
        while self.executando:
            if not self.pausado:
                vida_check(image_path)
            time.sleep(0.6)
            
    def exura_check_loop(self, image_path):
        while self.executando:
            if not self.pausado:
                exura_check(image_path)
            time.sleep(0.5)
            
    def ring_check_loop(self, image_path):
        while self.executando:
            if not self.pausado:
                ring_check(image_path)
            time.sleep(6)
            
    def colar_check_loop(self, image_path):
        while self.executando:
            if not self.pausado:
                colar_check(image_path)
            time.sleep(5)
            
    def on_press(self, key):
        try:
            if key.char == '=' and not self.executando:
                self.executando = True
                print("Programa iniciado")

                threading.Thread(target=self.loop_kill_box).start()
                threading.Thread(target=self.mana_check_loop, args=('img/mana_vazia_actionbar.png',)).start()
                threading.Thread(target=self.vida_check_loop, args=('img/life_vazia_actionbar.png',)).start()
                threading.Thread(target=self.exura_check_loop, args=('img/exura_life_vazia_actionbar.png',)).start()
                threading.Thread(target=self.ring_check_loop, args=('img/slot_ring.png',)).start()
                threading.Thread(target=self.colar_check_loop, args=('img/slot_colar.png',)).start()
            elif key.char == 'p':
                self.pausado = not self.pausado
                print("Programa pausado" if self.pausado else "Programa retomado")
            elif key.char == '[':
                self.pausadocombo = not self.pausadocombo
                print("Combo pausado" if self.pausadocombo else "Combo retomado")
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
    if programa.pausadocombo:
        return
    pg.press('9')
    if programa.pausadocombo:
        return
    time.sleep(random.uniform(2, 2.5))
    pg.press('8')
    pg.press('space')
    pg.press('4')
    if programa.pausadocombo:
        return
    time.sleep(random.uniform(2, 2.5))
    pg.press('9')
    if programa.pausadocombo:
        return
    time.sleep(random.uniform(2, 2.5))
    pg.press('0')
    if programa.pausadocombo:
        return
    pg.press('space')
    pg.press('4')
    if programa.pausadocombo:
        return
    time.sleep(random.uniform(2, 2.5))
    get_loot()
    
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
    time.sleep(0.1)
    for coord in loot_coordinates:
        pg.click(x=coord[0], y=coord[1], button='right')
    time.sleep(0.1)
    keyboard.release(Key.shift)
    
if __name__ == "__main__":
    programa = MeuPrograma()
    programa.iniciar()
    programa.listener.join()


