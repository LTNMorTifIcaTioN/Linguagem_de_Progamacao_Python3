"""
O algoritmo selection sort recebe esse nome,
porque faz a ordenação sempre escolhendo o menor valor para ocupar uma determinada posição.
A lógica do algoritmo é a seguinte:

iteração 1: percorre toda a lista, procurando o menor valor para ocupar a posição 0.
iteração 2: a partir da posição 1, percorre toda a lista, procurando o menor valor para ocupar a posição 1.
iteração 3: a partir da posição 2, percorre toda a lista, procurando o menor valor para ocupar a posição 2.
esse processo é repetido N-1 vezes, sendo N o tamanho da lista.
"""

print('In4')

def executar_selection_sort(lista):
    n = len(lista)
    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
print(executar_selection_sort(lista))

print()
print('==============================================================================================================')


"""
Nessa versão do selection sort, na qual criamos uma lista vazia e, dentro de uma estrutura de repetição,
usamos a função built-in min() para, a cada iteração,
encontrar o menor valor da sequência e adicioná-lo na lista_ordenada.
"""

print('In[2]')

def executar_selection_sort_2(lista):
    lista_ordenada = []
    while lista:
        minimo = min(lista)
        lista_ordenada.append(minimo)
        lista.remove(minimo)
    return lista_ordenada

lista = [10, 9, 5, 8, 11, -1, 3]
print(executar_selection_sort_2(lista))
