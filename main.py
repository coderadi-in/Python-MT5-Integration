# # IMPORTS
# from data_management import get_data
# from ema_strategy import EMACrossStrategy
# from sma_strategy import SMA3Strategy
# from strategy_manager import StrategyManager
# from consensus_engine import ConsensusEngine
# from risk_manager import RiskManager
# from mt5_service import PositionService, AccountService, init, mt5
# from trade_executor import TradeExecutor

# init()
# # df = get_data()
# # manager = StrategyManager()

# # manager.add_strategy(EMACrossStrategy)
# # manager.add_strategy(SMA3Strategy)

# # signals = manager.analyze_all(df)
# # consensus = ConsensusEngine.analyze(signals)

# # open_positions = PositionService.get_open_positions()
# # permission = RiskManager.evaluate(consensus, len(open_positions))

# # if (permission['allowed']):
# #     TradeExecutor.execute('SELL EURUSD')
# # else:
# #     print("Can't execute trade")
# #     print(f"Reason: {permission['reason']}")

# acc_info = AccountService.get_acc_info()
# print(acc_info)

# IMPORTS
from trading_engine import *

from sma_strategy import SMA3Strategy
from ema_strategy import EMACrossStrategy

strategy_manager = StrategyManager()
strategy_manager.add_strategy(SMA3Strategy)
strategy_manager.add_strategy(EMACrossStrategy)

consensus_engine = ConsensusEngine()
position_service = PositionManager()
risk_manager = RiskManager()

engine = TradingEngine(strategy_manager, consensus_engine, position_service, risk_manager)
engine.run()