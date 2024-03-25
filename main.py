import threading
import pyautogui as pg
import time
from pynput import keyboard as kb
import random

class MeuPrograma:
    def __init__(self):
        self.executando = False
        self.pausado = False
        self.listener = None

    def iniciar(self):
        self.listener = kb.Listener(on_press=self.on_press)
        self.listener.start()

        print('Aguardando pela tecla "=" para iniciar...')

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
    programa.listener.join()  # Esperar até que a thread do listener termine
