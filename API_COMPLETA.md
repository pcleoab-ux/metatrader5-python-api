# Referência Completa — MetaTrader 5 Python API

Documentação oficial: [https://www.mql5.com/en/docs/python_metatrader5](https://www.mql5.com/en/docs/python_metatrader5)

## Instalação

```bash
pip install MetaTrader5
```

---

## 1. Conexão e Terminal

| Função | Descrição | Retorno |
|--------|-----------|--------|
| `initialize()` | Conecta ao terminal MT5 | bool |
| `initialize(path, login, password, server, timeout, portable)` | Conecta com parâmetros | bool |
| `login(login, password, server, timeout)` | Faz login em uma conta | bool |
| `shutdown()` | Fecha a conexão | None |
| `version()` | Retorna versão do terminal | tuple (version, build, date) |
| `last_error()` | Último erro ocorrido | tuple |
| `terminal_info()` | Informações do terminal | namedtuple |

---

## 2. Conta

| Função | Descrição | Retorno |
|--------|-----------|--------|
| `account_info()` | Informações da conta atual | namedtuple |

---

## 3. Símbolos

| Função | Descrição | Retorno |
|--------|-----------|--------|
| `symbols_total()` | Total de símbolos | int |
| `symbols_get(group="")` | Lista de símbolos | tuple |
| `symbol_info(symbol)` | Informações de um símbolo | namedtuple |
| `symbol_info_tick(symbol)` | Último tick | namedtuple |
| `symbol_select(symbol, selected=True)` | Adiciona/remove do Market Watch | bool |

---

## 4. Market Depth (Book)

| Função | Descrição | Retorno |
|--------|-----------|--------|
| `market_book_add(symbol)` | Assina o book | bool |
| `market_book_get(symbol)` | Retorna o book | tuple |
| `market_book_release(symbol)` | Cancela assinatura | bool |

---

## 5. Candles (Rates)

| Função | Descrição |
|--------|-----------|
| `copy_rates_from(symbol, timeframe, date_from, count)` | Candles a partir de uma data |
| `copy_rates_from_pos(symbol, timeframe, start_pos, count)` | Candles a partir de uma posição |
| `copy_rates_range(symbol, timeframe, date_from, date_to)` | Candles em um intervalo |

---

## 6. Ticks

| Função | Descrição |
|--------|-----------|
| `copy_ticks_from(symbol, date_from, count, flags)` | Ticks a partir de uma data |
| `copy_ticks_range(symbol, date_from, date_to, flags)` | Ticks em um intervalo |

---

## 7. Ordens

| Função | Descrição |
|--------|-----------|
| `orders_total()` | Número de ordens ativas |
| `orders_get(symbol="", ticket=0)` | Lista de ordens ativas |
| `order_calc_margin(action, symbol, volume, price)` | Calcula margem |
| `order_calc_profit(action, symbol, volume, price_open, price_close)` | Calcula lucro |
| `order_check(request)` | Valida uma ordem |
| `order_send(request)` | Envia uma ordem |

---

## 8. Posições

| Função | Descrição |
|--------|-----------|
| `positions_total()` | Número de posições abertas |
| `positions_get(symbol="", ticket=0)` | Lista de posições |

---

## 9. Histórico

| Função | Descrição |
|--------|-----------|
| `history_orders_total(date_from, date_to)` | Total de ordens no histórico |
| `history_orders_get(date_from, date_to, group="")` | Ordens do histórico |
| `history_deals_total(date_from, date_to)` | Total de negócios |
| `history_deals_get(date_from, date_to, group="")` | Negócios do histórico |

---

## Constantes úteis

### Timeframes
```python
mt5.TIMEFRAME_M1
mt5.TIMEFRAME_M5
mt5.TIMEFRAME_M15
mt5.TIMEFRAME_M30
mt5.TIMEFRAME_H1
mt5.TIMEFRAME_H4
mt5.TIMEFRAME_D1
mt5.TIMEFRAME_W1
mt5.TIMEFRAME_MN1
```

### Tipos de ordem
```python
mt5.ORDER_TYPE_BUY
mt5.ORDER_TYPE_SELL
mt5.ORDER_TYPE_BUY_LIMIT
mt5.ORDER_TYPE_SELL_LIMIT
mt5.ORDER_TYPE_BUY_STOP
mt5.ORDER_TYPE_SELL_STOP
```

### Ações de trade
```python
mt5.TRADE_ACTION_DEAL
mt5.TRADE_ACTION_PENDING
mt5.TRADE_ACTION_SLTP
mt5.TRADE_ACTION_MODIFY
mt5.TRADE_ACTION_REMOVE
mt5.TRADE_ACTION_CLOSE_BY
```

### Filling
```python
mt5.ORDER_FILLING_FOK
mt5.ORDER_FILLING_IOC
mt5.ORDER_FILLING_RETURN
mt5.ORDER_FILLING_BOC
```

---

## Observação importante

Esta é a lista das **funções documentadas oficialmente** da biblioteca `MetaTrader5` da MetaQuotes.

O código-fonte da biblioteca é fechado. A referência completa e atualizada sempre está em:

https://www.mql5.com/en/docs/python_metatrader5
