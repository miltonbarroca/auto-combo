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
        time.sleep(1.9)  # Ajusta o delay conforme necessário

def mana():
    print('Verificando Mana')
    while programa.executando:
        if not programa.pausado:
            try:
                while not pg.locateOnScreen('img/mana_cheia.jpg'):
                    pg.press('3')  # Pressiona a tecla "3"
                    time.sleep(0.1)  # Espera um curto período antes de verificar novamente
            except pg.FailSafeException:  
                pass
        time.sleep(2.1)  # Ajusta o delay conforme necessário

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
                threading.Thread(target=exura).start()  # Inicia a função exura em uma thread separada
                threading.Thread(target=mana).start()   # Inicia a função mana em uma thread separada
                threading.Thread(target=life).start()   # Inicia a função life em uma thread separada
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
