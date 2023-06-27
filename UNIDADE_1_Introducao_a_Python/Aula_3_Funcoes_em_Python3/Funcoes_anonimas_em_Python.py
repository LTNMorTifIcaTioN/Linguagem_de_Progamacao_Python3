"""
Expressões lambda (às vezes chamadas de formas lambda) são usadas para criar funções anônimas.
Uma função anônima é uma função que não é construída com o "def" e, por isso, não possui nome.
Esse tipo de construção é útil, quando a função faz somente uma ação e é usada uma única vez.
"""
# In [14]
print((lambda x: x + 1)(x=3))
print()
print('==============================================================================================================')


# In [15]
print((lambda x, y: x + y)(x=3, y=2))
print()
print('==============================================================================================================')


# In [16]
somar = lambda x, y: x + y
print(somar(x=5, y=3))
