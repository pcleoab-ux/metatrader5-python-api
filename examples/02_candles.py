import MetaTrader5 as mt5
import pandas as pd

if not mt5.initialize():
    print("Falha:", mt5.last_error())
    quit()

# Baixar 100 candles de EURUSD no M5
rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M5, 0, 100)

if rates is None:
    print("Erro ao baixar candles:", mt5.last_error())
else:
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df.tail(10))

mt5.shutdown()
