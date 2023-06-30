"""
O algoritmo merge sort recebe esse nome porque faz a ordenação em duas etapa: (i) divide a lista em sublistas;
e (ii) junta (merge) as sublistas já ordenadas.

O paradigma de dividir e conquistar envolve três etapas em cada nível da recursão:
(i) dividir o problema em vários subproblemas;
(ii) conquistar os subproblemas, resolvendo-os recursivamente – se os tamanhos dos subproblemas forem pequenos
o suficiente, apenas resolva os subproblemas de maneira direta;
(iii) combine as soluções dos subproblemas na solução do problema original.
Etapa de divisão:
com base na lista original, encontre o meio e separe-a em duas listas: esquerda_1 e direita_2.
com base na sublista esquerda_1, se a quantidade de elementos for maior que 1,
encontre o meio e separe-a em duas listas: esquerda_1_1 e direta_1_1.
com base na sublista esquerda_1_1, se a quantidade de elementos for maior que 1,
encontre o meio e separe-a em duas listas: esquerda_1_2 e direta_1_2.
repita o processo até encontrar uma lista com tamanho 1.
chame a etapa de merge.
repita o processo para todas as sublistas.

Etapa de merge:
dadas duas listas, cada uma das quais contém 1 valor – para ordenar, basta comparar esses valores e fazer a troca,
gerando uma sublista com dois valores ordenados.
dadas duas listas, cada uma das quais contém 2 valores – para ordenar,
basta ir escolhendo o menor valor em cada uma e gerar uma sublista com quatro valores ordenados.
repita o processo de comparação e junção dos valores até chegar à lista original, agora ordenada.
"""

print('In [7]:')

def executar_merge_sort(lista):
    if len(lista) <= 1: return lista
    else:
        meio = len(lista) // 2
        esquerda = executar_merge_sort(lista[:meio])
        direita = executar_merge_sort(lista[meio:])
        return executar_merge(esquerda, direita)

def executar_merge(esquerda, direita):
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0,0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    return sub_lista_ordenada

lista = [10, 9, 5, 8, 11, -1, 3]
print(executar_merge_sort(lista))