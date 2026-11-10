import MetaTrader5 as mt5
import pandas as pd

if not mt5.initialize():
    print("Falha:", mt5.last_error())
    quit()

positions = mt5.positions_get()

if positions is None or len(positions) == 0:
    print("Nenhuma posição aberta")
else:
    df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
    print(df[['ticket', 'symbol', 'type', 'volume', 'price_open', 'profit']])

mt5.shutdown()
