import MetaTrader5 as mt5

def fechar_todas(symbol=None):
    if not mt5.initialize():
        print("Falha:", mt5.last_error())
        return

    positions = mt5.positions_get(symbol=symbol) if symbol else mt5.positions_get()
    if positions is None or len(positions) == 0:
        print("Nenhuma posição para fechar")
        mt5.shutdown()
        return

    for pos in positions:
        tick = mt5.symbol_info_tick(pos.symbol)
        if tick is None:
            continue

        tipo = mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
        price = tick.bid if tipo == mt5.ORDER_TYPE_SELL else tick.ask

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": pos.symbol,
            "volume": pos.volume,
            "type": tipo,
            "position": pos.ticket,
            "price": price,
            "deviation": 20,
            "magic": pos.magic,
            "comment": "fechar python",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(request)
        print(f"Fechando {pos.symbol} ticket {pos.ticket}: {result.retcode}")

    mt5.shutdown()

if __name__ == "__main__":
    fechar_todas()
