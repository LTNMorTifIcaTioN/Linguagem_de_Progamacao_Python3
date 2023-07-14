"""
Em to_do esse trabalho é comum fazer a divisão em duas etapas: (i) captura e transformação/padronização dos dados,
(ii) extração de informações.

Etapa de captura e transformação/padronização dos dados - A extração dos dados pode ser realizada por meio do
método read_json() e guardando em um DataFrame (DF) pandas. Ao carregar os dados em um DF,
podemos visualizar quantas linhas e colunas, bem como, os tipos de dados em cada coluna, com o método info().
"""

import pandas as pd

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
print(df_selic.info())


# Remover linhas duplicadas
"""
Para o carregamento de uma base de dados, um dos primeiros tratamentos que devemos fazer é remover os dados duplicados.
Um DataFrame da biblioteca pandas possui o método meu_df.drop_duplicates() que permite essa remoção de dados duplicados.
"""

df_selic.drop_duplicates(keep='last', inplace=True)


# Criar novas colunas e Método TO_DATETIME() e ASTYPE
"""
A sintaxe é similar a criar uma nova chave em um dicionário: meu_df['nova_coluna'] = dado.
Vamos criar uma coluna que adiciona a data de extração das informações. Observe a seguir, do módulo datetime,
estamos usando a classe date e o método today(). 
"""

from datetime import date

from datetime import datetime as dt

data_extracao = date.today()
df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Autora"

print(df_selic.info())
print(df_selic.head())
print('\n###########################################################################################################\n')


# Método TO_DATETIME() e ASTYPE:
"""
Trabalhar com o tipo "data" pode trazer vantagens, como por exemplo, ordenar da data mais recente para mais antiga,
ou ainda verificar a variação da taxa selic em um determinado período.
Vamos utilizar os métodos pandas.to_datime() e minha_series.astype() para fazer a conversão
e transformar as colunas data e data_extracao.
"""

df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
df_selic['data_extracao'] = df_selic['data_extracao'].astype('datetime64[ns]')

print(df_selic.info())
print(df_selic.head())
print('\n###########################################################################################################\n')


# Series.str e Método RESET_INDEX() e SET_INDEX()
"""
Observe o trecho de código seguir, selecionamos a coluna responsável,
acessamos o recurso str e aplicamos o método upper().
Dessa forma, a biblioteca pandas "entende" que queremos converter todos os valores dessa coluna para letras maiúsculas.
Como atribuímos o resultado na própria coluna, o valor antigo é substituído.
"""

df_selic['responsavel'] = df_selic['responsavel'].str.upper()
print(df_selic.head())
print('\n###########################################################################################################\n')


# Método SORT_VALUES():
"""
- No código a seguir, estamos usando o método sort_values() que permite ordenar o DF,
de acordo com os valores de uma coluna.
"""

df_selic.sort_values(by='data', ascending=False, inplace=True)
print(df_selic.head())
print('\n###########################################################################################################\n')


# Método RESET_INDEX() e SET_INDEX():
"""
As únicas formas de alterar o índice são com os métodos reset_index() e set_index().
O primeiro redefine o índice usando o padrão e o segundo utiliza definições de novos índices.
"""

df_selic.reset_index(drop=True, inplace=True)
print(df_selic.head())
print('\n###########################################################################################################\n')



"""
Durante a transformação dos dados, pode ser necessário definir novos valores para os índices,
ao invés de usar o range numérico. Essa transformação pode ser feita usando o método meu_df.set_index().
O método permite especificar os novos valores usando uma coluna já existente ou então passando uma lista,
de tamanho igual a quantidade de linhas.
"""

lista_novo_indice = [f'selic_{indice}' for indice in df_selic.index]
print(lista_novo_indice[:5])

df_selic.set_index(keys=[lista_novo_indice], inplace=True)
print(df_selic.head())
print('\n###########################################################################################################\n')



"""
Ao especificar um índice com valor conceitual, podemos usar as funções idxmin() e idxmax()
para descobrir qual o índice do menor e do maior de uma Series.
"""

print(df_selic['valor'].idxmin())
print(df_selic['valor'].idxmax())
print('\n###########################################################################################################\n')


# Etapa de extração de informações
# Filtros com LOC:
"""
DataFrames da biblioteca pandas possuem uma propriedade chamada loc.
Essa propriedade permite acessar um conjunto de linhas (filtrar linhas),
por meio do índice ou por um vetor booleano (vetor de True ou False).
"""

print(df_selic.loc['selic_0'])
print()

