## padrão de títulos do programa
def title(title):
    print("=" *40)
    print(f"{title.center(40, '´').upper()}")
    print("="*40)

## Exemplo de menu para escolher conversão
def choice_currency():
    title('Escolha uma moeda para conversão')
    print("1. Dólar")
    print("2. Euro")
    print("3. Bitcoin")

    try:
        choice = int(input('>>> '))
        return choice

    except ValueError as e:
        print(f'Valor invalido: {e}')

