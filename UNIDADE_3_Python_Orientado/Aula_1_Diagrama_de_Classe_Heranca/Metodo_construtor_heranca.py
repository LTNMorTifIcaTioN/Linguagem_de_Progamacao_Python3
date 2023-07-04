"""
Na herança, quando adicionamos a função __init__(), a classe-filho não herdará o construtor dos pais.
Ou seja, o construtor da classe-filho sobrescreve (override) o da classe-pai.
Para utilizar o construtor da classe-base, é necessário invocá-lo explicitamente, dentro do construtor-filho,
da seguinte forma: ClassePai.__init__().
"""

# In [13]
class int42(int):
    def __init__(self, n):
        int.__init__(n)

    def __add__(a, b):
        return 42

    def __str__(n):
        return '42'

print('In [14]')
a = int42(7)
b = int42(13)
print(a + b)
print(a)
print(b)
print()

print('In [15]')
c = int(7)
d = int(13)
print(c + d)
print(c)
print(d)