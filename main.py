# IMPORTS
from data_management import get_data
from ema_strategy import EMACrossStrategy
from sma_strategy import SMA3Strategy
from strategy_manager import StrategyManager
from consensus_engine import ConsensusEngine

df = get_data()
manager = StrategyManager()

manager.add_strategy(EMACrossStrategy)
manager.add_strategy(SMA3Strategy)

signals = manager.analyze_all(df)
consensus = ConsensusEngine.analyze(signals)

print(consensus)