# IMPORTS
from data_management import pd


# STRATEGY CLASS
class EMACrossStrategy:

    @staticmethod
    def analyze(df: pd.DataFrame, symbol: str) -> dict:

        df["ema5"] = df["close"].ewm(span=5).mean()

        df["ema10"] = df["close"].ewm(span=10).mean()

        previous = df.iloc[-2]
        current = df.iloc[-1]

        buy_signal = (
            previous["ema5"] > previous["ema10"] and current["ema5"] < current["ema10"]
        )

        sell_signal = (
            previous["ema5"] < previous["ema10"] and current["ema5"] > current["ema10"]
        )

        output_dict = {
            "signal": None,
            "symbol": symbol,
            "price": float(current["close"]),
            "timestamp": current["time"],
            "strategy": "EMA_Cross",
        }

        if buy_signal:
            output_dict["signal"] = "BUY"
        elif sell_signal:
            output_dict["signal"] = "SELL"
        else:
            output_dict["signal"] = "NO_SIGNAL"

        return output_dict

    @staticmethod
    def analyze_with_threshold(df: pd.DataFrame, symbol: str, threshold: float = 0.00005) -> dict:

        df["ema5"] = df["close"].ewm(span=5).mean()

        df["ema10"] = df["close"].ewm(span=10).mean()

        previous = df.iloc[-2]
        current = df.iloc[-1]

        current_distance = current["ema5"] - current["ema10"]

        previous_distance = previous["ema5"] - previous["ema10"]

        buy_signal = previous_distance < -threshold and current_distance > threshold

        sell_signal = previous_distance > threshold and current_distance < -threshold

        output_dict = {
            "signal": None,
            "symbol": symbol,
            "price": float(current["close"]),
            "timestamp": current["time"],
            "strategy": "EMA_Cross",
        }

        if buy_signal:
            output_dict["signal"] = "BUY"
        elif sell_signal:
            output_dict["signal"] = "SELL"
        else:
            output_dict["signal"] = "NO_SIGNAL"

        return output_dict
