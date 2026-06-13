# IMPORTS
from pandas import DataFrame

# STRATEGY_MANAGER CLASS
class StrategyManager:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def analyze_all(self, df: DataFrame, symbol: str):
        signals = []

        for strategy in self.strategies:
            signal = strategy.analyze(df, symbol)

            signals.append(signal)

        return signals