from datetime import datetime, UTC
from basic import *

connect()

tick = mt5.symbol_info_tick("EURUSD")

print(tick.time)
print(datetime.fromtimestamp(tick.time, UTC))