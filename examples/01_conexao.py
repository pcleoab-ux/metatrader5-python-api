import MetaTrader5 as mt5

# Conectar ao terminal
if not mt5.initialize():
    print("Falha ao inicializar:", mt5.last_error())
    quit()

print("Conectado com sucesso!")
print("Versão:", mt5.version())
print("Info do terminal:", mt5.terminal_info())

mt5.shutdown()
