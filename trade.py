import random

import pyscreeze
import PIL

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

class Trade:
    def __init__(self, balances):
        self.__primary_token = ["ETH", "USDC"]
        self.asset_and_balance = balances

    def select_category(self):
        selected_category = random.randint(0, 2)
        selected_bool = True if selected_category == 0 or selected_category == 1 else False
        return selected_bool

    def select_tokens(self, dapp_secondary_tokens,):
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
        # Fixed issue when new wallets don't have any secondary tokens & anything besides ETH
        if ETH_USD > 10 and ("USDC" in self.asset_and_balance or float(self.asset_and_balance.get("USDC", "0")) > 1.5):
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
                    if float(self.asset_and_balance.get("USDC")) >= 1.5:
                        amount_to_sell = str(random.uniform(1, 1.5))
                    else:
                        USDC_AMOUNT = float(self.asset_and_balance.get("USDC"))
                        MAX_USDC = min(float(self.asset_and_balance.get("USDC")), 1.5)
                        amount_to_sell = str(random.uniform(USDC_AMOUNT*0.2, MAX_USDC))
            # one secondary tokens required to sell
            elif not buy_primary and not sell_primary:
                print("Secondary x Secondary")
                print(f"Secondary tokens: {secondary_token}")
                print("Zero secondary tokens with balance" if secondary_token == [] else "Have some stuff")
                if secondary_token != []:
                    token_to_buy = random.choice(dapp_secondary_tokens)
                    token_to_sell = random.choice(secondary_token)
                    # Ensure selected tokens are different
                    while token_to_buy == token_to_sell:
                        token_to_buy = random.choice(dapp_secondary_tokens)
                        token_to_sell = random.choice(secondary_token)
                    print(f"Buy {token_to_buy} and sell {token_to_sell}")
                    amount_to_sell = float(self.asset_and_balance[token_to_sell])
                else:
                    print("Previous conditions INVALIDATED: lack of Secondary tokens with balance")
                    token_to_buy = random.choice(dapp_secondary_tokens)
                    token_to_sell = random.choice(primary_token)
                    print(f"Buy {token_to_buy} and sell {token_to_sell}")
                    if token_to_sell == "ETH":
                        amount_to_sell = str(random.uniform(1, 1.3)/TODAY_ETH_USD_PRICE)
                    elif token_to_sell == "USDC":
                        if float(self.asset_and_balance.get("USDC")) >= 1.5:
                            amount_to_sell = str(random.uniform(1, 1.5))
                        else:
                            USDC_AMOUNT = float(self.asset_and_balance.get("USDC"))
                            MAX_USDC = min(float(self.asset_and_balance.get("USDC")), 1.5)
                            amount_to_sell = str(random.uniform(USDC_AMOUNT*0.2, MAX_USDC))
                        
            # one secondary token required to sell
            elif buy_primary and not sell_primary:
                print("Primary x Secondary")
                print(f"Secondary tokens: {secondary_token}")
                print("Zero secondary tokens with balance" if secondary_token == [] else "Have some stuff")
                if secondary_token != []:
                    token_to_buy = random.choice(primary_token)
                    token_to_sell = random.choice(secondary_token)
                    print(f"Buy {token_to_buy} and sell {token_to_sell}")
                    amount_to_sell = float(self.asset_and_balance[token_to_sell])
                else:
                    print("Previous conditions INVALIDATED: lack of Secondary tokens with balance")
                    token_to_buy = random.choice(dapp_secondary_tokens)
                    token_to_sell = random.choice(primary_token)
                    print(f"Buy {token_to_buy} and sell {token_to_sell}")
                    if token_to_sell == "ETH":
                        amount_to_sell = str(random.uniform(1, 1.3)/TODAY_ETH_USD_PRICE)
                    elif token_to_sell == "USDC":
                        if float(self.asset_and_balance.get("USDC")) >= 1.5:
                            amount_to_sell = str(random.uniform(1, 1.5))
                        else:
                            USDC_AMOUNT = float(self.asset_and_balance.get("USDC"))
                            MAX_USDC = min(float(self.asset_and_balance.get("USDC")), 1.5)
                            amount_to_sell = str(random.uniform(USDC_AMOUNT*0.2, MAX_USDC))

            elif not buy_primary and sell_primary:
                print("Secondary x Primary")
                # token_to_buy = random.choice(secondary_token)  # This only selects secondary token to buy that has exsting balance
                token_to_buy = random.choice(dapp_secondary_tokens)
                token_to_sell = random.choice(primary_token)
                print(f"Buy {token_to_buy} and sell {token_to_sell}")
                if token_to_sell == "ETH":
                    amount_to_sell = str(random.uniform(1, 1.3)/TODAY_ETH_USD_PRICE)
                elif token_to_sell == "USDC":
                    if float(self.asset_and_balance.get("USDC")) >= 1.5:
                        amount_to_sell = str(random.uniform(1, 1.5))
                    else:
                        USDC_AMOUNT = float(self.asset_and_balance.get("USDC"))
                        MAX_USDC = min(float(self.asset_and_balance.get("USDC")), 1.5)
                        amount_to_sell = str(random.uniform(USDC_AMOUNT*0.2, MAX_USDC))

        elif ETH_USD > 10 and ("USDC" not in self.asset_and_balance or float(self.asset_and_balance.get("USDC", "0")) < 1.5):
            print("Previous conditions INVALIDATED: lack of USDC")
            print("Mandatory: Primary x Primary")
            token_to_sell = "ETH"
            amount_to_sell = str(random.uniform(1, 1.3)/TODAY_ETH_USD_PRICE)
            token_to_buy = "USDC"
            
        print(f"{amount_to_sell} {token_to_sell} and buy {token_to_buy}")
        return token_to_buy, token_to_sell, amount_to_sell