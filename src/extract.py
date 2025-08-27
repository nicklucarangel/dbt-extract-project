# Import
import yfinance as yf
import pandas as pd

# Get the price data for commodity assets
def buscar_dados_commodities(simbolo, periodo='10d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)  # usar simbolo, não lista
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)



