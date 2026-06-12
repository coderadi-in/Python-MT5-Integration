# CONSENSUS ENGINE CLASS
class ConsensusEngine:
    
    @staticmethod
    def analyze(signals: list) -> str:

        buy_count, sell_count = 0, 0

        for signal in signals:
            if (signal['signal'] == 'BUY'): buy_count += 1
            elif (signal['signal'] == 'SELL'): sell_count += 1

        if (buy_count > sell_count): return 'BUY'
        elif (sell_count > buy_count): return 'SELL'
        else: return 'NO_SIGNAL'
