"""
Podemos classificar os módulos (bibliotecas) em três categorias, cada uma das quais vamos estudar:
* Módulos built-in: embutidos no interpretador.
* Módulos de terceiros: criados por terceiros e disponibilizados via PyPI.
* Módulos próprios: criados pelo desenvolvedor.
"""

# Módulos built-in - Ao instalar o interpretador Python, também é feita a instalação de uma biblioteca de módulos.

"""
Módulo random - Random é um módulo built-in usado para criar números aleatórios. Vamos explorar as funções: 

* random.randint(a, b): retorna um valor inteiro aleatório, de modo que esse número esteja entre a, b. 
* random.choice(seq): extrai um valor de forma aleatória de uma certa sequência. 
* random.sample(population, k): retorna uma lista com k elementos, extraídos da população.
"""

import random

print(random.randint(0, 100))
print(random.choice([1, 10, -1, 100]))
print(random.sample(range(100000), k=12))

print()
print('==============================================================================================================')


"""
Módulo OS - OS é um módulo built-in usado para executar comandos no sistema operacional. Vamos explorar as funções:

* os.getcwd(): retorna uma string com o caminho do diretório de trabalho. 
* os.listdir(path='.'): retorna uma lista com todas as entradas de um diretório. Se não for especificado um caminho, 
então a busca é realizada em outro diretório de trabalho. 
* os.cpu_count(): retorna um inteiro com o número de CPUs do sistema. 
* os.getlogin(): retorna o nome do usário logado. 
* os.getenv(key): retorna uma string com o conteúdo de uma variável de ambiente especificada na key. 
* os.getpid(): retorna o id do processo atual.
"""

import os

print(os.getcwd())
print(os.listdir())
print(os.cpu_count())
print(os.getlogin())
print(os.getenv(key='path'))
print(os.getpid())

print()
print('==============================================================================================================')

"""
Módulo RE - O módulo re (regular expression) fornece funções para busca de padrões em um texto.
Uma expressão regular especifica um conjunto de strings que corresponde a ela.
As funções neste módulo permitem verificar se uma determinada string corresponde a uma determinada expressão regular.
Essa técnica de programação é utilizada em diversas linguagens de programação,
pois a construção de re depende do conhecimento de padrões. Vamos explorar as funções:

* re.search(pattern, string, flags=0): varre a string procurando o primeiro local onde o padrão de expressão regular
produz uma correspondência e o retorna. Retorna None se nenhuma correspondência é achada.
* re.match(pattern, string, flags=0): procura por um padrão no começo da string. Retorna None se a sequência não
corresponder ao padrão.
* re.split(pattern, string, maxsplit=0, flags=0): divide uma string pelas ocorrências do padrão.

O search() faz a procura em toda string, o match() faz a procura somente no começo (razão pela qual, portanto,
também encontrará neste caso) e o split() faz a transformação em uma lista.
"""

import re

string = 'meuArquivo_20-01-2020.py'
padrao = "[a-zA-Z]*"
texto1 = re.search(padrao, string).group()
texto2 = re.match(padrao, string).group()
texto3 = re.split("_", string)[0]

print(texto1)
print(texto2)
print(texto3)

print()
print('==============================================================================================================')


"""
Módulo Datetime - Em Python há um módulo built-in capaz de lidar com datas e horas.
O módulo datetime fornece classes para manipular datas e horas. Uma vez que esse módulo possui classes,
então a sintaxe para acessar os métodos deve ser algo similar a: modulo.classe.metodo().
"""

import datetime as dt

# Operações com data e hora
hoje = dt.datetime.today()
print(hoje)
ontem = hoje - dt.timedelta(days=1)
print(ontem)
uma_semana_atras = hoje - dt.timedelta(weeks=1)
print(uma_semana_atras)
agora = dt.datetime.now()
print(agora)
duas_horas_atras = agora - dt.timedelta(hours=2)
print(duas_horas_atras)

# Formatação

hoje_formatado = dt.datetime.strftime(hoje, "%d-%m-%Y")
print(hoje_formatado)

#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

ontem_formatado = dt.datetime.strftime(ontem, "%d de %B de %Y")
print(ontem_formatado)

# Converção de string para data

data_string = '11/06/2019 15:30'
print(data_string)
data_dt = dt.datetime.strptime(data_string, "%d/%m/%Y %H:%M")
print(data_dt)

