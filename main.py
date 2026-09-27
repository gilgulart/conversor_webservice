## Arquivo Main será onde o programa vai de fato rodar (loop do programa)

## Importa a função de conexão com a API e função de conversão
from api.connect import connect
from data.currency import *
# ---------------------------

data = connect() # recebe os dados da API

# armazenamos as moedas em constantes (podemos add mais moedas)
USD = get_currency(data, "USDBRL")
EUR = get_currency(data, "EURBRL")
BTC = get_currency(data, "BTCBRL")
# --------------------------------------------

## Conversão: passar valor da carteira e a moeda em get_conversion(valor, moeda)
## Imprimir informações sobre a moeda: display_currency_info(moeda)


