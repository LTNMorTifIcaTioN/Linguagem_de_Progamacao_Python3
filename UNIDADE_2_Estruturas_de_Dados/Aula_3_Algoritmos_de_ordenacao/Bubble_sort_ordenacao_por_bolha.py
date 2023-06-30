"""
O algoritmo bubble sort (algoritmo da bolha) recebe esse nome porque faz a ordenação sempre a partir do início da lista,
comparando um valor com seu vizinho.

A lógica do algoritmo é a seguinte:

iteração 1: seleciona o valor na posição 0 e o compara com seu vizinho – se for menor, há troca; se não for,
seleciona o próximo e compara, repentindo o processo.
iteração 2: seleciona o valor na posição 0 e compara ele com seu vizinho, se for menor troca,
senão seleciona o próximo e compara, repentindo o processo.
iteração N - 1: seleciona o valor na posição 0 e o compara com seu vizinho – se for menor, há troca;
se não for, seleciona o próximo e compara, repentindo o processo.
"""

print('In[5]')

def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
print(executar_bubble_sort(lista))