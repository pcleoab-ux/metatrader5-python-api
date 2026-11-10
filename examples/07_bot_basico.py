import MetaTrader5 as mt5
import pandas as pd
import time

# ===================== CONFIGURAÇÃO =====================
SYMBOL = "EURUSD"
TIMEFRAME = mt5.TIMEFRAME_M5
LOT = 0.01
MAGIC = 123456
RSI_PERIOD = 14
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
# ========================================================

def calcular_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def tem_posicao_aberta():
    positions = mt5.positions_get(symbol=SYMBOL)
    return positions is not None and len(positions) > 0

def enviar_ordem(tipo):
    tick = mt5.symbol_info_tick(SYMBOL)
    if tick is None:
        return False

    price = tick.ask if tipo == mt5.ORDER_TYPE_BUY else tick.bid
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": LOT,
        "type": tipo,
        "price": price,
        "deviation": 20,
        "magic": MAGIC,
        "comment": "bot rsi",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    return result.retcode == mt5.TRADE_RETCODE_DONE

def loop():
    if not mt5.initialize():
        print("Falha ao conectar:", mt5.last_error())
        return

    mt5.symbol_select(SYMBOL, True)
    print(f"Bot iniciado | {SYMBOL} | RSI")

    try:
        while True:
            rates = mt5.copy_rates_from_pos(SYMBOL, TIMEFRAME, 0, RSI_PERIOD + 5)
            if rates is None or len(rates) < RSI_PERIOD:
                time.sleep(5)
                continue

            df = pd.DataFrame(rates)
            rsi_atual = calcular_rsi(df['close']).iloc[-1]

            print(f"RSI: {rsi_atual:.2f} | Posição aberta: {tem_posicao_aberta()}")

            if not tem_posicao_aberta():
                if rsi_atual < RSI_OVERSOLD:
                    print("Sinal de COMPRA")
                    enviar_ordem(mt5.ORDER_TYPE_BUY)
                elif rsi_atual > RSI_OVERBOUGHT:
                    print("Sinal de VENDA")
                    enviar_ordem(mt5.ORDER_TYPE_SELL)

            time.sleep(10)
    except KeyboardInterrupt:
        print("Bot parado pelo usuário")
    finally:
        mt5.shutdown()

if __name__ == "__main__":
    loop()
