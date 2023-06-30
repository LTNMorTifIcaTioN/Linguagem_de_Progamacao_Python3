"""
Dedup é a abreviação para deduplicação de dados, que consiste em eliminar registros duplicados dos dados.
"""

print('In[1]')

nomes = 'João Marcela Sonia Daryl Vernon Eder Mechelle Edan Igor Ethan Reed Travis Hoyt'.split()

print('Marcela' in nomes)
print('Roberto' in nomes)

print()
print('==============================================================================================================')


"""
Uma pesquisa linear examina todos os elementos da sequência até encontrar o de destino.
Para implementar a busca linear, vamos precisar de uma estrutura de repetição (for) para percorrer a sequência,
e uma estrutura de decisão (if) para verificar se o valor em uma determinada posição é o que procuramos.
"""

print('In[2]')

def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False

#In[3]

import random

lista = random.sample(range(1000), 50)
# por meio da biblioteca random criamos uma lista de 50 números inteiros randômicos que variam entre 0 e 1000;
print(sorted(lista))
print(executar_busca_linear(lista, 10))

print()
print('==============================================================================================================')

"""
Em Python, as estruturas de dados do tipo sequência possuem a função index(), que é usada da seguinte forma:
sequencia.index(valor). 
A função index() espera como parâmetro o valor a ser procurado na sequência. 
"""

print('In [4]')

vogais = 'aeiou'
resultado = vogais.index('e')
print(resultado)


print()
print('==============================================================================================================')


"""
Dada uma lista numérica, somente podem ser localizados valores do mesmo tipo. O mesmo para uma sequência de caracteres,
que só pode localizar letras, palavras ou ainda uma string vazia.
O tipo None não pode ser localizado em nenhuma lista – se tentar passar como parâmetro, poderá receber um erro
"""

print('In[5]')

def procurar_valor(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return i
    return None

#In[6]

vogais = 'aeiou'
resultado = procurar_valor(lista=vogais, valor='a')

if resultado != None:
    print(f"Valor encontrado na posição {resultado}")
else:
    print("Valor não encontrado")