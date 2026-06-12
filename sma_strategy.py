# IMPORTS
from data_management import get_data, pd

# STRATEGY CLASS
class SMA3Strategy:
    @staticmethod
    def analyze(df: pd.DataFrame) -> dict:
        previous = df.iloc[-2]
        current = df.iloc[-1]

        buy_signal = (
            previous['close'] < previous['sma3']
            and
            current['close'] > current['sma3']
        )

        sell_signal = (
            previous['close'] > previous['sma3']
            and 
            current['close'] < current['sma3']
        )

        output_dict = {
            "signal": None,
            "price": current["close"],
            "timestamp": current["time"]
        }

        if (buy_signal): output_dict['signal'] = 'BUY'
        elif (sell_signal): output_dict['signal'] = 'SELL'
        else: output_dict['signal'] = 'NO SIGNAL'

        return output_dict

    @staticmethod
    def analyze_with_threshold(df: pd.DataFrame, threshold: float = 0.00005) -> dict:
        previous = df.iloc[-2]
        current = df.iloc[-1]

        previous_distance = previous['close'] - previous['sma3']
        current_distance = current['close'] - current['sma3']

        buy_signal = (
            previous_distance > -threshold
            and
            current_distance > threshold
        )

        sell_signal = (
            previous_distance > threshold
            and 
            current_distance > -threshold
        )

        output_dict = {
            "signal": None,
            "price": current["close"],
            "timestamp": current["time"]
        }

        if (buy_signal): output_dict['signal'] = 'BUY'
        elif (sell_signal): output_dict['signal'] = 'SELL'
        else: output_dict['signal'] = 'NO SIGNAL'

        return output_dict