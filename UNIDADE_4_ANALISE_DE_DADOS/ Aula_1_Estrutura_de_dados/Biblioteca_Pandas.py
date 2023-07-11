"""
Dentre as diversas bibliotecas disponíveis no repositório PyPI, pandas é um pacote Python que fornece
estruturas de dados projetadas para facilitar o trabalho com dados estruturados (tabelas) e de séries temporais.
Pandas pretende ser o alicerce de alto nível fundamental para uma análise prática, a dos dados do mundo real em Python.

* Para utilizar a biblioteca pandas é preciso fazer a instalação: pip install pandas

Como uma ferramenta de alto nível, pandas possui duas estruturas de dados que são as principais para a
análise/manipulação de dados: a Series e o DataFrame.
* Uma Series é um como um vetor de dados (unidimencional), capaz de armazenar diferentes tipos de dados.
* Um DataFrame é conjunto de Series, ou como a documentação apresenta, um contêiner para Series.
Ambas estruturas, possuem como grande característica, a indexação das linhas, ou seja,
cada linha possui um rótulo (nome) que o identifica, o qual pode ser uma string, uma inteiro, um decimal ou uma data.
Podemos comparar um DataFrame como uma planilha eletrônico, como o Excel (da Microsoft) ou o Calc (do Open Office).
"""

import pandas as pd

"""
Series - Para construir um objeto do tipo Series, precisamos utilizar o método Series() do pacote pandas.
O método possui o seguinte construtor: 
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False).
"""

print(pd.Series(data=5)) # Cria uma Series com o valor a
print('===============================================================================================================')
print()

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
print(pd.Series(lista_nomes)) # Cria uma Series com uma lista de nomes
print('===============================================================================================================')
print()

dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}
print(pd.Series(dados)) # Cria uma Series com um dicionário
print('===============================================================================================================')
print()

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
print(pd.Series(lista_nomes, index=cpfs))
print('===============================================================================================================')
print()

series_dados = pd.Series(lista_nomes, index=cpfs)

print(series_dados.loc['111.111.111-11'])