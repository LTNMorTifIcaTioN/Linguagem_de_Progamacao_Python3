"""
No DataFrame temos o método info() que mostra quantas linhas e colunas existem.
Também exibe o tipo de cada coluna e quanto valores não nulos existem ali.
Esse método também retorna uma informação sobre a quantidade de memória RAM essa estrutura está ocupando.
"""
import pandas as pd

dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}
pd.DataFrame(dados)

df_dados = pd.DataFrame(dados)

print('\nInformações do DataFrame:\n')
print(df_dados.info()) # Apresenta informações sobre a estrutura do DF
print('\nQuantidade de linhas e colunas = ', df_dados.shape) # Retorna uma tupla com o número de linhas e colunas
print('\nTipo de dados:\n', df_dados.dtypes) # Retorna o tipo de dados, para cada coluna, se for misto será object
print('\nQual o menor valor de cada coluna?\n', df_dados.min()) # Extrai o menor de cada coluna
print('\nQual o maior valor?\n', df_dados.max()) # Extrai o valor máximo e cada coluna
# print('\nQual a média aritmética?\n', df_dados.mean()) # Extrai a média aritmética de cada coluna numérica
# print('\nQual o desvio padrão?\n', df_dados.std()) # Extrai o desvio padrão de cada coluna numérica
# print('\nQual a mediana?\n', df_dados.median()) # Extrai a mediana de cada coluna numérica
print('\nResumo:\n', df_dados.describe()) # Exibe um resumo
print(df_dados.head()) # Exibe os 5 primeiros registros do DataFrame
print('===============================================================================================================')
print()


# SELEÇÃO DE COLUNAS EM UM DATAFRAME
"""
Para selecionar uma coluna, as duas possíveis sintaxes são:

1 - nome_df.nome_coluna
2 - nome_df[nome_coluna]

A primeira forma é familiar aos desenvolvedores que utilizar a linguagem SQL,
porém ela não aceita colunas com espaços entre as palavras. Já a segunda aceita. 
Se precisarmos selecionar mais do que uma coluna, então precisamos passar uma lista, da seguinte forma:
nome_df[['col1', 'col2', 'col3']], se preferir a lista pode ser criada fora da seção e passada como parâmetro.
"""

df_uma_coluna = df_dados['idades']
print(type(df_uma_coluna))
print('Média de idades = ', df_uma_coluna.mean())
print('Desvio Padrão de idades = ', df_uma_coluna.std())
print('Mediana de idades = ', df_uma_coluna.median())
print(df_uma_coluna)
print('===============================================================================================================')
print()

colunas = ['nomes', 'cpfs']
df_duas_colunas = df_dados[colunas]
print(type(df_duas_colunas))
print(df_duas_colunas)
print('===============================================================================================================')
print()