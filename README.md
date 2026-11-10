# MetaTrader 5 Python API

Documentação e exemplos da **API oficial** do MetaTrader 5 para Python.

Documentação oficial: [https://www.mql5.com/en/docs/python_metatrader5](https://www.mql5.com/en/docs/python_metatrader5)

## Instalação

```bash
pip install MetaTrader5
```

Requisitos:
- Windows (ou Wine no Linux)
- MetaTrader 5 instalado e aberto
- Conta logada (demo ou real)

## Funções Principais

### Conexão
| Função | Descrição |
|--------|-----------|
| `initialize()` | Conecta ao terminal |
| `login()` | Login em uma conta |
| `shutdown()` | Fecha a conexão |
| `version()` | Versão do terminal |
| `last_error()` | Último erro |

### Informações
| Função | Descrição |
|--------|-----------|
| `account_info()` | Dados da conta |
| `terminal_info()` | Status do terminal |
| `symbols_total()` | Total de símbolos |
| `symbols_get()` | Lista de símbolos |
| `symbol_info()` | Info de um símbolo |
| `symbol_info_tick()` | Último tick |

### Dados de Mercado
| Função | Descrição |
|--------|-----------|
| `copy_rates_from()` | Candles a partir de uma data |
| `copy_rates_from_pos()` | Candles a partir de uma posição |
| `copy_rates_range()` | Candles em um intervalo |
| `copy_ticks_from()` | Ticks a partir de uma data |
| `copy_ticks_range()` | Ticks em um intervalo |

### Operações
| Função | Descrição |
|--------|-----------|
| `order_send()` | Envia ordem |
| `order_check()` | Valida ordem |
| `orders_total()` / `orders_get()` | Ordens abertas |
| `positions_total()` / `positions_get()` | Posições abertas |
| `history_orders_get()` | Histórico de ordens |
| `history_deals_get()` | Histórico de negócios |

## Exemplos

Veja a pasta `examples/` para scripts prontos.

## Licença

Este repositório contém apenas documentação e exemplos. A biblioteca `MetaTrader5` é propriedade da MetaQuotes.
