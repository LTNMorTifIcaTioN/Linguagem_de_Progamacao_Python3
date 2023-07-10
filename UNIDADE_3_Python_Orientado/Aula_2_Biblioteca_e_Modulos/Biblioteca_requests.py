"""
A biblioteca requests habilita funcionalidades do protocolo HTTP, como o get e o post. Dentre seus métodos,
o get() é o responsável por capturar informação da internet. A documentação sobre ela está disponível no endereço.
Essa biblioteca foi construída com o intuito de substituir o módulo urllib2,
que demanda muito trabalho para obter os resultados.
O método get() permite que você informe a URL de que deseja obter informação.
Sua sintaxe é: requests.get('https://XXXXXXX').
"""
 # primeiro passo extrair as informações com o request utilizando o método json().

import requests

info = requests.get('https://api.github.com/events')
print(info.headers)

print(info.headers['date']) # Data de extração
print(info.headers['server']) # Servidor de origem
# print(info.headers['status']) # Status HTTP da extração, 200 é ok
print(info.encoding) # Encoding do texto
print(info.headers['last-modified']) # Data da última modificação da informação

texto_str = info.text
print(type(texto_str))
print(texto_str[:200]) # exibe somente os 100 primeiros caracteres

texto_json = info.json()
print(type(texto_json))
print(texto_json[0])
