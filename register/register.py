def register():
    try:
        nome = str(input("Qual o seu nome? "))
        amount = float(input("Quanto você tem na carteira? R$ "))

        return {
            'name': nome,
            'amount': amount

        }
    except Exception as e:
        print(e)
