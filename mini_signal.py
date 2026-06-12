from data_management import get_data

df = get_data()
print(df)

current = df.iloc[-1]
previous = df.iloc[-2]

buy_signal = (
    previous["close"] < previous["sma3"]
    and
    current["close"] > current["sma3"]
)

sell_signal = (
    previous["close"] > previous["sma3"]
    and
    current["close"] < current["sma3"]
)

if buy_signal:
    print("BUY")

elif sell_signal:
    print("SELL")

else:
    print("NO SIGNAL")