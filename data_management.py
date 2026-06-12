# IMPORT
import pandas as pd
from basic import *

# CONNECT
connect()

def get_data():
    data = fetch_market_data()
    df = pd.DataFrame(data)

    df["time"] = (
        pd.to_datetime(df["time"], unit="s", utc=True)
          .dt.tz_convert("Asia/Kolkata")
    )

    df["sma3"] = df["close"].rolling(3).mean()
    return df

if __name__ == "__main__":
    print(get_data())