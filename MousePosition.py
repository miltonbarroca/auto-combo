import pyautogui
from pynput import keyboard

def on_space_pressed(key):
    if key == keyboard.Key.space:
        x, y = pyautogui.position()
        rgb = pyautogui.pixel(x, y)
        print(f"Coordenadas do mouse: ({x}, {y}), RGB: {rgb}")

print("Pressione a tecla de espaço para obter as coordenadas e a cor RGB do mouse...")

with keyboard.Listener(on_press=on_space_pressed) as listener:
    listener.join()
