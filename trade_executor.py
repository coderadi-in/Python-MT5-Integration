import MetaTrader5 as mt5

# TRADE EXECUTOR CLASS
class TradeExecutor:

    @staticmethod
    def execute(signal):

        tick = mt5.symbol_info_tick("EURUSD")

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": "EURUSD",
            "volume": 0.01,
            "type": mt5.ORDER_TYPE_BUY,
            "price": tick.ask,
            "deviation": 20,
            "magic": 1000,
            "comment": "ECHO_TEST"
        }

        result = mt5.order_send(request)

        if (result.retcode == mt5.TRADE_RETCODE_DONE):
            print("Executed successfully.")
            print(result.retcode)
            print(result.comment)
            print(result.order)

        else:
            print("Something went wrong!")
            print(result.retcode)
            print(result.comment)
            print(result.order)