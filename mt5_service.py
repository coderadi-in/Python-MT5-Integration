# IMPORTS
import MetaTrader5 as mt5

def init():
    if (not mt5.initialize()):
        print("Failed to connect with MT-5 because; ", mt5.last_error())
        quit()

# POSITION SERVICE CLASS
class PositionManager:
    
    @staticmethod
    def get_open_positions():

        positions = mt5.positions_get()

        if (positions is None):
            return []
        
        return positions
    
    @staticmethod
    def get_open_positions_by_symbol(symbol):

        positions = mt5.positions_get(symbol=symbol)

        return positions or []
    
    @staticmethod
    def get_position_by_ticket(ticket):
        positions = mt5.positions_get()

        if (not positions): return None

        for position in positions:
            if (position.ticket == ticket):
                return position
            
        return None

    @staticmethod
    def close_position(ticket):
        position = PositionManager.get_position_by_ticket(ticket)
        if (not position): return {
            "success": False,
            "error": "NO_OPEN_POSITION_FOUND"
        }

        if (position.type == mt5.POSITION_TYPE_BUY):
            order_type = mt5.POSITION_TYPE_SELL
        else:
            order_type = mt5.POSITION_TYPE_SELL

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": position.symbol,
            "volume": position.volume,
            "type": order_type,
            "position": position.ticket,
            "price": position.price,
            "deviation": 20,
            "magic": 1000,
            "comment": "POSITION_CLOSE"
        }

        result = mt5.order_send(request)
        
        if (result.retcode == mt5.TRADE_RETCODE_DONE):
            return {
                "success": True,
                "ticket": ticket
            }
        
        return {
            "success": False,
            "error": result.comment
        }
    
    @staticmethod
    def has_position(symbol):

        positions = (
            PositionManager
            .get_position_by_symbol(symbol)
        )

        return len(positions) > 0
    
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
    
init()