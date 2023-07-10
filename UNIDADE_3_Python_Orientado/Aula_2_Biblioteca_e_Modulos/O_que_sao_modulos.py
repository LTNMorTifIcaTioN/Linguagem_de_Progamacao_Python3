"""
* Um módulo pode ser uma biblioteca de códigos, o qual possui diversas funções (matemáticas, sistema operacional, etc.)
as quais possibilitam a reutilização de código de uma forma elegante e eficiente.

* Um módulo é um arquivo contendo definições e instruções Python.
O nome do arquivo é o nome do módulo acrescido do sufixo .py.

* Um módulo pode ser uma biblioteca de códigos

Como utilizar um módulo - Para utilizar um módulo é preciso importá-lo para o arquivo.
Essa importação pode ser feita de maneiras distintas:
1. import moduloXXText
1.2  import moduloXX as apelido
2. from moduloXX import itemA, itemB
"""

print('In [1]:')
import math

print(math.sqrt(25))
print(math.log2(1024))
print(math.cos(45))
print()

print('In [2]:')
import math as m

print(m.sqrt(25))
print(m.log2(1024))
print(m.cos(45))
print()

print('In [3]:')
from math import sqrt, log2, cos

print(sqrt(25))
print(log2(1024))
print(cos(45))

