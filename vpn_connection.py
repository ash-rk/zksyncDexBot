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

class VPNConnection:
    def __init__(self):
        self.coordinates = {
            'NORD': (1528, 17, 0.5),
            'NORD_SEARCH': (1543, 175, 0.5),
            'NORD_DISCONNECT': (1581, 128, 0.5),
            # Add more coordinates related to VPN as needed
        }
    
    def _move_to_click(self, position):
        """Helper method to move and click on a specific position."""
        if position not in self.coordinates:
            print(f"Unknown symbol: {position}")
            return

        x, y, delay = self.coordinates[position]

        # Randomizing the duration by +20% to +100%
        random_duration_multiplier = 1 + random.uniform(0.20, 1.00)
        random_delay = delay * random_duration_multiplier

        pyautogui.moveTo(x, y, duration=random_delay)
        pyautogui.click(clicks=1)

    # ENABLE VPN    
    def enable_vpn(self):
        # Avoid Hong Kong for slow speed
        countries = ["United Kingdom", "Singapore", "Switzerland", "Canada", "Hong Kong", "Turkey", "Australia"]
        random_index = random.randint(0, len(countries)-1)
        country = countries[random_index]
        print(f"Selected country: {country}")
        self._move_to_click('NORD')
        time.sleep(1) 
        self._move_to_click('NORD_SEARCH')
        pyautogui.hotkey('command', 'a', interval=0)
        pyautogui.press('backspace', presses=1)
        pyautogui.write(country, interval=0)
        pyautogui.move(-50, 70, 0)
        time.sleep(1)
        pyautogui.click(clicks=1)
        time.sleep(4)
        # connected_location = pyautogui.locateOnScreen('connected.png', region=(2784, 100, 152, 52))
        # # ^CX: 1222 Y:   64
        # print(f"location: {connected_location[0]/2}, {connected_location[1]/2}")
        # print("VPN connected successfully :)" if connected_location is not None else "VPN connection unsuccessful :(")
        index = 0  # Make sure to initialize index
        connected_location = pyautogui.locateOnScreen('connected.png', region=(2763, 87, 228, 78))

        while connected_location is None and index < 4:
            print("Waiting for VPN to connect")
            connected_location = pyautogui.locateOnScreen('connected.png', region=(2763, 87, 228, 78))
            time.sleep(5)
            index = index + 1
        print("VPN connected successfully :)" if connected_location is not None else "VPN connection unsuccessful :(")


    def disconnect_vpn(self):
        self._move_to_click('NORD_DISCONNECT')

# Usage example:
# vpn = VPNConnection()
# vpn.enable_vpn()
