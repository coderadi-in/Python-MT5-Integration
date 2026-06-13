# IMPORT
import pandas as pd
from basic import *

def get_data(symbol: str = "EURUSD"):
    data = fetch_market_data(symbol)
    df = pd.DataFrame(data)

    df["time"] = (
        pd.to_datetime(df["time"], unit="s", utc=True)
          .dt.tz_convert("Asia/Kolkata")
    )

    df["sma3"] = df["close"].rolling(3).mean()
    return df, symbol

if __name__ == "__main__":
    connect()
    print(get_data())