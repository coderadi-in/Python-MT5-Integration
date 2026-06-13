# RISK MANAGER CLASS
class RiskManager:

    MAX_OPEN_TRADES = 3

    @staticmethod
    def evaluate(signal, total_positions, symbol_positions, account_info):

        if (signal == 'NO_SIGNAL'):
            return {
                "allowed": False,
                "reason": "NO_SIGNAL"
            }
        
        if (len(total_positions) > RiskManager.MAX_OPEN_TRADES):
            return {
                "allowed": False,
                "reason": "MAX_OPEN_TRADES_LIMIT_REACHED"
            }
        
        if len(symbol_positions) > 0:
            return {
                "allowed": False,
                "reason": "POSITION_ALREADY_OPEN"
            }
        
        if (account_info['equity'] < 100):
            return {
                "allowed": False,
                "reason": "EQUITY_TOO_LOW"
            }
        
        return {
            "allowed": True,
            "reason": None
        }