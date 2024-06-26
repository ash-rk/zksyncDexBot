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

class DefiDex:
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

            # SyncSwap connect to wallet & Trade
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
            'SYNC_SWAP_100_BUTTON': (1025, 407, 0.5), # 100% button

            # Metamask connect started
            'MM_NEXT': (1276, 1026, 0.5), # next
            'MM_CONNECT': (1283, 1075, 0.5), # connect
        
            # Velocore getting started
            'VELOCORE_CONNECT_1': (1637, 193, 0.5), # initial connect
            'VELOCORE_CONNECT_2': (627, 474, 0.5), # ethereum wallet
            'VELOCORE_WALLET_NEXT': (1276, 1026, 0.5), # next
            'VELOCORE_WALLET_CONNECT': (1283, 1075, 0.5), # connect

            # Velocore trade
            'VELOCORE_VALUE_BAR': (1037, 541, 0.5), # sell value bar
            'VELCORE_FLIP': (860, 662, 0.5), # flip button
            'VELCORE_SELL_TOKEN': (708, 535, 0.5), # sell token
            'VELCORE_BUY_TOKEN': (709, 750, 0.5), # buy token
            'VELCORE_SEARCH_TOKEN': (775, 497, 0.5), # search bar
            'VELCORE_SELECT_TOKEN': (833, 675, 0.5), # select token
            'VELCORE_100_BUTTON': (1019, 607, 0.5), # 100% button

            # OnchainTrade getting started
            'OT_SWAP': (1319, 238, 0.5), # Click on swap
            'OT_CONNECT_1': (1545, 137, 0.5), # initial connect
            'OT_CONNECT_2': (803, 444, 0.5), # ethereum wallet

            # OnchainTrade - trade 
            'OT_VALUE_BAR': (1290, 318, 0.5), # sell value bar
            'OT_SELL_TOKEN': (1647, 319, 0.5), # sell token
            'OT_SEARCH_SELL_TOKEN': (1665, 375, 0.15), # search sell token
            'OT_SELECT_SELL_TOKEN': (1503, 474, 0.5), # select sell token
            'OT_BUY_TOKEN': (1637, 389, 0.5), # buy token
            'OT_SEARCH_BUY_TOKEN': (1463, 456, 0.5), # search buy token
            'OT_SELECT_BUY_TOKEN': (1519, 546, 0.5), # select buy token
            'OT_TRADE_SWAP': (1465, 473, 0.5), # swap button
            'OT_100_BUTTON': (1683, 287, 0.5), # 100% button

            # Pancakeswap connect to wallet & Trade
            'PANCAKESWAP_WALLET_1': (1622, 204, 0.5), # initial connect
            'PANCAKESWAP_WALLET_2': (564, 561, 0.5), # ethereum wallet
            'PANCAKESWAP_SELL_TOKEN': (757, 495, 0.5), # sell token
            'PANCAKESWAP_BUY_TOKEN': (763, 694, 0.5), # buy token
            'PANCAKESWAP_VALUE_BAR': (956, 540, 0.5), # value bar
            'PANCAKESWAP_SEARCH_TOKEN': (749, 367, 0.5), # Search bar
            'PANCAKESWAP_SELECT_TOKEN': (827, 531, 0.5), # Select token from search bar
            'PANCAKESWAP_SWAP_BUTTON': (865, 897, 0.5), # Swap for trade
            'PANCAKESWAP_100_BUTTON': (976, 589, 0.5), # 100% button
        }
    # ot_loaded = pyautogui.locateOnScreen(os.path.join('images', 'onchaintrade', 'ot_expected2.png'), confidence=0.8)

    def pancakeswap_start(self):
        # SyncSwap getting started clicks
        self.goto("https://pancakeswap.finance/swap?chain=zkSync")
        time.sleep(2)
        pancake_loaded = pyautogui.locateOnScreen(os.path.join('images', 'pancakeswap', 'expected1.png'), confidence=0.8)
        while pancake_loaded is None and index < 4:
            print("Waiting for Pancakeswap to load")
            pancake_loaded = pyautogui.locateOnScreen(os.path.join('images', 'pancakeswap', 'expected1.png'), confidence=0.8)
            time.sleep(5)
            index = index + 1
        print("Pancakeswap loaded" if pancake_loaded is not None else "Failed to load Pancakeswap :(")
        # Authorize wallet
        self.move_to_click('PANCAKESWAP_WALLET_1')
        self.move_to_click('PANCAKESWAP_WALLET_2')
        self.metamask_connect()
        time.sleep(2)
        print("Pancakeswap connected successfully :)")
        secondary_tokens = ["CAKE", "TES", "WBTC"]
        return secondary_tokens

    def pancakeswap_trade(self, token_to_buy, token_to_sell, amount_to_sell):
        print(f"FINAL: TOP - {token_to_sell} {amount_to_sell} bottom - {token_to_buy}")
        # Secondary x Secondary
        # token_to_sell = "ETH" # remove this its here for testing purposes
        time.sleep(2)
        # setting it match ETH buy USDC for Syncswap algorithm to be reused alternatively can use the below link in goto
        # https://pancakeswap.finance/swap?chain=zkSync&outputCurrency=0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4
        self.move_to_click('PANCAKESWAP_BUY_TOKEN')
        self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
        pyautogui.write("USDC", interval=0.1)
        self.move_to_click('PANCAKESWAP_SELECT_TOKEN')

        if token_to_sell == "ETH" and token_to_buy == "USDC":
            print("DEFAULT: Sell ETH and buy USDC")
            self.move_to_click('PANCAKESWAP_VALUE_BAR')
            pyautogui.write(str(amount_to_sell), interval=0.1)

        # sell USDC buy ETH
        elif token_to_sell == "USDC" and token_to_buy == "ETH":
            self.move_to_click('PANCAKESWAP_SELL_TOKEN')
            self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('PANCAKESWAP_SELECT_TOKEN')
            print("REVERSE DEFAULT: Sell USDC and buy ETH")
            self.move_to_click('PANCAKESWAP_VALUE_BAR')
            pyautogui.write(str(amount_to_sell), interval=0.1)

        # sell ETH and buy Secondary
        elif token_to_sell == "ETH" and token_to_buy != "USDC":
            self.move_to_click('PANCAKESWAP_BUY_TOKEN')
            self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('PANCAKESWAP_SELECT_TOKEN')
            self.move_to_click('PANCAKESWAP_VALUE_BAR')
            pyautogui.write(str(amount_to_sell), interval=0.1)
        
        # sell Secondary and buy ETH
        elif token_to_sell not in {"ETH", "USDC"} and token_to_buy == "ETH":
            print("sell Secondary and buy ETH")
            self.move_to_click('PANCAKESWAP_SELL_TOKEN')
            self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('PANCAKESWAP_SELECT_TOKEN')
            # Selecting Secondary token name
            self.move_to_click('PANCAKESWAP_BUY_TOKEN')
            self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('PANCAKESWAP_SELECT_TOKEN')
            # Direct 100% button to be clicked for amount to sell for SECONDARY
            self.move_to_click('PANCAKESWAP_100_BUTTON')
        
        # sell USDC and buy Secondary
        elif token_to_sell == "USDC" and token_to_buy != "ETH":
            print("sell USDC and buy Secondary")
            self.move_to_click('PANCAKESWAP_SELL_TOKEN')
            self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('PANCAKESWAP_SELECT_TOKEN')
            # Selecting Secondary token name
            self.move_to_click('PANCAKESWAP_BUY_TOKEN')
            self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('PANCAKESWAP_SELECT_TOKEN')
            self.move_to_click('PANCAKESWAP_VALUE_BAR')
            pyautogui.write(str(amount_to_sell), interval=0.1)
        
        # sell Secondary and buy USDC
        elif token_to_sell not in {"ETH", "USDC"} and token_to_buy == "USDC":
            print("sell Secondary and buy USDC")
            self.move_to_click('PANCAKESWAP_SELL_TOKEN')
            self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('PANCAKESWAP_SELECT_TOKEN')
            # Direct 100% button to be clicked for amount to sell for SECONDARY
            self.move_to_click('PANCAKESWAP_100_BUTTON')

        # V2 sell Secondary buy Secondary
        elif token_to_sell not in {"ETH", "USDC"} and token_to_buy not in {"ETH", "USDC"}:
            print("V2 sell Secondary and buy Secondary")
            self.move_to_click('PANCAKESWAP_SELL_TOKEN')
            self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('PANCAKESWAP_SELECT_TOKEN')
            # self.move_to_click_random_duration('SYNC_SWAP_SEARCH_TOKEN')
            self.move_to_click('PANCAKESWAP_BUY_TOKEN')
            self.move_to_click('PANCAKESWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('PANCAKESWAP_SELECT_TOKEN')
            # Direct 100% button to be clicked for amount to sell for SECONDARY
            self.move_to_click('PANCAKESWAP_100_BUTTON')
        
        # self.move_to_click('SYNC_SWAP_VALUE_BAR')
        # pyautogui.write(str(amount_to_sell), interval=0.1)
        time.sleep(2)
        swap_button_loaded = pyautogui.locateOnScreen(os.path.join('images', 'pancakeswap', 'swap_button.png'), confidence=0.8)
        while swap_button_loaded is None and index < 4:
            print("Waiting for Swap button to load")
            swap_button_loaded = pyautogui.locateOnScreen(os.path.join('images', 'pancakeswap', 'swap_button.png'), confidence=0.8)
            time.sleep(5)
            index = index + 1
        print("Swap button loaded!" if swap_button_loaded is not None else "Failed to load Swap button :(")
        if swap_button_loaded:
            self.simple_click(self.get_center(swap_button_loaded))

    def onchaintrade_start(self):
        self.goto("https://onchain.trade/#/trade") 
        index = 0
        time.sleep(2)
        ot_loaded = pyautogui.locateOnScreen(os.path.join('images', 'onchaintrade', 'ot_expected2.png'), confidence=0.8)
        while ot_loaded is None and index < 4:
            print("Waiting for OT website to load")
            ot_loaded = pyautogui.locateOnScreen(os.path.join('images', 'onchaintrade', 'ot_expected2.png'), confidence=0.8)
            time.sleep(5)
            index = index + 1
        print("OT Swap loaded" if ot_loaded is not None else "Failed to load OT Swap :(")

        index = 0
        time.sleep(2)
        ot_loaded_USDC = pyautogui.locateOnScreen(os.path.join('images', 'onchaintrade', 'ot_expected3.png'), confidence=0.8)
        while ot_loaded_USDC is None and index < 4:
            print("Waiting for OT USDC to load")
            ot_loaded_USDC = pyautogui.locateOnScreen(os.path.join('images', 'onchaintrade', 'ot_expected3.png'), confidence=0.8)
            time.sleep(5)
            index = index + 1
        print("OT Swap loaded successfully :)" if ot_loaded_USDC is not None else "Failed to load OT Swap :(")

        # move to swap and then authorize
        self.move_to_click('OT_SWAP')
        time.sleep(1)
        self.move_to_click('OT_CONNECT_1')
        self.move_to_click('OT_CONNECT_2')
        self.metamask_connect()
        print("OT connected successfully :)")
        secondary_tokens = ["OT", "Cheems", "OSD"]
        return secondary_tokens
    
    def onchaintrade_trade(self, token_to_buy, token_to_sell, amount_to_sell):
        print(f"FINAL: TOP - {token_to_sell} {amount_to_sell} bottom - {token_to_buy}")
        time.sleep(2)
        # Select buy token
        self.hover_to('OT_BUY_TOKEN')
        time.sleep(1)
        self.move_to_click('OT_SEARCH_BUY_TOKEN')
        pyautogui.write(token_to_buy, interval=0.1)
        self.move_to_click('OT_SELECT_BUY_TOKEN')
        # Select sell token
        self.hover_to('OT_SELL_TOKEN')
        time.sleep(1)
        self.move_to_click('OT_SEARCH_SELL_TOKEN')
        pyautogui.write(token_to_sell, interval=0.1)
        self.move_to_click('OT_SELECT_SELL_TOKEN')

        if token_to_sell not in {"ETH", "USDC"}:
            self.move_to_click('OT_100_BUTTON')
        else:
            self.move_to_click('OT_VALUE_BAR')
            pyautogui.write(str(amount_to_sell), interval=0.1)
        
    def velocore_start(self):
        self.goto("https://app.velocore.xyz/swap")
        index = 0
        pyautogui.move(0, 200, 0.5)
        time.sleep(5)
        self.gradual_scroll(-10)
        time.sleep(2)
        vc_loaded = pyautogui.locateOnScreen(os.path.join('images', 'velocore', 'vc_expected1.png'), confidence=0.8)
        while vc_loaded is None and index < 4:
            print("Waiting for Velocore website to load")
            vc_loaded = pyautogui.locateOnScreen(os.path.join('images', 'velocore', 'vc_expected1.png'), confidence=0.8)
            time.sleep(5)
            index = index + 1
        print("Velocore loaded successfully :)" if vc_loaded is not None else "Failed to load Velocore :(")
        # Authorize wallet
        self.move_to_click('VELOCORE_CONNECT_1')
        time.sleep(1)
        self.move_to_click('VELOCORE_CONNECT_2')
        time.sleep(2)
        self.gradual_scroll(-40)
        time.sleep(2)
        self.move_to_click('VELOCORE_WALLET_NEXT')
        self.move_to_click('VELOCORE_WALLET_CONNECT')
        time.sleep(2)
        print("Velocore authorized & connected")
        secondary_tokens = ["VC", "WAIFU", "SIS", "ONEZ", "RF"]
        return secondary_tokens

    def velocore_trade(self, token_to_buy, token_to_sell, amount_to_sell):
        print(f"FINAL: TOP - {token_to_sell} {amount_to_sell} bottom - {token_to_buy}")
        time.sleep(2)

        # sell ETH and buy USDC
        if token_to_sell == "ETH" and token_to_buy == "USDC":
            print("DEFAULT: Sell ETH and buy USDC")
            self.move_to_click('VELOCORE_VALUE_BAR')
            pyautogui.hotkey('command', 'a', interval=0)
            pyautogui.press('backspace', presses=1)
            pyautogui.write(str(amount_to_sell), interval=0.1)
        
        # sell USDC buy ETH
        elif token_to_sell == "USDC" and token_to_buy == "ETH":
            self.move_to_click('VELCORE_FLIP')
            self.move_to_click('VELOCORE_VALUE_BAR')
            pyautogui.hotkey('command', 'a', interval=0)
            pyautogui.press('backspace', presses=1)
            pyautogui.write(str(amount_to_sell), interval=0.1)

        # sell ETH and buy Secondary
        elif token_to_sell == "ETH" and token_to_buy != "USDC":
            self.move_to_click('VELOCORE_BUY_TOKEN')
            self.move_to_click('VELOCORE_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('VELOCORE_SELECT_TOKEN')
            self.move_to_click('VELOCORE_VALUE_BAR')
            pyautogui.hotkey('command', 'a', interval=0)
            pyautogui.press('backspace', presses=1)
            pyautogui.write(str(amount_to_sell), interval=0.1)

        # sell Secondary and buy ETH
        elif token_to_sell not in {"ETH", "USDC"} and token_to_buy == "ETH":
            print("sell Secondary and buy ETH")
            self.move_to_click('VELOCORE_SELL_TOKEN')
            self.move_to_click('VELOCORE_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('VELOCORE_SELECT_TOKEN')
            # Selecting Secondary token name
            self.move_to_click('VELOCORE_BUY_TOKEN')
            self.move_to_click('VELOCORE_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('VELOCORE_SELECT_TOKEN')
            # Direct 100% button to be clicked for amount to sell for SECONDARY
            self.move_to_click('VELOCORE_100_BUTTON')

        # sell USDC and buy Secondary
        elif token_to_sell == "USDC" and token_to_buy != "ETH":
            print("sell USDC and buy Secondary")
            self.move_to_click('VELCORE_FLIP')
            self.move_to_click('VELOCORE_BUY_TOKEN')
            self.move_to_click('VELOCORE_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('VELOCORE_SELECT_TOKEN')
            self.move_to_click('VELOCORE_VALUE_BAR')
            pyautogui.hotkey('command', 'a', interval=0)
            pyautogui.press('backspace', presses=1)
            pyautogui.write(str(amount_to_sell), interval=0.1)

        # sell Secondary and buy USDC
        elif token_to_sell not in {"ETH", "USDC"} and token_to_buy == "USDC":
            print("sell Secondary and buy USDC")
            self.move_to_click('VELOCORE_SELL_TOKEN')
            self.move_to_click('VELOCORE_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('VELOCORE_SELECT_TOKEN')
            # Selecting Secondary token name
            self.move_to_click('VELOCORE_BUY_TOKEN')
            self.move_to_click('VELOCORE_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('VELOCORE_SELECT_TOKEN')
            # Direct 100% button to be clicked for amount to sell for SECONDARY
            self.move_to_click('VELOCORE_100_BUTTON')

        # V2 sell Secondary buy Secondary
        elif token_to_sell not in {"ETH", "USDC"} and token_to_buy not in {"ETH", "USDC"}:
            print("sell Secondary and buy Secondary")
            self.move_to_click('VELOCORE_SELL_TOKEN')
            self.move_to_click('VELOCORE_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('VELOCORE_SELECT_TOKEN')
            # Selecting Secondary token name
            self.move_to_click('VELOCORE_BUY_TOKEN')
            self.move_to_click('VELOCORE_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('VELOCORE_SELECT_TOKEN')
            # Direct 100% button to be clicked for amount to sell for SECONDARY
            self.move_to_click('VELOCORE_100_BUTTON')
        self.gradual_scroll(-10)
        
    def get_tokens_by_method_name(self, method_name):
        # print(dir(self))
        try:
            # Get the method by name and call it
            method = getattr(self, method_name)
            return method()
        except AttributeError:
            print(f"Method {method_name} not found in DefiDex class")
            return []

    def syncswap_start(self):
        # SyncSwap getting started clicks
        self.goto("https://syncswap.xyz/")
        time.sleep(2)
        loaded = self.locate_with_retries(os.path.join('images', 'syncswap', 'welcome.png'))
        if not loaded:
            return
        self.move_to_click('SYNC_SWAP_GETTING_STARTED_1')
        self.move_to_click('SYNC_SWAP_GETTING_STARTED_2')
        self.move_to_click('SYNC_SWAP_GETTING_STARTED_3')
        self.move_to_click('SYNC_SWAP_GETTING_STARTED_4')
        # Authorize wallet
        self.move_to_click('SYNC_SWAP_WALLET_1')
        self.move_to_click('SYNC_SWAP_WALLET_2')
        time.sleep(2)
        self.gradual_scroll(-40)
        time.sleep(2)
        self.move_to_click('SYNC_SWAP_WALLET_3')
        self.move_to_click('SYNC_SWAP_WALLET_4')
        time.sleep(2)
        print("SyncSwap connected")
        secondary_tokens = ["MAV", "MUTE", "cbETH", "VC", "VS", "IZI", "SPACE"]
        return secondary_tokens

    def syncswap_trade(self, token_to_buy, token_to_sell, amount_to_sell):
        print(f"FINAL: TOP - {token_to_sell} {amount_to_sell} bottom - {token_to_buy}")
        # Secondary x Secondary
        # token_to_sell = "ETH" # remove this its here for testing purposes
        time.sleep(2)
        # sell ETH buy USDC
        if token_to_sell == "ETH" and token_to_buy == "USDC":
            print("DEFAULT: Sell ETH and buy USDC")
            self.move_to_click('SYNC_SWAP_VALUE_BAR')
            pyautogui.write(str(amount_to_sell), interval=0.1)

        # sell USDC buy ETH
        elif token_to_sell == "USDC" and token_to_buy == "ETH":
            self.move_to_click('SYNC_SWAP_SELL_TOKEN')
            self.move_to_click('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('SYNC_SWAP_SELECT_TOKEN')
            print("REVERSE DEFAULT: Sell USDC and buy ETH")
            self.move_to_click('SYNC_SWAP_VALUE_BAR')
            pyautogui.write(str(amount_to_sell), interval=0.1)

        # sell ETH and buy Secondary
        elif token_to_sell == "ETH" and token_to_buy != "USDC":
            self.move_to_click('SYNC_SWAP_BUY_TOKEN')
            self.move_to_click('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('SYNC_SWAP_SELECT_TOKEN')
            self.move_to_click('SYNC_SWAP_VALUE_BAR')
            pyautogui.write(str(amount_to_sell), interval=0.1)
        
        # sell Secondary and buy ETH
        elif token_to_sell not in {"ETH", "USDC"} and token_to_buy == "ETH":
            print("sell Secondary and buy ETH")
            self.move_to_click('SYNC_SWAP_SELL_TOKEN')
            self.move_to_click('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('SYNC_SWAP_SELECT_TOKEN')
            # Selecting Secondary token name
            self.move_to_click('SYNC_SWAP_BUY_TOKEN')
            self.move_to_click('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('SYNC_SWAP_SELECT_TOKEN')
            # Direct 100% button to be clicked for amount to sell for SECONDARY
            self.move_to_click('SYNC_SWAP_100_BUTTON')
        
        # sell USDC and buy Secondary
        elif token_to_sell == "USDC" and token_to_buy != "ETH":
            print("sell USDC and buy Secondary")
            self.move_to_click('SYNC_SWAP_SELL_TOKEN')
            self.move_to_click('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('SYNC_SWAP_SELECT_TOKEN')
            # Selecting Secondary token name
            self.move_to_click('SYNC_SWAP_BUY_TOKEN')
            self.move_to_click('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('SYNC_SWAP_SELECT_TOKEN')
            self.move_to_click('SYNC_SWAP_VALUE_BAR')
            pyautogui.write(str(amount_to_sell), interval=0.1)
        
        # sell Secondary and buy USDC
        elif token_to_sell not in {"ETH", "USDC"} and token_to_buy == "USDC":
            print("sell Secondary and buy USDC")
            self.move_to_click('SYNC_SWAP_SELL_TOKEN')
            self.move_to_click('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('SYNC_SWAP_SELECT_TOKEN')
            # Direct 100% button to be clicked for amount to sell for SECONDARY
            self.move_to_click('SYNC_SWAP_100_BUTTON')

        # V2 sell Secondary buy Secondary
        elif token_to_sell not in {"ETH", "USDC"} and token_to_buy not in {"ETH", "USDC"}:
            print("V2 sell Secondary and buy Secondary")
            self.move_to_click('SYNC_SWAP_SELL_TOKEN')
            self.move_to_click('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_sell, interval=0.1)
            self.move_to_click('SYNC_SWAP_SELECT_TOKEN')
            # self.move_to_click_random_duration('SYNC_SWAP_SEARCH_TOKEN')
            self.move_to_click('SYNC_SWAP_BUY_TOKEN')
            self.move_to_click('SYNC_SWAP_SEARCH_TOKEN')
            pyautogui.write(token_to_buy, interval=0.1)
            self.move_to_click('SYNC_SWAP_SELECT_TOKEN')
            # Direct 100% button to be clicked for amount to sell for SECONDARY
            self.move_to_click('SYNC_SWAP_100_BUTTON')
        
        # self.move_to_click('SYNC_SWAP_VALUE_BAR')
        # pyautogui.write(str(amount_to_sell), interval=0.1)
        time.sleep(1)
        print("looking for unlock")
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
        #     self.move_to_click('SYNC_SWAP_SWAP_BUTTON')

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
        secondary_tokens = ["PEP", "cbETH", "Izumi", "Blade"]
        return secondary_tokens
    
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

        # Check if address contains the '#' character and handle it
        if '#' in address:
            # Split the address into parts around the '#' character
            parts = address.split('#')
            # Type the first part of the address
            pyautogui.write(parts[0], interval=0.1)
            # Handle the '#' character
            self.type_hash()
            # Type the rest of the address
            if len(parts) > 1:
                pyautogui.write(parts[1], interval=0.1)
        else:
            # If there's no '#' character, just type the address as usual
            pyautogui.write(address, interval=0.1)

        pyautogui.press('enter', presses=1)

    def type_hash(self):
        # Here, use the specific keystrokes that are required to type the '#' character on your keyboard
        pyautogui.hotkey('option', '3')  # Adjust this to your keyboard

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
    
    def hover_to(self, position):
        if position not in self.coordinates:
            print(f"Unknown symbol: {position}")
            return

        x, y, delay = self.coordinates[position]

        # Randomizing the duration by +20% to +100%
        random_duration_multiplier = 1 + random.uniform(0.20, 1.00)
        random_delay = delay * random_duration_multiplier

        pyautogui.moveTo(x, y, duration=random_delay)

    def gradual_scroll(self, amount, clicks=2, interval=0.0001):
        # Determine the direction of the scroll
        direction = 1 if amount > 0 else -1
        for _ in range(abs(amount)):
            pyautogui.scroll(direction * clicks)
            time.sleep(interval)

    def get_center(self,position):
        position = pyautogui.center(position)
        return((position[0]/2, position[1]/2))
    
    def metamask_connect(self):
        time.sleep(2)
        self.gradual_scroll(-40)
        time.sleep(2)
        self.move_to_click('MM_NEXT')
        self.move_to_click('MM_CONNECT')

    # Locate with retries
    def locate_with_retries(self, image_path, retries=3, delay=2):
        attempt = 0
        while attempt < retries:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                return location
            time.sleep(delay)
            attempt += 1
        return None