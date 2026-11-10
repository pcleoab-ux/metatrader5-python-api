import MetaTrader5 as mt5

if not mt5.initialize():
    print("Falha:", mt5.last_error())
    quit()

symbol = "EURUSD"
lot = 0.01

# Garantir que o símbolo está no Market Watch
mt5.symbol_select(symbol, True)

tick = mt5.symbol_info_tick(symbol)
if tick is None:
    print("Não foi possível obter o tick")
    mt5.shutdown()
    quit()

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": tick.ask,
    "deviation": 20,
    "magic": 234000,
    "comment": "python script",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

result = mt5.order_send(request)
print(result)

mt5.shutdown()
