# IMPORTS
import MetaTrader5 as mt5

def init():
    if (not mt5.initialize()):
        print("Failed to connect with MT-5 because; ", mt5.last_error())
        quit()

# POSITION SERVICE CLASS
class PositionService:
    
    @staticmethod
    def get_open_positions():

        positions = mt5.positions_get()

        if (positions is None):
            return []
        
        return positions
    
# ACCOUNT SERVICE CLASS
class AccountService:

    @staticmethod
    def get_acc_info():

        acc_info = mt5.account_info()

        if (not acc_info): return None

        return {
            "login": acc_info.login,
            "balance": acc_info.balance,
            "equity": acc_info.equity,
            "profit": acc_info.profit,
            "margin": acc_info.margin,
            "free_margin": acc_info.margin_free
        }