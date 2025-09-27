# run the following command to activate the venv for Windows: 
# Set-ExecutionPolicy Unrestricted -Scope Process
# .\env\Scripts\Activate

# for Linux:
# source env/bin/activate

import os
import sys
from pynput import mouse, keyboard
from creategif import create_gifs_from_pngs
from window import FoxWindow

global win
global pressed_keys

def on_click(x, y, btn, pressed):
    win.m_click(x, y, pressed)

def on_press(key):
    if getattr(key, "vk", None) == 191:
        exit()

def on_release(key):
    pressed_keys.discard(key)

def exit():
    m_listener.stop()
    kb_listener.stop()
    win.destroy()
    print("Program terminated")
    sys.exit()

if __name__ == "__main__":
    if not os.path.exists("./fox/f.gif") or not os.path.exists("./fox/l.gif") or not os.path.exists("./fox/r.gif"): create_gifs_from_pngs()

    win = FoxWindow(42, 24, "Foxle")

    m_listener = mouse.Listener(on_click=on_click)
    m_listener.start()

    pressed_keys = set()
    kb_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    kb_listener.start()

    win.start()