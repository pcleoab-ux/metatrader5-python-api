# Bot Completo MT5

Bot autônomo para MetaTrader 5 usando a API oficial.

## Estratégia

- RSI + Média Móvel
- Compra quando RSI < 30 e preço acima da média
- Vende quando RSI > 70 e preço abaixo da média
- Stop Loss e Take Profit configuráveis

## Como usar

1. Abra o MetaTrader 5
2. Faça login na **conta demo**
3. Ative o **Algo Trading** (botão no topo)
4. Edite o arquivo `config.py` se quiser mudar símbolo, lote, etc.
5. Execute:

```bash
cd bot
pip install -r requirements.txt
python bot.py
```

## Parar o bot

Pressione `Ctrl + C`

## Aviso

Use primeiro em **conta demo**. Operação automatizada envolve risco.
