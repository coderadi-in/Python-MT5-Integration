# IMPORTS
from mt5_service import init, PositionManager, AccountService
from data_management import get_data

from strategy_manager import StrategyManager
from consensus_engine import ConsensusEngine
from risk_manager import RiskManager

# TRADING ENGINE CLASS
class TradingEngine:
    def __init__(
            self, 
            strategy_manager: StrategyManager,
            consensus_engine: ConsensusEngine,
            position_service: PositionManager,
            risk_manager: RiskManager,
    ):
        init()
        self.strategy_manager = strategy_manager
        self.consensus_engine = consensus_engine
        self.position_service = position_service
        self.risk_manager = risk_manager

    def run(self, symbol: str = "EURUSD"):
        
        df, symbol = get_data(symbol)
        signals = self.strategy_manager.analyze_all(df, symbol)
        final_signal = self.consensus_engine.analyze(signals)

        positions = self.position_service.get_open_positions()
        open_positions = len(positions)

        symbol_positions = PositionManager.get_open_positions_by_symbol(symbol)
        account_info = AccountService.get_acc_info()

        risk_result = self.risk_manager.evaluate(final_signal, open_positions, symbol_positions, account_info)
        
        if (risk_result['allowed']):
            print("Trade approved!")

        else:
            print("Trade rejected!")
            print("Reason:", risk_result['reason'])