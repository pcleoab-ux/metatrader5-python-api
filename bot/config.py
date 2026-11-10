# ===================== CONFIGURAÇÃO DO BOT =====================

# Conta (deixe None para usar a conta já logada no terminal)
LOGIN = None
PASSWORD = None
SERVER = None

# Operação
SYMBOL = "EURUSD"
TIMEFRAME = "M5"          # M1, M5, M15, M30, H1, H4, D1
LOT_FIXO = 0.01           # Se quiser lote fixo, use isso
USAR_RISCO_PERCENTUAL = False
RISCO_PERCENTUAL = 1.0    # % do saldo por operação

# Estratégia (RSI + Média)
RSI_PERIOD = 14
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
MA_PERIOD = 50

# Gerenciamento
STOP_LOSS_PIPS = 20
TAKE_PROFIT_PIPS = 40
MAX_POSICOES = 1
MAGIC = 202611

# Controle
INTERVALO_SEGUNDOS = 10
# ===============================================================
