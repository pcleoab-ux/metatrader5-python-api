import MetaTrader5 as mt5
import pandas as pd
import time
from datetime import datetime
from config import *

TIMEFRAME_MAP = {
    "M1": mt5.TIMEFRAME_M1,
    "M5": mt5.TIMEFRAME_M5,
    "M15": mt5.TIMEFRAME_M15,
    "M30": mt5.TIMEFRAME_M30,
    "H1": mt5.TIMEFRAME_H1,
    "H4": mt5.TIMEFRAME_H4,
    "D1": mt5.TIMEFRAME_D1,
}

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def conectar():
    if not mt5.initialize():
        log(f"Erro ao inicializar: {mt5.last_error()}")
        return False

    if LOGIN and PASSWORD and SERVER:
        if not mt5.login(LOGIN, password=PASSWORD, server=SERVER):
            log(f"Erro no login: {mt5.last_error()}")
            return False

    mt5.symbol_select(SYMBOL, True)
    log("Conectado com sucesso")
    return True

def obter_candles(qtd=100):
    tf = TIMEFRAME_MAP.get(TIMEFRAME, mt5.TIMEFRAME_M5)
    rates = mt5.copy_rates_from_pos(SYMBOL, tf, 0, qtd)
    if rates is None:
        return None
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def calcular_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def analisar():
    df = obter_candles(MA_PERIOD + RSI_PERIOD + 10)
    if df is None or len(df) < MA_PERIOD:
        return None

    df['rsi'] = calcular_rsi(df['close'], RSI_PERIOD)
    df['ma'] = df['close'].rolling(MA_PERIOD).mean()

    ultimo = df.iloc[-1]
    rsi = ultimo['rsi']
    preco = ultimo['close']
    ma = ultimo['ma']

    if rsi < RSI_OVERSOLD and preco > ma:
        return "BUY"
    elif rsi > RSI_OVERBOUGHT and preco < ma:
        return "SELL"
    return None

def posicoes_abertas():
    positions = mt5.positions_get(symbol=SYMBOL)
    if positions is None:
        return []
    return [p for p in positions if p.magic == MAGIC]

def calcular_lote():
    if not USAR_RISCO_PERCENTUAL:
        return LOT_FIXO

    account = mt5.account_info()
    if account is None:
        return LOT_FIXO

    info = mt5.symbol_info(SYMBOL)
    if info is None:
        return LOT_FIXO

    risco_valor = account.balance * (RISCO_PERCENTUAL / 100)
    pip_value = info.trade_tick_value * (info.point / info.trade_tick_size) * 10
    if pip_value == 0:
        return LOT_FIXO

    lote = risco_valor / (STOP_LOSS_PIPS * pip_value)
    return round(max(0.01, min(lote, info.volume_max)), 2)

def enviar_ordem(tipo):
    tick = mt5.symbol_info_tick(SYMBOL)
    if tick is None:
        return False

    info = mt5.symbol_info(SYMBOL)
    point = info.point
    price = tick.ask if tipo == "BUY" else tick.bid

    if tipo == "BUY":
        sl = price - STOP_LOSS_PIPS * point * 10
        tp = price + TAKE_PROFIT_PIPS * point * 10
        order_type = mt5.ORDER_TYPE_BUY
    else:
        sl = price + STOP_LOSS_PIPS * point * 10
        tp = price - TAKE_PROFIT_PIPS * point * 10
        order_type = mt5.ORDER_TYPE_SELL

    lote = calcular_lote()

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": lote,
        "type": order_type,
        "price": price,
        "sl": round(sl, info.digits),
        "tp": round(tp, info.digits),
        "deviation": 20,
        "magic": MAGIC,
        "comment": "bot completo",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        log(f"Ordem {tipo} enviada | Lote: {lote} | Preço: {price}")
        return True
    else:
        log(f"Erro ao enviar ordem: {result.retcode} - {result.comment}")
        return False

def loop():
    log("Bot iniciado")
    log(f"Símbolo: {SYMBOL} | Timeframe: {TIMEFRAME}")
    log("Pressione Ctrl+C para parar")

    try:
        while True:
            if len(posicoes_abertas()) >= MAX_POSICOES:
                log("Posição já aberta. Aguardando...")
            else:
                sinal = analisar()
                if sinal:
                    log(f"Sinal encontrado: {sinal}")
                    enviar_ordem(sinal)
                else:
                    log("Sem sinal")

            time.sleep(INTERVALO_SEGUNDOS)
    except KeyboardInterrupt:
        log("Bot parado pelo usuário")
    finally:
        mt5.shutdown()
        log("Conexão encerrada")

if __name__ == "__main__":
    if conectar():
        loop()
