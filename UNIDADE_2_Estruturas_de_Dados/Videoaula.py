#   E   S   T   R   U   R   A   S      D   E      D   A   D   O   S

# Listas em Python
"""
* Sequencial composto por elementos organizados de modo linear;
* Os elementos podem ser acessados a partir de um índice que representa sua posição na coleção, iniciando em zero;
'lista = []'
append(): adiciona um elemento no final da lista;
insert(x,y): adiciona o elemento y na posição x;
remove(y): remove y da lista;
sort() - ordena por valor;
extend(lista) - concatenar com outra lista;
index(elemento) - descobrir a posição de um elemento;
clear() - apagar todos os elementos da lista;
"""

# Fatiamento de listas
"""
>>> L = [1, 3, 5, 7, 9, 77, 13, 15, 17, 19, 21, 23]
>>> L[0:3]
[1, 3, 5]
>>> L[:5]
[1, 3, 5, 7, 9]
>>> L[0:8:3]
[1, 7, 13]
"""

# List Comprehension
"""
Uma construção sintática para criação de uma lista baseada em listas existentes.
[expr for item in lista if cond]
>>> S = [x*2 for x in range(0,10) if x % 2 == 0]
>>> print S
[0, 4, 8, 12, 16]
"""

# Tuplas()
"""
* Semelhante a lista, porém, imutável;
* São capazes de conter quaisquer outros tipos definidos em Python;
* Acesso aos elementos de fá por meio de índices;
* Comumente os elementos são definidos entre parênteses;
Aceitam os operadores de concatenação '+' e multiplicativo '*' e aplicam-se a elas as operações de fatiamento.
"""

# Dicionários
"""
Dicionários: também conhecido como mapa, uma coleção de elementos, do qual temos N entradas associadas a uma ou mais
chaves por entrada.
{<chave 1>:<valor 1>, <chave 2>:<valor 2>, ..., <chave i>:<valor i>}
"""

# Criação de matrizes com NumPy
"""
NumPy: um pacote de extensão do Pyhton para matrizes multi-dimensionais;

import numpy as no
X=np.array([
            [0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
                    ])
"""

# Desafio 1 - Cálculo de Média

"""def ValorLista():
    for i in range(1, 5):
        lista.append(int(input(f'Digite o valor da sua prova{i}: ')))

def Media():
    s=0
    for i in range(len(lista)):
        s = s + lista[i]
    m = s/4
    return m

lista = []
ValorLista()
m = Media()
print(m)"""


#   A   L   G   O   R   I   T   M   O   S      D   E      B   U   S   C   A

# Busca Sequencial
"""
* É o algoritmo mais simples de busca;
    > Percorrer toda a coleção comparando a chave com o valor do elemento em cada posição;
    > No caso, se a chave for igual a algum valor, retorna a posição correspondente na coleção.
    > Caso não exista a chave na estrutura percorrida, então retorne o valor -1
"""

# Busca Binária
"""
* Eficiente para uma estrutura de dados ordenada.
    > O elemento é comparado com o elemento do meio do arranjo, se igual, retorna o valor;
    > Se menor, realiza a busca na metade inferior do arranjo;
    > Se maior, realiza a busca na metade superior do arranjo;
"""

"""def BuscaSeq(list, item):
    pos=0
    x=False
    while pos<len(list) and not x:
        if list[pos]==item:
            x=True
        else:
            pos = pos +1
    return x


lista = [1, 3, 5, 7, 9, 77, 13, 15, 17, 19, 21, 23]
print(BuscaSeq(lista, 9))
print(BuscaSeq(lista, 12))"""

# Desafio 2 - Busca Binária

"""def BuscaBin(list, item):
    prim = 0
    ult = len(list) - 1
    found = False
    while prim <= ult and not found:
        meio = (prim + ult) // 2
        if list[meio] == item:
            found = True
        else:
            if item < list[meio]:
                ult = meio - 1
            else:
                prim = meio + 1
    return found

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
print(BuscaBin(lista, 2))
print(BuscaBin(lista, 13))
"""

#   A   L   G   O   R   I   T   M   O   S      D   E      O   R   D   E   N   A   Ç   Ã   O

# Ordenação
"""
Dado uma sequência arbitrária com n (>= 0) elementos, o objetivo da ordenação é produzir uma nova sequência em que os
elementos aparecem em ordem.
* Para ordenar determinado domínio de dados, deve-se existir relação entre os elementos: >, = ou >;
"""

# Bubble Sort
"""
Percorre o vetor várias vazes, a cada passagem faz a troca para o topo o maior/menor elemento da sequência.
O = n^2


def bubbleSort(list):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                print(list)

lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(lista)
print(lista)
"""

# Selection Sort
"""
Este algoritmo seleciona em cada iteração um elemento para ser inserido na sequência ordenada produzida.
O = N^2
"""

# Insertion Sort
"""
O Insertion Sort ordena os elementos inserindo-os na posição correta. Os elementos são divididos em duas regiões,
ordenados e ainda não ordenados.
"""

# MergeSort
"""
Utiliza estratégia de divisão e conquista;
* Divide recursivamente a sequência ao meio;
* Ao chegar a uma subsequência unitária, esta encontra-se ordenada;
* A partir desse ponto, intercale gradativamente subsequências ordenadas,
gerando subsequências ordenadas de maior tamanho;
* Termine ao intercalar a sequência original;
O = N*log(N)
"""

# QuickSort
"""
* Estratégia de divisão e conquista;
* Escolha de um elemento: Pivô;
* Rearranja a lista, aonde todos os elementos anteriores ao pivô sejam menores e os elementos posteriores ao pivô
sejam maiores;
* Recursivamente ordena as sequencias esquerda e direita do pivô;

def executar_quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quicksort(lista, inicio, pivo - 1)
        executar_quicksort(lista, pivo + 1, fim)
    return lista


def executar_particao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
    lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
    return esquerda

lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
executar_quicksort(lista, 0, len(lista)-1)
print(lista)
"""

# Desafio 3 - Dicionário
"""aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'

for x, y in aluno.items():
    print(f'-{x} ´é igual a {y}')

print(aluno.keys())
print(aluno.values())"""

numeros = [2, 3]
print(map(lambda x: 2 x, numeros))