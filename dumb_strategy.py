from basic import *
from data_management import get_data

connect()
df = get_data()

current = df.iloc[-1]
previous = df.iloc[-2]

print(current)
print(previous)