# Módulos de terceiros
"""
Para utilizar uma biblioteca do repositório PyPI, é preciso instalá-la.
Para isso, abra um terminal no sistema operacional e digite:
pip install biblioteca [biblioteca é o nome do pacote que deseja instalar. Por exemplo: pip install numpy.]
"""

# Bibliotecas para tratamento de imagens
"""
* Pillow: esta biblioteca oferece amplo suporte aos formatos de arquivo,
uma representação interna eficiente e recursos de processamento de imagem bastante poderosos.
* OpenCV Python: é uma biblioteca de código aberto licenciada por BSD que inclui várias
centenas de algoritmos de visão computacional.
* Luminoth: é um kit de ferramentas de código aberto para visão computacional.
Atualmente, atua com a detecção de objetos, mas a ideia é expandi-la.
* Mahotas: é uma biblioteca de algoritmos rápidos de visão computacional
(todos implementados em C++ para ganhar velocidade) que opera com matrizes NumPy.
"""

# Bibliotecas para visualização de dados
"""
* Matplotlib: é uma biblioteca abrangente para criar visualizações estáticas, animadas e interativas em Python.
* Bokeh: é uma biblioteca de visualização interativa para navegadores modernos. 
Oferece interatividade de alto desempenho em conjuntos de dados grandes ou de streaming.
* Seaborn: é uma biblioteca para criar gráficos estatísticos em Python.
* Altair: é uma biblioteca declarativa de visualização estatística para Python.
"""

# Bibliotecas para tratamento de dados
"""
* Pandas: é um pacote Python que fornece estruturas de dados rápidas, flexíveis e expressivas,
projetadas para facilitar o trabalho com dados estruturados (em forma de tabela).
* NumPy: além de seus óbvios usos científicos, a NumPy também pode ser usada como um eficiente recipiente
multidimensional de dados genéricos.
* Pyspark: Spark é um sistema de computação em cluster rápido e geral para Big Data.
* Pingouin: é um pacote estatístico Python baseado em Pandas.
"""

# Bibliotecas para tratamento de textos
"""
* Punctuation: esta é uma biblioteca Python que removerá toda a pontuação em uma string.
* NLTK: o Natural Language Toolkit é um pacote Python para processamento de linguagem natural.
* FlashText: este módulo pode ser usado para substituir palavras-chave em frases ou extraí-las.
* TextBlob: é uma biblioteca Python para processamento de dados textuais.
"""

# Internet, rede e cloud
"""
* Requests: permite que você envie solicitações HTTP/1.1 com extrema facilidade.
Não há necessidade de adicionar manualmente queries de consulta aos seus URLs ou de codificar os dados PUT e POST:
basta usar o método JSON.
* BeautifulSoup: é uma biblioteca que facilita a captura de informações de páginas da web.
* Paramiko: é uma biblioteca para fazer conexões SSH2 (cliente ou servidor).
A ênfase está no uso do SSH2 como uma alternativa ao SSL para fazer conexões seguras entre scripts Python.
* s3fs: é uma interface de arquivos Python para S3 (Amazon Simple Storage Service).
"""

# Bibliotecas para acesso a bancos de dados
"""
* mysql-connector-python: permite que programas em Python acessem bancos de dados MySQL.
* cx-Oracle: permite que programas em Python acessem bancos de dados Oracle.
* psycopg2: permite que programas em Python acessem bancos de dados PostgreSQL.
* SQLAlchemy: fornece um conjunto completo de padrões de persistência,
projetados para acesso eficiente e de alto desempenho a diversos banco de dados,
adaptado para uma linguagem de domínio simples e Python.
"""

# Deep learning - Machine learning
"""
* Keras: é uma biblioteca de rede neural profunda de código aberto.
* TensorFlow: é uma plataforma de código aberto de ponta a ponta para aprendizado de máquina,
desenvolvido originalmente pela Google.
* PyTorch: é um pacote Python que fornece dois recursos de alto nível:
i) computação de tensor (como NumPy) com forte aceleração de GPU; e ii) redes neurais profundas.
* Scikit Learn: módulo Python para aprendizado de máquina construído sobre o SciPy
(SciPy é um software de código aberto para matemática, ciências e engenharia).
"""

# Biblioteca para jogos - PyGame
"""
PyGame: é uma biblioteca para a construção de aplicações gráficas e aplicação multimídia,
utilizada para desenvolver jogos.
"""