"""
Em Python, as tuplas (objetos imutáveis) podem ser construídas de três maneiras:

usando um par de parênteses para denotar uma tupla vazia: tupla1 = ()
usando um par de parênteses e elementos separados por vírgulas: tupla2 = ('a', 'b', 'c')
usando o construtor de tipo: tuple()
"""
print('In[15]')

vogais = ('a', 'e', 'i', 'o', 'u')

print(f"Tipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

print()
print('==============================================================================================================')


print('In[17]')

vogais = ('a', 'e', 'i', 'o', 'u')

for item in enumerate(vogais):
    print(item)

print()
print(tuple(enumerate(vogais)))
print()
print(list(enumerate(vogais)))