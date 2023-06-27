"""Podemos construir dicionários em Python das seguintes maneiras:

usando um par de chaves para denotar um dict vazio: dicionario1 = {}
usando um par de elementos na forma, chave:valor separados por vírgulas: dicionario2 = {'one': 1, 'two': 2, 'three': 3}
usando o construtor de tipo: dict()"""

print('In[20]')

# Exemplo 1 - Criação de dicionário vazio, com atribuição posterior de chave e valor

dici_1 = {}
dici_1['nome'] = "João"
dici_1['idade'] = 30

# Exemplo 2 - Criação de dicionário usando um par elementos na forma, chave : valor

dici_2 = {'nome': 'João', 'idade': 30}

# Exemplo 3 - Criação de dicionário com uma lista de tuplas. Cada tupla representa um par chave : valor

dici_3 = dict([('nome', "João"), ('idade', 30)])

# Exemplo 4 - Criação de dicionário com a função built-in zip() e duas listas, uma com as chaves, outra com os valores.

dici_4 = dict(zip(['nome', 'idade'], ["João", 30]))

print(dici_1 == dici_2 == dici_3 == dici_4)  # Testando se as diferentes construções resultamo em objetos iguais.

print()
print('==============================================================================================================')


"""
No código a seguir, a função keys() retorna uma lista com todas as chaves de um dicionário. 
A função values() retorna uma lista com todos os valores. A função items() retorna uma lista de tuplas, 
cada uma das quais é um par chave-valor.
"""

print('In[21]')

cadastro = {
    'nome': ['João', 'Ana', 'Pedro', 'Marcela'],
    'cidade': ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
    'idade': [25, 33, 37, 18]
}

print("len(cadastro) = ", len(cadastro))
# a função len() retorna quantas chaves um dicionário possui.
print("\n cadastro.keys() = \n", cadastro.keys())
# cadastro.keys(): retorna uma lista com todas as chaves no dicionário.
print("\n cadastro.values() = \n", cadastro.values())
# cadastro.values(): retorna uma lista com os valores. Como os valores também são listas, temos uma lista de listas.
print("\n cadastro.items() = \n", cadastro.items())
# cadastro.items(): retorna uma lista de tuplas, cada uma das quais é composta pela chave e pelo valor.
print("\n cadastro['nome'] = ", cadastro['nome'])
# cadastro['nome']: acessa o valor atribuído à chave 'nome'; nesse caso, uma lista de nomes.
print("\n cadastro['nome'][2] = ", cadastro['nome'][2])
# cadastro['nome'][2]: acessa o valor na posição 2 da lista atribuída à chave 'nome'.
print("\n cadastro['idade'][2:] = ", cadastro['idade'][2:])
# cadastro['idade'][2:]: acessa os valores da posição 2 até o final da lista atribuída à chave 'nome'.

print()
print('==============================================================================================================')


print('In[22]')

print(len(cadastro['nome']))
print(len(cadastro['cidade']))
print(len(cadastro['idade']))

qtde_itens = sum([len(cadastro[chave]) for chave in cadastro])

print(f"\n\nQuantidade de elementos no dicionário = {qtde_itens}")