# IMPORT
import MetaTrader5 as mt5

# CONNECTION
def connect():
    connected = mt5.initialize()

    if (not connected):
        print("Connection failed because ", mt5.last_error())
        quit()

# ACCOUNT INFO
def print_account_bal():
    account = mt5.account_info()
    print(account.balance)

# FETCH MARKET DATA
def fetch_market_data(symbol ="EURUSD", timeframe = mt5.TIMEFRAME_M15, amount = 10):
    rates = mt5.copy_rates_from_pos(
        symbol,
        timeframe,
        0, amount
    )

    return rates


if __name__ == "__main__":
    print(fetch_market_data())


mt5.shutdown()