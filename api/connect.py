## Importa a lib requests e o plugin RequestException
import requests
from requests import RequestException

## Função conecta com a api e retorna a resposta JSON
def connect():
        try:
         url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
         response = requests.get(url, timeout=5)
         response.raise_for_status()
         return response.json()

        except RequestException as e:
            print(f"Failed ao conectar com a Api: {e}")






