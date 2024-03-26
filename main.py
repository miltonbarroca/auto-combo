import threading
import pyautogui as pg
import time
from pynput import keyboard as kb
import random

def exura():
    print('Executando Exura')
    while programa.executando:
        if not programa.pausado:
            try:
                if pg.pixelMatchesColor(759, 794, (73, 74, 74)):
                    pg.press('2') #hotkey exura
            except pg.FailSafeException:
                pass
        time.sleep(random.uniform(1.9, 2.8))  # Ajusta o delay conforme necessário

def mana():
    print('Verificando Mana')
    while programa.executando:
        if not programa.pausado:
            try:
                if pg.pixelMatchesColor(1073, 794, (121, 121, 121)):
                    pg.press('3') #hotkey pot mana
            except pg.FailSafeException:  
                pass
        time.sleep(random.uniform(2.3, 2.8))  # Ajusta o delay conforme necessário

def life():
    print('Verificando Life')
    while programa.executando:
        if not programa.pausado:
            try:
                if pg.pixelMatchesColor(605, 792, (69, 70, 70)):
                    pg.press('1') #hotkey pot vida
            except pg.FailSafeException:
                pass
        time.sleep(1) # Ajusta o delay conforme necessário

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

    def on_press(self, key):
        try:
            if key.char == '=' and not self.executando:
                self.executando = True
                print("Programa iniciado")

                threading.Thread(target=self.loop_kill_box).start()
                threading.Thread(target=exura).start()  
                threading.Thread(target=mana).start()   
                threading.Thread(target=life).start()   
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