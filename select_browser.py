import pyautogui
import time
import random
import pyperclip
import cv2
import os

import pyscreeze
import PIL

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

class SelectBrowser:
    def __init__(self):
        pass

    def trigger_spotlight(self):
        pyautogui.hotkey('command', 'space', interval=0.25)

    def open_brave(self):
        self.trigger_spotlight()
        pyautogui.write('Brave PRIVATE', interval=0.1)
        pyautogui.press('enter', presses=1)
        time.sleep(2)
