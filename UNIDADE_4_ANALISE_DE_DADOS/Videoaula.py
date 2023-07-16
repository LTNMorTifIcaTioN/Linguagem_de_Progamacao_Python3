# CIÊNCIA DE DADOS - CONCEITOS
"""
Dados
- O tempo to_do nós geramos dados.
Como geramos os dados?
    Os dados são produzidos por algum tipo de dispositivo, como por exemplo, um texto digitado em uma rede social,
    um sensor, uma foto tirada na câmera do celular e etc.

* Campo interdisciplinar que visa resolver problemas reais, com o uso de métodos estatísticos para gerar uma visão
preditiva;

Big Data
* grande volume de dados com diversos tipos que são gerados em altas velocidades;
* Metodologia para captura, armazenamento e processamento de informação;
* Matéria prima para a ciência de dados.

Ciclo de Vida dos Dados:
    ... -> Produção -> Armazenamento -> Transformação -> Análise -> Descarte -> ...

Utilização destes dados
* Direcionamento de propaganda;
* Sistemas Especioalistas;
* Previsão de vendas;
* IoT;
"""

# Introdução A Biblioteca Pandas
"""
Pandas
* Biblioteca para manipulação e análise de dados;
* Integração com diversos tipos de arquivos, por exemplo: aql, excel, csv e etx...;
* Plotagem dos dados utilizando o Matplotlib;
* Estatísticas básicas são facilmente calculadas;
    import pandas as pd

DataFrame
* Estrutura de dados bidimensional com colunas de tipos potencialmente diferentes;
* Semelhante a uma planilha;
* Tipos possíveis: dicionários, listas, arrays, séries, outro, ...;
"""

# DataFrame
import pandas as pd

df = pd.DataFrame({
    "Nome": ["João da Silva",
             "Carlos Souza",
             "Maria Ferreira"],
        "Idade": [22, 35, 58],
        "Sexo": ["masculino", "masculino", "feminino"]}
)

print(df)
print('\n===========================================================================================================\n')


# Series
"""
Estrutura de dados unidimensional capaz de conter qualquer tipo de dados;
s = pd.Series(data, index = index)
"""
import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

print(s)
print('\n===========================================================================================================\n')


d = {'b': 1, 'a': 0, 'c': 2}
s = pd.Series(d)
print(s)
print('\n===========================================================================================================\n')

cliente = {"Nome": ['Marcelo', 'Ana', 'Maria'],
           "Idade": [33, 26, 45]}
print(cliente)
print()
dataframe = pd.DataFrame(cliente)
print(dataframe)
print('\n===========================================================================================================\n')

vetor = np.array([5, 6, 7, 8])
v = pd.Series(vetor)
print(vetor)
print()
print(v)
print('\n===========================================================================================================\n')


# INTRODUÇÃO A MANIPULAÇÃO DE DADOS EM PANDAS

# Manipulação de arquivos delimitados (CSV)
"""
Formato CSV: armazena os dados separados por vírgula em cada linha do arquivo.
Nome, Idade
Marcos, 35
Eduardo, 33
Aline, 29
Lais, 34

df = pd.read_csv("Arquivo.csv", encoding = "UTF-8", sep = ",")

* Cabeçalho é opcional;
* Números decimais devem ser separados por ponto(.);
* Separador pode ser virgula (,) ou ponto e vírgula (;):
"""

# Manipulação de arquivos chave-valor (JSON)
"""
Formato JSON (JavaScript Object Notation): armazena informações estruturadas e é utilizado principalmente para
transferir dados entre um servidor e um cliente;
-> É composto por chave e valor.

{'cidade': 'São Paulo', 'país': 'Brasil'}

df = pd.read_json('Arquivo.json')
"""

# Manipulação de banco de dados com Pandas
"""
df = pd.read_sql_query()
df = read_sql_table()
df.to_sql()
"""
import pandas as pd
import sqlite3

conector = sqlite3.connect("conta.db")
df = pd.read_sql_query("SELECT * from cadastro", conector)
print(df.head())
print('\n===========================================================================================================\n')


# VISUALIZAÇÃO DE DADOS EM PYTHON
"""
* Matplotlib;
* Seaborn-Count plot;
* Scatter plot;
"""

import pandas as pd
import matplotlib.pyplot as plt

Data = {'Ano': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
        'Taxa_Desemprego': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
        }

df = pd.DataFrame(Data, columns=['Ano', 'Taxa_Desemprego'])

df.plot(x='Ano', y='Taxa_Desemprego', kind='line')
plt.show()

df.plot(x='Ano', y='Taxa_Desemprego', kind='bar')
plt.show()

df.plot(x='Ano', y='Taxa_Desemprego', kind='box')
plt.show()

df.plot.scatter(x='Ano', y='Taxa_Desemprego')
plt.show()