import time
import random
from trade import Trade
from vpn_connection import VPNConnection
from select_browser import SelectBrowser
from wallet import Wallet
from defi_dex import DefiDex
from planner import Planner

# Current Resolution: Size(width=1728, height=1117)

class SproutStarter:
    def __init__(self):
        self.vpn = VPNConnection()
        self.browser = SelectBrowser()
        self.wallet = Wallet()
        self.balances = {}
        self.dex = DefiDex()
        self.secondary_tokens = []
        self.planner = Planner()

    def fetch_balance(self):
        self.balances = self.wallet.get_balance()
    
    def get_secondary_tokens(self, method_name):
        tokens = self.dex.get_tokens_by_method_name(method_name)
        if tokens:
            self.secondary_tokens.extend(tokens)
        else:
            print(f"Failed to get tokens using method: {method_name}")

    def dex_trade(self, method_name, token_to_buy, token_to_sell, amount_to_sell):
        method = getattr(self.dex, method_name, None)
        if method:
            return method(token_to_buy, token_to_sell, amount_to_sell)
        else:
            print(f"Method {method_name} not found in DefiDex class")
            return None

class Orchestrator:
    def __init__(self):
        self.fertilize = SproutStarter()
        self.trade = None

    # The prod function to run with genuine data
    def run(self):
        # Enable VPN
        # self.fertilize.vpn.enable_vpn()
        selected_dex = self.fertilize.planner.select_dex()
        # Open preferred browser
        self.fertilize.browser.open_brave()
        time.sleep(2)

        # Login to wallet and fetch balance
        self.fertilize.wallet.login_metamask()
        time.sleep(2)
        self.fertilize.wallet.select_account("Account 23")
        time.sleep(2)

        # Fetch balance from debank
        self.fertilize.fetch_balance()

        # Get secondary tokens
        self.fertilize.get_secondary_tokens(f"{selected_dex}_start")

        # Decide trade
        self.trade = Trade(self.fertilize.balances)
        token_to_buy, token_to_sell, amount_to_sell = self.trade.select_tokens(self.fertilize.secondary_tokens)
        
        # Execute trade
        self.fertilize.dex_trade(f"{selected_dex}_trade", token_to_buy, token_to_sell, amount_to_sell)

    # The test function to run with mock data
    def test_run(self):
        # self.fertilize.wallet.login_metamask()
        # time.sleep(2)
        # self.fertilize.wallet.select_account("Account 5")
        # time.sleep(2)
        balance = self.fertilize.wallet.get_balance()

        # Mock data & code refinement
        # mock balance below
        # time.sleep(2)
        # mock_balance_pan = {'ETH': '0.031547184058244909', 'CAK': '0.000604536391884623', 'USDC': '2.50', 'TES': '49.73671446', 'OSD': '3.215840476238897837'}
        # self.fertilize.get_secondary_tokens("pancakeswap_start")
        # time.sleep(2)
        # self.trade = Trade(mock_balance_pan)
        # mock_pan_tokens = ["CAK", "TES", "WBTC"]
        # token_to_buy, token_to_sell, amount_to_sell = self.trade.select_tokens(mock_pan_tokens)
        # self.fertilize.dex_trade("pancakeswap_trade", token_to_buy, token_to_sell, amount_to_sell)
        
        # mock_balance_v = {'ETH': '0.031547184058244909', 'WAIFU': '0.000604536391884623', 'USDC': '2.50', 'SIS': '49.73671446', 'ONEZ': '3.215840476238897837', 'SWORD': '2.044985551206500507', 'USDC/WETH cSLP': '0.000000023589285067', 'VC': '50.565873038613550091', 'VS': '451.337346287287375391'}
        # self.fertilize.get_secondary_tokens("velocore_start")

        # self.trade = Trade(mock_balance_v)
        # token_to_buy, token_to_sell, amount_to_sell = self.trade.select_tokens(self.fertilize.secondary_tokens)
        # self.fertilize.dex_trade("velocore_trade", token_to_buy, token_to_sell, amount_to_sell)
        
        # mock_balance = {'ETH': '0.031547184058244909', 'cbETH': '0.000604536391884623', 'USDC': '2.50', 'eUSDC': '49.73671446', 'MAV': '3.215840476238897837', 'SWORD': '2.044985551206500507', 'USDC/WETH cSLP': '0.000000023589285067', 'VC': '50.565873038613550091', 'VS': '451.337346287287375391'}
        # # Below doesn't have USDC
        # mock_balance2 = {'ETH': '0.031547184058244909', 'cbETH': '0.000604536391884623', 'MAV': '3.215840476238897837'}
        # # Below does have USDC, and some secondary
        # mock_balance3 = {'ETH': '0.031547184058244909', 'USDC': '2.50', 'cbETH': '0.000604536391884623', 'MAV': '3.215840476238897837'}
        # # Below doesn't have any secondary
        # mock_balance4 = {'ETH': '0.031547184058244909', 'USDC': '2.50'}
        # self.trade = Trade(mock_balance)
        # mock_secondary_tokens = ["MAV", "MUTE", "cbETH", "VC", "VS", "IZI", "SPACE"]
        # token_to_buy, token_to_sell, amount_to_sell = self.trade.select_tokens(mock_secondary_tokens)
        # print(f"Token to buy: {token_to_buy}, Token to sell: {token_to_sell}, Amount to sell: {amount_to_sell}")

if __name__ == "__main__":
    Orchestrator().run()

# Dexes automated: Syncswap, Velocore, OnchainTrade, PancakeSwap
# sync_swap_start and sync_swap_trade, velocore_start and velocore_trade
# onchaintrade_start and onchaintrade_trade, pancakeswap_start and pancakeswap_trade