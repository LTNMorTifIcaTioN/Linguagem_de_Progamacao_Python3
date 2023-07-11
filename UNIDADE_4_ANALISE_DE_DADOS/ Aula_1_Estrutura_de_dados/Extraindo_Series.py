"""
Atributo shape: Verifica quantas linhas a Series possui (quantos índices).
método count(): conta quantos dados não nulos existem.
"""
import pandas as pd

series_dados = pd.Series([10.2, -1, None, 15, 23.4])

print('Quantidade de linhas = ', series_dados.shape) # Retorna uma tupla com o número de linhas
print('Tipo de dados', series_dados.dtypes) # Retorna o tipo de dados, se for misto será object
print('Os valores são únicos?', series_dados.is_unique) # Verifica se os valores são únicos (sem duplicações)
print('Existem valores nulos?', series_dados.hasnans) # Verifica se existem valores nulos
print('Quantos valores existem?', series_dados.count()) # Conta quantas valores existem (excluí os nulos)
print('Qual o menor valor?', series_dados.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor?', series_dados.max()) # Extrai o valor máximo, com a mesma condição do mínimo
print('Qual a média aritmética?', series_dados.mean()) # Extrai a média aritmética de uma Series numérica
print('Qual o desvio padrão?', series_dados.std()) # Extrai o desvio padrão de uma Series numérica
print('Qual a mediana?', series_dados.median()) # Extrai a mediana de uma Series numérica
print('\nResumo:\n', series_dados.describe()) # Exibe um resumo sobre os dados na Series
print('===============================================================================================================')
print()

# DATAFRAME
"""
Para construir um objeto do tipo DataFrame, precisamos utilizar o método DataFrame() do pacote pandas.
O método possui o seguinte construtor: pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False).

Dentre todos os parâmetros esperados, somente um é obrigatório para se criar um DataFrame com dados,
o parâmetro data=XXXX. Esse parâmetro pode receber, um objeto iterável, como uma lista, tupla,
um dicionário ou um DataFrame 
"""

# CONSTRUTOR DATAFRAME COM LISTA

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

print(pd.DataFrame(lista_nomes, columns=['nome']))
print('===============================================================================================================')
print()

print(pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs))
print('===============================================================================================================')
print()

dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas
print(pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email']))
print('===============================================================================================================')
print()


# CONSTRUTOR DATA FRAME COM DICIONÁRIO
"""
 Cada chave será uma coluna e pode ter atribuída uma lista de valores.
 Obs: cada chave deve estar associada a uma lista de mesmo tamanho.
"""

dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

print(pd.DataFrame(dados))