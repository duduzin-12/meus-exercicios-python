import requests

# Teste de API
cep = "31610210"

url_api =f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url_api)

dados = resposta.json()

print(f"Logadouro: {dados['logradouro']}, Bairro: {dados['bairro']}, Localidade: {dados['localidade']}")