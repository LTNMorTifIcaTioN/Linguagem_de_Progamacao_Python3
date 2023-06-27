"""
Lista é uma estrutura de dados do tipo sequencial que possui como principal característica ser mutável.
Ou seja, novos valores podem ser adicionados ou removidos da sequência. Em Python,
as listas podem ser construídas de várias maneiras:
usando um par de colchetes para denotar uma lista vazia: lista1 = []
usando um par de colchetes e elementos separados por vírgulas: lista2 = ['a', 'b', 'c']
usando uma "list comprehension": [x for x in iterable]
usando o construtor de tipo: list()
"""

print('In [5]')

vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas

for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')

print()
print('==============================================================================================================')


print('In [6]')
# Mesmo resultado.

vogais = []

print(f"Tipo do objeto vogais = {type(vogais)}")

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

print()
print('==============================================================================================================')


print('In [7]')

frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

print("maça" in frutas) # True
print("abacate" in frutas) # False
print("abacate" not in frutas) # True
print(min(frutas)) # banana
print(max(notas)) # 10
print(frutas.count("maça")) # 2
print(frutas + notas)
print(2 * frutas)

print()
print('==============================================================================================================')

print('In[8]')

lista = ['Python', 30.61, "Java", 51, ['a', 'b', 20], "maça"]

print(f"Tamanho da lista = {len(lista)}")

for i, item in enumerate(lista):
    print(f"Posição = {i},\t valor = {item} -----------------> tipo individual = {type(item)}")
print("\nExemplos de slices:\n")
print("lista[1] = ", lista[1])
print("lista[0:2] = ", lista[0:2])
print("lista[:2] = ", lista[:2])
print("lista[3:5] = ", lista[3:5])
print("lista[3:6] = ", lista[3:6])
print("lista[3:] = ", lista[3:])
print("lista[-2] = ", lista[-2])
print("lista[-1] = ", lista[-1])
print("lista[4][1] = ", lista[4][1])

print()
print('==============================================================================================================')


