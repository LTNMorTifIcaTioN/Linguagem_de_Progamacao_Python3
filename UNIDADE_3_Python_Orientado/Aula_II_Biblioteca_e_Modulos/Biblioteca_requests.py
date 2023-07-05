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

import datetime as dt

jogos = requests.get('http://worldcup.sfg.io/matches').json()

print(type(jogos))

# segundo passo: percorrer cada dicionário da lista (ou seja, cada jogo) extraindo as informações

info_relatorio = []

file = open('relatorio_jogos.txt', "w") # cria um arquivo txt na pasta em que está trabalhando.

for jogo in jogos:
    data = jogo['datetime'] # extrai a data
    data = dt.datetime.strptime(data, "%Y-%m-%dT%H:%M:%SZ") # converte de string para data
    data = data.strftime("%d/%m/%Y") # formata
    nome_time1 = jogo['home_team_country']
    nome_time2 = jogo['away_team_country']
    gols_time1 = jogo['home_team']['goals']
    gols_time2 = jogo['away_team']['goals']

    linha = f"({data}) - {nome_time1} x {nome_time2} = {gols_time1} a {gols_time2}"

    file.write(linha + '\n') # escreve a linha no arquivo txt

    info_relatorio.append(linha)

file.close() # é preciso fechar o arquivo
info_relatorio[:5]