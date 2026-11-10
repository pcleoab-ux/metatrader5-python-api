import MetaTrader5 as mt5
import pandas as pd
import numpy as np

if not mt5.initialize():
    print("Falha:", mt5.last_error())
    quit()

symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_M5
candles = 200

rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, candles)
if rates is None:
    print("Erro ao baixar candles")
    mt5.shutdown()
    quit()

df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df['time'], unit='s')

# Médias Móveis
df['sma_20'] = df['close'].rolling(20).mean()
df['sma_50'] = df['close'].rolling(50).mean()
df['ema_12'] = df['close'].ewm(span=12, adjust=False).mean()
df['ema_26'] = df['close'].ewm(span=26, adjust=False).mean()

# RSI
def rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

df['rsi'] = rsi(df['close'])

# MACD
df['macd'] = df['ema_12'] - df['ema_26']
df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()

print(df[['time', 'close', 'sma_20', 'sma_50', 'rsi', 'macd']].tail(10))

mt5.shutdown()
