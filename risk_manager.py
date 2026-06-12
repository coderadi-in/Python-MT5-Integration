# RISK MANAGER CLASS
class RiskManager:

    MAX_OPEN_TRADES = 3

    @staticmethod
    def evaluate(signal, open_positions):

        if (signal == 'NO_SIGNAL'):
            return {
                "allowed": False,
                "reason": "NO_SIGNAL"
            }
        
        if (open_positions > RiskManager.MAX_OPEN_TRADES):
            return {
                "allowed": False,
                "reason": "MAX_OPEN_TRADES_LIMIT_REACHED"
            }
        
        return {
            "allowed": True,
            "reason": None
        }