print(df_selic.loc[['selic_0', 'selic_4', 'selic_200']])
print()

print(df_selic.loc[:'selic_5'])
print('\n###########################################################################################################\n')


"""
A propriedade loc aceita um segundo argumento, que é a coluna (ou colunas) que serão exibidas para os índices escolhidos.
"""

print(df_selic.loc[['selic_0', 'selic_4', 'selic_200'], 'valor'])
print()

print(df_selic.loc[['selic_0', 'selic_4', 'selic_200'], ['valor', 'data_extracao']])
print('\n###########################################################################################################\n')


"""
Vale mencionar que existe também a propriedade iloc, a qual filtra as linhas considerando a posição que ocupam no objeto. 
"""

print(df_selic.iloc[:5])
print('\n###########################################################################################################\n')


# Filtros com testes Booleanos
"""
Podemos usar operadores relacionais e lógicos para fazer testes condicionais com os valores das colunas de um DF.
Ao criarmos um teste condicional, internamente, a biblioteca testa todas as linhas do DF ou da Series,
retornando uma Series booleana, ou seja, composta por valores True ou False.
"""

teste = df_selic['valor'] < 0.01
print(type(teste))
print(teste[:5])
print('\n###########################################################################################################\n')


# Utilizamos o método to_datetime() para converter a string para data e então fazer a comparação.

teste2 = df_selic['data'] >= pd.to_datetime('2020-01-01')
print(type(teste2))
print(teste2[:5])
print('\n###########################################################################################################\n')


"""
O teste condicional pode ser construído também utilizando operadores lógicos. Para a operação lógica AND (E),
em pandas, usa-se o caracter &. Para fazer a operação lógica OR (OU), usa-se o caracter |.
Cada teste deve estar entre parênteses, senão ocorre um erro.
"""

teste3 = (df_selic['valor'] < 0.01) & (df_selic['data'] >= pd.to_datetime('2020-01-01'))
teste4 = (df_selic['valor'] < 0.01) | (df_selic['data'] >= pd.to_datetime('2020-01-01'))

print("Resultado do AND:\n")
print(teste3[:3])
print("Resultado do OR:\n")
print(teste4[:3])
print('\n###########################################################################################################\n')


"""
Agora que já sabemos criar as condições, basta aplicá-las no DataFrame para criar o filtro.
A construção é feita passando a condição para a propriedade loc.
"""

print(df_selic.loc[df_selic['valor'] < 0.01])
print('\n###########################################################################################################\n')


"""
odo esse filtro poderia ter sido escrito em uma única linha:
df_selic.loc[(df_selic['data'] >= pd.to_datetime('2020-01-01')) & (df_selic['data'] <= pd.to_datetime('2020-01-31'))]
Mas veja como fica mais difícil ler e interpretar o filtro, ainda mais para quem for dar manutenção no código.
"""

data1 = pd.to_datetime('2020-01-01')
data2 = pd.to_datetime('2020-01-31')
filtro_janeiro_2020 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)
df_janeiro_2020 = df_selic.loc[filtro_janeiro_2020]
print(df_janeiro_2020.head())
print('\n###########################################################################################################\n')


# No código a seguir, vamos criar um novo DF contendo as informações do mês de janeiro do ano de 2019

data1 = pd.to_datetime('2019-01-01')
data2 = pd.to_datetime('2019-01-31')
filtro_janeiro_2019 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)
df_janeiro_2019 = df_selic.loc[filtro_janeiro_2019]
print(df_janeiro_2019.head())
print('\n###########################################################################################################\n')


"""
Agora que temos três DFs, um completo e dois com filtros,
vamos utilizar métodos da estatística descritiva para extrair informações sobre o valor da taxa selic em cada DF.
Queremos saber, qual o valor máximo e mínimo registrado em cada caso e qual a média.
"""

print('Mínimo geral = ', df_selic['valor'].min())
print('Mínimo janeiro de 2019 = ', df_janeiro_2019['valor'].min())
print('Mínimo janeiro de 2020 = ',df_janeiro_2020['valor'].min(), '\n')
print('Máximo geral = ', df_selic['valor'].max())
print('Máximo janeiro de 2019 = ', df_janeiro_2019['valor'].max())
print('Máximo janeiro de 2020 = ',df_janeiro_2020['valor'].max(), '\n')
print('Média geral = ', df_selic['valor'].mean())
print('Média janeiro de 2019 = ', df_janeiro_2019['valor'].mean())
print('Média janeiro de 2020 = ',df_janeiro_2020['valor'].mean(), '\n')

df_selic.to_csv('dados_selic.csv')