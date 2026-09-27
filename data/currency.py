# Acessar chave da moeda
def get_currency(data, currency):
    return data.get(currency)

# informações sobre a conversão
def display_currency_info(currency):
    print(f'Moeda: {currency['code']}')
    print(f'Nome: {currency['name']}')
    print(f'Compra: {currency['bid']}')
    print(f'Venda: {currency['ask']}')
    print(f'Máxima: {currency['high']}')
    print(f'Mínima: {currency['low']}')

# Converter
def get_conversion(amount: float, currency):
    return amount * float(currency['bid'])


