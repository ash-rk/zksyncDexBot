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

class Planner:
    def __init__(self):
        pass
    
    def select_dex(self):
        # Onchain trade not working with VPN
        # Velocore redesigned
        dexes = ["syncswap", "velocore", "onchaintrade", "pancakeswap"]
        # dexes = ["syncswap",  "pancakeswap"]
        selected_dex = random.choice(dexes)
        return selected_dex
        # return "syncswap"