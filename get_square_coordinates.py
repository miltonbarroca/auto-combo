import pyautogui as pg
from pynput.keyboard import Listener, Key

def on_press(key):
    pass

def on_release(key):
    global upper_left, lower_right, step
    if key == Key.space:
        if step == 0:
            upper_left = pg.position()
            print(f"Canto superior esquerdo: {upper_left}")
            step = 1
        elif step == 1:
            lower_right = pg.position()
            print(f"Canto inferior direito: {lower_right}")
            step = 2
            listener.stop()

print("Posicione o mouse no canto superior esquerdo do quadrado e pressione a tecla Space.")
step = 0
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()

x = min(upper_left[0], lower_right[0])
y = min(upper_left[1], lower_right[1])
width = abs(upper_left[0] - lower_right[0])
height = abs(upper_left[1] - lower_right[1])

print(f"Coordenadas: (x={x}, y={y}), Largura={width}, Altura={height}")
