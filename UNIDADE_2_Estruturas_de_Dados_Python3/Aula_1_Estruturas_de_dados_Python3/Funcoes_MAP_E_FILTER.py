"""
A função map() é utilizada para aplicar uma determinada função em cada item de um objeto iterável.
Para que essa transformação seja feita, a função map() exige que sejam passados dois parâmetros:
a função e o objeto iterável.
"""

print('In[13]')

# Exemplo 1
print("Exemplo 1")

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
nova_lista = map(lambda x: x.lower(), linguagens)

print(f"A nova lista é = {nova_lista}\n")

nova_lista = list(nova_lista)

print(f"Agora sim, a nova lista é = {nova_lista}")

# Exemplo 2
print("\n\nExemplo 2")

numeros = [0, 1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x * x, numeros))

print(f"Lista com o número elevado a ele mesmo = {quadrados}\n")

print()
print('==============================================================================================================')

"""
A função filter() tem as mesmas características da função map(), mas, 
em vez de usarmos uma função para transformar os valores da lista, nós a usamos para filtrar.
"""

print('In[14]')
numeros = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)