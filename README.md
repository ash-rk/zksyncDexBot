# SproutStarter

## Overview
SproutStarter is a Python automation script designed to facilitate trading operations. It serves as the orchestrator for various trading-related tasks, including establishing a VPN connection, launching and interacting with a web browser, handling a wallet, retrieving and managing balances, and executing trades using the DefiDex class.

This has been designed to use on a 16-inch Macbook Pro (Uses resolution 1728 x 1117)

The resolution can be customised, I had customised them for use on Mac VM softwares like UTM which have a slightly different resolution due to lack of the notch.

Simple_click.py will be deprecated soon, as it's the file that contained all the functionality. 

The main class is sprout_starter.py

## Structure

### `SproutStarter Class`
**Attributes:**
- `vpn`: An instance of the VPNConnection class.
- `browser`: An instance of the SelectBrowser class.
- `wallet`: An instance of the Wallet class.
- `balances`: A dictionary holding asset balances.
- `dex`: An instance of the DefiDex class.
- `secondary_tokens`: A list of secondary tokens.
- `planner`: To select DEX and potential planning & usage of accounts

**Methods:**
- `fetch_balance()`: Fetches the wallet balance and updates the `balances` attribute.
- `get_secondary_tokens(method_name)`: Retrieves tokens using a specified method from the DefiDex class and extends the `secondary_tokens` list.

### `Orchestrator Class`
**Attributes:**
- `fertilize`: An instance of the SproutStarter class.
- `trade`: Initially set to None, will later hold an instance of the Trade class.

**Methods:**
- `run()`: Orchestrates the various operations including:
  - Wallet login and balance fetching.
  - Secondary token retrieval.
  - Trade decision-making using the Trade class.
  - Trade execution through the DefiDex class.

### Other Classes
The script imports and utilizes other external classes including `Trade`, `VPNConnection`, `SelectBrowser`, `Wallet`, and `DefiDex`. Each of these classes should be defined in their respective modules and should be available in the project directory.

## Usage
Execute the script by running the following command in your terminal:

```shell
python3 -m venv myenv2
python sprout_starter.py
```

Dependencies
- time
- random
- pyscreeze
- PIL
