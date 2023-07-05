"""
Como desenvolvedor em uma empresa de consultoria de software,
você foi alocado em um projeto com base no qual o cliente deseja automatizar a extração dos dados do CNAE
e gerar um relatório. Os dados estão disponíveis neste endereço. Você deve extraí-los e gerar as seguintes informações:

Quantas atividades distintas estão registradas?
Quantos grupos de atividades existem?
Quantas atividades estão cadastradas em cada grupo?
Qual grupo ou quais grupos possuem o maior número de atividades vinculadas?
"""

import requests

dados = requests.get('https://servicodados.ibge.gov.br/api/v2/cnae/classes').json() # resulta em uma lista de diconários
print(dados[0]) # exibindo o primeiro registro de dados (primeiro dicionário da lista)
print()

# Quantidade distintas de atividades, basta saber o tamanho da lista.
qtde_atividades_distintas = len(dados)
print(qtde_atividades_distintas)
print()

# Criar uma lista dos grupos de atividades, extraindo a descrição de cada registro
grupos = []
for registro in dados:
    grupos.append(registro['grupo']['descricao'])
print(grupos[:10])
print()

# A partir da lista, podemos extrair a quantidade de grupos de atividades
qtde_grupos_distintos = len(set(grupos)) # o construtor set cria uma estrutura de dados removendo as duplicações.
print(qtde_grupos_distintos)
print()

# Resultado é uma lista de tuplas. Cria uma nova lista com o grupo e a quantidade de atividades pertencentes a ele
grupos_count = [(grupo, grupos.count(grupo)) for grupo in set(grupos)]
print(grupos_count[:5])
print()

# Por conveniência, transformamos a lista em um dicionário
grupos_count = dict(grupos_count)
print(grupos_count)
print()

# A partir do dicionário vamos descobrir qual (ou quais) grupos possuem mais atividades
valor_maximo = max(grupos_count.values())
grupos_mais_atividades = [chave for (chave, valor) in grupos_count.items() if valor == valor_maximo]
print(len(grupos_mais_atividades))

import requests
from datetime import datetime

class ETL:
    def __init__(self):
        self.url = None

    def extract_cnae_data(self, url):
        self.url = url
        data_extracao = datetime.today().strftime("%Y/%m/%d - %H:%M:%S")
        # Faz extração
        dados = requests.get(self.url).json()
         # Extrai os grupos dos registros
        grupos = []
        for registro in dados:
            grupos.append(registro['grupo']['descricao'])
        # Cria uma lista de tuplas (grupo, quantidade_atividades)
        grupos_count = [(grupo, grupos.count(grupo)) for grupo in set(grupos)]
        grupos_count = dict(grupos_count)  # transforma a lista em dicionário
        valor_maximo = max(grupos_count.values())  # Captura o valor máximo de atividades
        # Gera uma lista com os grupos que possuem a quantidade máxima de atividades
        grupos_mais_atividades = [chave for (chave, valor) in grupos_count.items() if valor == valor_maximo]
        # informações
        qtde_atividades_distintas = len(dados)
        qtde_grupos_distintos = len(set(grupos))
        print(f"Dados extraídos em: {data_extracao}")
        print(f"Quantidade de atividades distintas = {qtde_atividades_distintas}")
        print(f"Quantidade de grupos distintos = {qtde_grupos_distintos}")
        print(f"Grupos com o maior número de atividades = {grupos_mais_atividades}, atividades = {valor_maximo}")
        return None

# Usando a classe ETL

ETL().extract_cnae_data('https://servicodados.ibge.gov.br/api/v2/cnae/classes')

