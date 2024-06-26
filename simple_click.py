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

# python3 -m venv myenv
# source myenv/bin/activate
# Size(width=1728, height=1117)
# im1 = pyautogui.screenshot()
# im1.save('my_screenshot.png')
#  Eventually deprecate this class and file
class MouseAutomation:
    def __init__(self):
        self.coordinates = {
            'APPLE_SYMBOL': (21, 7, 1),
            'URL_BAR': (369, 91, 1),
            'NORD': (1528, 17, 0.5),
            'NORD_SEARCH': (1543, 175, 0.5),
            'NORD_DISCONNECT': (1581, 128, 0.5),
            'METAMASK': (1487, 88, 0.5),
            'METAMASK_COPY_ADDRESS': (1321, 200, 0.5),
            'METAMASK_LIST_ACCOUNTS': (1318, 135, 0.5),
            'METAMASK_SEARCH_ACCOUNTS': (1254, 254, 0.5),
            'METAMASK_SELECT_ACCOUNT': (1301, 321, 0.5),
            'ACCOUNT_EXPLORER_1': (1472, 135, 0.5),
            'ACCOUNT_EXPLORER_2': (1351, 225, 0.5),

            # SyncSwap getting started clicks
            'SYNC_SWAP_GETTING_STARTED_1': (866, 734, 0.5),
            'SYNC_SWAP_GETTING_STARTED_2': (407, 314, 0.5),
            'SYNC_SWAP_GETTING_STARTED_3': (1666, 317, 0.5),
            'SYNC_SWAP_GETTING_STARTED_4': (946, 776, 0.5),
            # SyncSwap connect to wallet
            'SYNC_SWAP_WALLET_1': (1602, 155, 0.5), # initial connect
            'SYNC_SWAP_WALLET_2': (643, 550, 0.5), # ethereum wallet
            'SYNC_SWAP_WALLET_3': (1276, 1026, 0.5), # next
            'SYNC_SWAP_WALLET_4': (1283, 1075, 0.5), # connect
            'SYNC_SWAP_SELL_TOKEN': (1017, 339, 0.5), # sell token
            'SYNC_SWAP_BUY_TOKEN': (1020, 490, 0.5), # buy token
            'SYNC_SWAP_VALUE_BAR': (676, 343, 0.5), # value bar
            'SYNC_SWAP_SEARCH_TOKEN': (737, 386, 0.5), # Search bar
            'SYNC_SWAP_SELECT_TOKEN': (796, 491, 0.5), # Select token from search bar
            'SYNC_SWAP_SWAP_BUTTON': (858, 654, 0.5), # Swap for trade

            # MUTE Dex coordinates
            'MUTE_1': (1620, 143, 0.5), # initial connect
            'MUTE_2': (795, 489, 0.5), # select metamask
            'MUTE_BUTTON_SELL_TOKEN': (990, 516, 0.5), # Sell token button
            'MUTE_BUTTON_SEARCH_ASSET': (808, 349, 0.5), # Search token bar
            'MUTE_BUTTON_BUY_TOKEN': (1006, 621, 0.5), # Sell token button
            'MUTE_BUTTON_SEARCH_RESULT': (856, 542, 0.5), # Select searched token result
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

        self.asset_and_balance = {}

        self.__primary_token = ["ETH", "USDC"]
        
    def print_screen_resolution(self):
        # current resolution: Size(width=1728, height=1117)
        print(pyautogui.size())
        
    def print_current_position_continuously(self, interval=0.5):
        print('Press Ctrl-C to quit.')
        try:
            while True:
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)
        except KeyboardInterrupt:
            print('\n')


    def wait(self, duration=2):
        time.sleep(duration)
        
    def print_current_position(self):
        print(pyautogui.position())
        
    def move_to_click(self, position):
        if position not in self.coordinates:
            print(f"Unknown symbol: {position}")
            return
        
        x, y, delay = self.coordinates[position]
        pyautogui.moveTo(x, y, duration=delay)
        pyautogui.click(clicks=1)

    def move_to_click_random_duration(self, position):
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
        self.move_to_click('NORD')
        time.sleep(1) 
        self.move_to_click('NORD_SEARCH')
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
        self.move_to_click('NORD_DISCONNECT')

    def gradual_scroll(self, amount, clicks=2, interval=0.0001):
        # Determine the direction of the scroll
        direction = 1 if amount > 0 else -1
        for _ in range(abs(amount)):
            pyautogui.scroll(direction * clicks)
            time.sleep(interval)
            
    def trigger_spotlight(self):
        pyautogui.hotkey('command', 'space', interval=0.25)
        
    def open_brave(self):
        self.trigger_spotlight()
        pyautogui.write('Brave PRIVATE', interval=0.1)
        pyautogui.press('enter', presses=1)
        time.sleep(2)

    def login_metamask(self):
        self.move_to_click("METAMASK")
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
        self.move_to_click_random_duration("METAMASK_LIST_ACCOUNTS")
        self.move_to_click_random_duration("METAMASK_SEARCH_ACCOUNTS")
        pyautogui.write(selected_account, interval=0.1)
        pyautogui.moveTo(1301, 321, 0.5)
        self.gradual_scroll(10)
        self.move_to_click_random_duration("METAMASK_SELECT_ACCOUNT")
 
    def account_explorer(self):
        # position (1063, 532)
        # self.move_to_click("METAMASK")
        self.move_to_click('ACCOUNT_EXPLORER_1')
        self.move_to_click('ACCOUNT_EXPLORER_2')
        time.sleep(2)

    def goto(self, address):
        self.move_to_click('URL_BAR')
        time.sleep(1)
        pyautogui.write(address, interval=0.1)
        pyautogui.press('enter', presses=1)

    def sync_swap_start(self):
        # SyncSwap getting started clicks
        self.goto("https://syncswap.xyz/")
        time.sleep(2)
        self.move_to_click_random_duration('SYNC_SWAP_GETTING_STARTED_1')
        self.move_to_click_random_duration('SYNC_SWAP_GETTING_STARTED_2')
        self.move_to_click_random_duration('SYNC_SWAP_GETTING_STARTED_3')
        self.move_to_click_random_duration('SYNC_SWAP_GETTING_STARTED_4')
        # Authorize wallet
        self.move_to_click_random_duration('SYNC_SWAP_WALLET_1')
        self.move_to_click_random_duration('SYNC_SWAP_WALLET_2')
        time.sleep(2)
        self.gradual_scroll(-40)
        time.sleep(2)
        self.move_to_click_random_duration('SYNC_SWAP_WALLET_3')
        self.move_to_click_random_duration('SYNC_SWAP_WALLET_4')
        time.sleep(2)
        print("SyncSwap connected")

    def random_sleep(self, duration):
        upper_bound = 1.25 * duration
        lower_bound = 0.8 * duration
        random_duration = random.uniform(lower_bound, upper_bound)
        time.sleep(random_duration)

    def mute_trade(self):
        # MUTE Dex coordinates
        # 'MUTE_1': (1620, 143, 0.5), # initial connect
        # 'MUTE_2': (795, 489, 0.5), # select metamask
        # 'MUTE_BUTTON_SELL_TOKEN': (990, 516, 0.5), # Sell token button
        # 'MUTE_BUTTON_SEARCH_ASSET': (808, 349, 0.5), # Search token bar
        # 'MUTE_BUTTON_BUY_TOKEN': (1006, 621, 0.5), # Sell token button
        # 'MUTE_BUTTON_SEARCH_RESULT': (856, 542, 0.5), # Select searched token result
        self.move_to_click_random_duration('MUTE_1')
        self.move_to_click_random_duration('MUTE_2')
        self.random_sleep(3)
        self.gradual_scroll(-40)
        self.random_sleep(1)
        self.move_to_click_random_duration('SYNC_SWAP_WALLET_3')
        self.move_to_click_random_duration('SYNC_SWAP_WALLET_4')
        self.random_sleep(2)
        print("Mute connected")
        

    def sync_swap_trade(self):
        # 'SYNC_SWAP_SELL_TOKEN': (1017, 339, 0.5), # sell token
        # 'SYNC_SWAP_BUY_TOKEN': (1020, 490, 0.5), # buy token
        # 'SYNC_SWAP_VALUE_BAR': (676, 343, 0.5), # value bar
        # 'SYNC_SWAP_SEARCH_TOKEN': (737, 386, 0.5), # Search bar
        # 'SYNC_SWAP_SELECT_TOKEN': (796, 491, 0.5), # Select token from search bar
        # 'SYNC_SWAP_SWAP_BUTTON': (858, 654, 0.5), # Swap for trade

        sync_secondary_tokens = ["MAV", "MUTE", "cbETH", "VC", "VS", "IZI", "SPACE"]
        token_to_buy, token_to_sell, amount_to_sell = self.decide_trade_tokens(sync_secondary_tokens)
        print(f"FINAL: TOP - {token_to_sell} {amount_to_sell} bottom - {token_to_buy}")
    
        # Secondary x Secondary
        # token_to_sell = "ETH" # remove this its here for testing purposes
        time.sleep(2)
        if token_to_sell == "ETH" and token_to_buy == "USDC":
            print("DEFAULT: Sell ETH and buy USDC")
        elif token_to_sell == "USDC" and token_to_buy == "ETH":
            self.move_to_click_random_duration('SYNC_SWAP_SELL_TOKEN')
            self.move_to_click_random_duration('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click_random_duration('SYNC_SWAP_SELECT_TOKEN')
            print("REVERSE DEFAULT: Sell USDC and buy ETH")
        elif token_to_sell != "ETH":
            self.move_to_click_random_duration('SYNC_SWAP_SELL_TOKEN')
            self.move_to_click_random_duration('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click_random_duration('SYNC_SWAP_SELECT_TOKEN')
            # self.move_to_click_random_duration('SYNC_SWAP_SEARCH_TOKEN')

            if token_to_buy != "USDC":
                self.move_to_click_random_duration('SYNC_SWAP_BUY_TOKEN')
                self.move_to_click_random_duration('SYNC_SWAP_SEARCH_TOKEN')
                pyautogui.write(token_to_buy, interval=0.1)
                self.move_to_click_random_duration('SYNC_SWAP_SELECT_TOKEN')
                # uncomment below was commented for testing purposes
        self.move_to_click_random_duration('SYNC_SWAP_VALUE_BAR')
        pyautogui.write(str(amount_to_sell), interval=0.1)
        time.sleep(1)
        unlock_location = pyautogui.locateOnScreen(os.path.join('syncswap', 'unlock.png'), confidence=0.8)
        if unlock_location:
            print("Token Unlock is required")
            # print(f"unlock location: {self.get_center(unlock_location)}")
            self.simple_click(self.get_center(unlock_location))
            time.sleep(3)
            next_location = pyautogui.locateOnScreen(os.path.join('syncswap', 'next.png'), confidence=0.8)
            # print("Next wasn't located" if next_location is None else "Next was located")
            if next_location:
                self.simple_click(self.get_center(next_location))
                time.sleep(2)
                approve_location = pyautogui.locateOnScreen(os.path.join('syncswap', 'approve.png'), confidence=0.8)
                # print(f"Approve location: {self.get_center(approve_location)}")
                if approve_location:
                    # print("Approve not located" if approve_location is None else "Approve located")
                    self.simple_click(self.get_center(approve_location))
                    print("Token Unlocked")
        # else:
        #     self.move_to_click_random_duration('SYNC_SWAP_SWAP_BUTTON')

    def decide_trade_tokens(self, dapp_secondary_tokens):
        # Mock data below
        # self.asset_and_balance = {'ETH': '0.031547184058244909', 'cbETH': '0.000604536391884623', 'USDC': '2.50', 'eUSDC': '49.73671446', 'MAV': '3.215840476238897837', 'SWORD': '2.044985551206500507', 'USDC/WETH cSLP': '0.000000023589285067', 'VC': '50.565873038613550091', 'VS': '451.337346287287375391'}
        # self.asset_and_balance = {'ETH': '0.023203'}
        TODAY_ETH_USD_PRICE = 1570 # in dollars

        primary_token = [token for token in self.__primary_token if token in self.asset_and_balance] 
        print(primary_token)
        secondary_token = [token for token in dapp_secondary_tokens if token in self.asset_and_balance] 
        print(secondary_token)

        ETH_USD = TODAY_ETH_USD_PRICE * float(self.asset_and_balance['ETH'])
        print(f"Ethereum in USD: {ETH_USD}")
        
        buy_primary = self.select_category()
        print(f"Buy: {'Primary' if buy_primary else 'Secondary'}")

        sell_primary = self.select_category()
        print(f"Sell: {'Primary' if sell_primary else 'Secondary'}")
        # buy_primary = True #Remove this, it's for testing a condition
        # sell_primary = True #Remove this, it's for testing a condition
        token_to_buy = ""
        token_to_sell = ""
        amount_to_sell = ""
        
        if ETH_USD > 10 and float(self.asset_and_balance["USDC"]) > 1.5:
            print("Conditions for ETH & USDC met")
            if buy_primary and sell_primary:
                print("Primary x Primary")
                selected_tokens = random.sample(primary_token, 2)
                token_to_buy = selected_tokens[0]
                token_to_sell = selected_tokens[1]
                print(f"Buy {token_to_buy} and sell {token_to_sell}")
                if token_to_sell == "ETH":
                    amount_to_sell = str(random.uniform(1, 1.3)/TODAY_ETH_USD_PRICE)
                elif token_to_sell == "USDC":
                    amount_to_sell = str(random.uniform(1, 1.5))
            elif not buy_primary and not sell_primary:
                print("Secondary x Secondary")
                selected_tokens = random.sample(secondary_token, 2)
                token_to_buy = selected_tokens[0]
                token_to_sell = selected_tokens[1]
                print(f"Buy {token_to_buy} and sell {token_to_sell}")
                amount_to_sell = float(self.asset_and_balance[token_to_sell])
            elif buy_primary and not sell_primary:
                print("Primary x Secondary")
                token_to_buy = random.choice(primary_token)
                token_to_sell = random.choice(secondary_token)
                print(f"Buy {token_to_buy} and sell {token_to_sell}")
                amount_to_sell = float(self.asset_and_balance[token_to_sell])
            elif not buy_primary and sell_primary:
                print("Secondary x Primary")
                token_to_buy = random.choice(secondary_token)
                token_to_sell = random.choice(primary_token)
                print(f"Buy {token_to_buy} and sell {token_to_sell}")
                if token_to_sell == "ETH":
                    amount_to_sell = str(random.uniform(1, 1.3)/TODAY_ETH_USD_PRICE)
                elif token_to_sell == "USDC":
                    amount_to_sell = str(random.uniform(1, 1.5))

        elif ETH_USD > 10 and ("USDC" not in self.asset_and_balance or float(self.asset_and_balance.get("USDC", "0")) < 1.5):
            print("Previous conditions INVALIDATED")
            print("Mandatory: Primary x Primary")
            token_to_sell = "ETH"
            amount_to_sell = str(random.uniform(1, 1.3)/TODAY_ETH_USD_PRICE)
            token_to_buy = "USDC"
        print(f"{amount_to_sell} {token_to_sell} and buy {token_to_buy}")
        return token_to_buy, token_to_sell, amount_to_sell
    
    def select_category(self):
        selected_category = random.randint(0, 2)
        selected_bool = True if selected_category == 0 or selected_category == 1 else False
        return selected_bool

    def simple_click(self, position, *args):
        x, y = position
        delay = args[0] if args else 0.5  # You can set a default delay value if needed

        # Randomizing the duration by +20% to +100%
        random_duration_multiplier = 1 + random.uniform(0.20, 1.00)
        random_delay = delay * random_duration_multiplier

        pyautogui.moveTo(x, y, duration=random_delay)
        pyautogui.click(clicks=1)

    def get_balance(self):
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
        else:
            print("Couldn't locate copy icon")
        

    def get_center(self,position):
        position = pyautogui.center(position)
        return((position[0]/2, position[1]/2))
# Example usage:
automation = MouseAutomation()
automation.print_screen_resolution()

automation.print_current_position_continuously()

# automation.enable_vpn()

# automation.open_brave()
# time.sleep(2)
# automation.login_metamask()

# time.sleep(2)
# automation.select_account(selected_account="Account 2")

# time.sleep(2)
# automation.account_explorer()

# time.sleep(2)
# automation.get_balance()

# time.sleep(2)  
# automation.sync_swap_start()

# time.sleep(2)
# automation.sync_swap_trade()

# time.sleep(2)
# automation.mute_trade()

# automation.disconnect_vpn()

# automation.decide_trade_tokens(["MAV", "MUTE", "cbETH", "VC", "VS", "IZI"])