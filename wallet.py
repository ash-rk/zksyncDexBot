import pyautogui
import time
import random
import pyperclip
import cv2
import os
from bs4 import BeautifulSoup

import pyscreeze
import PIL

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

class Wallet:
    def __init__(self):
        self.coordinates = {
            'URL_BAR': (369, 91, 1),
            'METAMASK': (1487, 88, 0.5),
            'METAMASK_COPY_ADDRESS': (1327, 202, 0.5),
            'METAMASK_LIST_ACCOUNTS': (1322, 135, 0.5),
            'METAMASK_SEARCH_ACCOUNTS': (1275, 206, 0.5),
            'METAMASK_SELECT_ACCOUNT': (1309, 273, 0.5),
            'ACCOUNT_EXPLORER_1': (1472, 135, 0.5),
            'ACCOUNT_EXPLORER_2': (1351, 225, 0.5),

            'DEBANK_SEARCH': (1156, 143, 0.5),
            'INSPECT_ELEMENT': (1156, 303, 0.5),
            'INSPECT_ELEMENT_CLOSE': (1703, 124, 0.5)
        }

        self.token_address_and_asset = {
            "0x000000000000000000000000000000000000800A": "ETH",
            "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4": "USDC",
            "0x75Af292c1c9a37b3EA2E6041168B4E48875b9ED5": "cbETH",
            "0x90973213E2a230227BD7CCAfB30391F4a52439ee": "eUSDC",
            "0x787c09494Ec8Bcb24DcAf8659E7d5D69979eE508": "MAV", #Maverick
            "0x85D84c774CF8e9fF85342684b0E795Df72A24908": "VC", #Velocore
            "0x5756A28E2aAe01F600FC2C01358395F5C1f8ad3A": "VS", #VeSync
            "0x240f765Af2273B0CAb6cAff2880D6d8F8B285fa4": "SWORD",
            "0x80115c708E12eDd42E504c1cD52Aea96C547c05c": "USDC/WETH cSLP", #Liquidity
            "0x0e97C7a0F8B2C9885C8ac9fC6136e829CbC21d42": "MUTE",
        }
        self.div_wallet = "card_card__i5VM9 TokenWallet_container__2Nxzq"
        self.asset_and_balance = {}

    def move_to_click(self, position):
        if position not in self.coordinates:
            print(f"Unknown symbol: {position}")
            return

        x, y, delay = self.coordinates[position]

        # Randomizing the duration by +20% to +100%
        random_duration_multiplier = 1 + random.uniform(0.20, 1.00)
        random_delay = delay * random_duration_multiplier

        pyautogui.moveTo(x, y, duration=random_delay)
        pyautogui.click(clicks=1)

    def login_metamask(self):
        self.move_to_click("METAMASK")
        loaded = self.locate_with_retries(os.path.join('images', 'metamask', 'welcome.png'))
        if not loaded:
            return
        key = '.secret'
        with open(key, 'r') as file:
            content = file.read()
            # print(content)
            time.sleep(2)
            pyautogui.write(content, interval=0.1)
        pyautogui.press('enter', presses=1)
        time.sleep(1)

    def select_account(self, selected_account):
        # 'METAMASK_COPY_ADDRESS': (1321, 200, 0.5),
        # 'METAMASK_LIST_ACCOUNTS': (1318, 135, 0.5),
        # 'METAMASK_SEARCH_ACCOUNTS': (1254, 254, 0.5),
        # 'METAMASK_SELECT_ACCOUNT': (1301, 321, 0.5),
        # self.move_to_click_random_duration("METAMASK_COPY_ADDRESS")
        self.move_to_click("METAMASK_LIST_ACCOUNTS")
        self.move_to_click("METAMASK_SEARCH_ACCOUNTS")
        pyautogui.write(selected_account, interval=0.1)
        pyautogui.moveTo(1301, 321, 0.5)
        self.gradual_scroll(10)
        self.move_to_click("METAMASK_SELECT_ACCOUNT")

    def gradual_scroll(self, amount, clicks=2, interval=0.0001):
        # Determine the direction of the scroll
        direction = 1 if amount > 0 else -1
        for _ in range(abs(amount)):
            pyautogui.scroll(direction * clicks)
            time.sleep(interval)

    def account_explorer(self):
        # position (1063, 532)
        # self.move_to_click("METAMASK")
        self.move_to_click('ACCOUNT_EXPLORER_1')
        self.move_to_click('ACCOUNT_EXPLORER_2')
        time.sleep(2)

    # Locate with retries
    def locate_with_retries(self, image_path, retries=3, delay=5):
        attempt = 0
        while attempt < retries:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                return location
            time.sleep(delay)
            attempt += 1
        return None

    # Fetch balance from debank
    def get_balance(self):
        metamask_open = self.locate_with_retries(os.path.join('images', 'debank', 'metamask_open.png'))
        if not metamask_open:
            self.move_to_click('METAMASK')
        time.sleep(2)
        print("Metamask already open" if metamask_open else "Opened metamask manually")
        self.move_to_click('METAMASK_COPY_ADDRESS')
        self.goto("https://debank.com/")
        time.sleep(2)
        # Account address copied
        wallet_address = pyperclip.paste()

        # locate search bar
        search_bar = self.locate_with_retries(os.path.join('images', 'debank', 'search_bar.png'))
        if not search_bar:
            return
        print("debank loaded successfully")
        self.simple_click(self.get_center(search_bar))
        # pyautogui.write(wallet_address, interval=0.1)
        pyautogui.hotkey('command', 'v', interval=0)
        time.sleep(2)
        pyautogui.press('enter', presses=1)
        time.sleep(3)

        # filter zkSync chain
        show_zksync_balances = self.locate_with_retries(os.path.join('images', 'debank', 'zksync.png'))
        if not show_zksync_balances:
            return
        self.simple_click(self.get_center(show_zksync_balances))
        print("Selected chain: zkSync Era", end=" ")
        time.sleep(1)

        # Inspect element, select element, parse & then get balance
        pyautogui.hotkey('command', 'option', 'i', interval=0)
        time.sleep(2)
        self.move_to_click('INSPECT_ELEMENT')
        time.sleep(1)
        pyautogui.hotkey('command', 'f', interval=0)
        pyperclip.copy(self.div_wallet)
        pyautogui.hotkey('command', 'v', interval=0)
        pyautogui.press('enter', presses=1)
        inspect_div = self.locate_with_retries(os.path.join('images', 'debank', 'inspect_div.png'))
        if not inspect_div:
            return
        self.simple_click(self.get_center(inspect_div))
        pyautogui.hotkey('command', 'c', interval=0)
        html_wallet_balance = pyperclip.paste()
        print(f"Account {wallet_address}")
        balance = self.wallet_balance_formatter(html_wallet_balance)
        self.move_to_click('INSPECT_ELEMENT_CLOSE')
        return balance

    def wallet_balance_formatter(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        # Locate all rows within the table body
        rows = soup.select('.db-table-wrappedRow')

        for row in rows:
            token_name_elem = row.select_one('.TokenWallet_detailLink__282Ky')
            if token_name_elem:
                token_name = token_name_elem.text
            else:
                token_name = None

            price_elem = row.select_one('.db-table-cell:nth-of-type(2)')
            if price_elem:
                price = price_elem.text
            else:
                price = None

            amount_elem = row.select_one('.db-table-cell:nth-of-type(3)')
            if amount_elem:
                amount = amount_elem.text
            else:
                amount = None

            usd_value_elem = row.select_one('.db-table-cell:nth-of-type(4)')
            if usd_value_elem:
                usd_value = usd_value_elem.text
            else:
                usd_value = None
            self.asset_and_balance[token_name] = float(amount.replace(",", ""))
            print(f"Token: {token_name}, Price: {price}, Amount: {amount}, USD Value: {usd_value}")
        return self.asset_and_balance
        # print(f"The final balance: {self.asset_and_balance}")

    def get_balance_explorer(self):
        # print(f"Asset: {self.token_address_and_asset.get(address)}")
        # self.simple_click((1159, 696), 0.5)
        print("Fetching balances")
        show_balances = pyautogui.locateOnScreen('show_all_balances.png', region=(2180, 1378, 270, 58))
        if show_balances:
            # print(f"Show all balances coordinates: {show_balances}")
            self.simple_click(self.get_center(show_balances))
            time.sleep(1)
        copy_address = pyautogui.locateOnScreen('copy_icon.png', region=(2806, 846, 144, 60))
        copy_location = self.get_center(copy_address)
        balance = pyautogui.locateOnScreen('balance.png', confidence=0.8)
        balance_center = self.get_center(balance)
        # print(f"Balance location: {balance}, Balance Center: {balance_center}")
        difference = balance_center[0] - copy_location[0]
        # print(f"Difference: {difference}")
        if copy_location:
            # print(f"Copy icon location: {copy_location}")
            self.simple_click(copy_location, 0.5)
            token_Address = pyperclip.paste()
            # print("Token address could not be found" if token_Address is None else "Address found")
            pyautogui.move(difference-15, -10, 0.5)
            pyautogui.click(button='right')
            pyautogui.click(button='left')
            time.sleep(0.5)
            pyautogui.hotkey('command', 'c')
            time.sleep(0.5)
            balance = pyperclip.paste()
            asset = self.token_address_and_asset.get(token_Address, 'Not Found')
            # print(f"Asset: {asset} Balance: {balance} Address: {token_Address}")
            if asset != 'Not Found':
                self.asset_and_balance[asset] = balance
            copy_address_down = 52 # Fixed for lower copy button clicks
            index = 1
            while True:
                if index == 1:
                    pyautogui.moveTo(copy_location[0], copy_location[1], (0.5*((index/1)+1))) # main copy icon
                    pyautogui.move(0, copy_address_down*index, 0.3)
                else:
                    pyautogui.moveTo(copy_location[0], copy_location[1]+(copy_address_down*index), (0.5*((index/10)+1)))
                pyperclip.copy('Ended')
                pyautogui.click(clicks=1)
                token_Address = pyperclip.paste()
                if token_Address == 'Ended':
                    print("\nExit reached, as no more addresses found")
                    break
                # print("Token address could not be found" if token_Address is None else "Address found")
                pyperclip.copy('None')
                pyautogui.move(difference-15, 6, 0.5)
                pyautogui.click(button='right')
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.hotkey('command', 'c')
                time.sleep(0.5)
                balance = pyperclip.paste()
                pyperclip.copy('Ended')
                asset = self.token_address_and_asset.get(token_Address, 'Not Found')
                if asset != 'Not Found':
                    self.asset_and_balance[asset] = balance
                # print(f"Asset: {asset} Balance: {balance} Address: {token_Address}")
                index = index + 1
            print(self.asset_and_balance)
            return self.asset_and_balance
        else:
            print("Couldn't locate copy icon")
            return 0

    def get_center(self,position):
        position = pyautogui.center(position)
        return((position[0]/2, position[1]/2))
    
    def simple_click(self, position, *args):
        x, y = position
        delay = args[0] if args else 0.5  # You can set a default delay value if needed

        # Randomizing the duration by +20% to +100%
        random_duration_multiplier = 1 + random.uniform(0.20, 1.00)
        random_delay = delay * random_duration_multiplier

        pyautogui.moveTo(x, y, duration=random_delay)
        pyautogui.click(clicks=1)

    def goto(self, address):
        self.move_to_click('URL_BAR')
        time.sleep(1)
        pyautogui.write(address, interval=0.1)
        pyautogui.press('enter', presses=1)