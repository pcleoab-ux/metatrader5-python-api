import MetaTrader5 as mt5

def calcular_lote(saldo, risco_percentual, stop_loss_pips, pip_value=10):
    """Calcula o tamanho do lote baseado no risco."""
    risco_valor = saldo * (risco_percentual / 100)
    lote = risco_valor / (stop_loss_pips * pip_value)
    return round(max(0.01, lote), 2)

def verificar_risco_conta():
    if not mt5.initialize():
        print("Falha:", mt5.last_error())
        return

    account = mt5.account_info()
    if account is None:
        print("Não foi possível obter informações da conta")
        mt5.shutdown()
        return

    print(f"Saldo: {account.balance:.2f}")
    print(f"Equity: {account.equity:.2f}")
    print(f"Margem Livre: {account.margin_free:.2f}")
    print(f"Drawdown: {((account.balance - account.equity) / account.balance * 100):.2f}%")

    # Exemplo de cálculo de lote
    lote = calcular_lote(account.balance, 1.0, 20)
    print(f"\nLote sugerido (1% risco, 20 pips SL): {lote}")

    mt5.shutdown()

if __name__ == "__main__":
    verificar_risco_conta()
