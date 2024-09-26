import time

from pynput.keyboard import Key
from pynput.keyboard import Controller


while True:
    time.sleep(30)
    ctrl = Key.ctrl
    keyboard = Controller()
    keyboard.press(ctrl)
    keyboard.release(ctrl)

