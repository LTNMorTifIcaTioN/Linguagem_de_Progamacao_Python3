"""
O algoritmo insertion sort (algoritmo de inserção) recebe esse nome porque faz a ordenação pela simulação da inserção
de novos valores na lista. Para entendermos como funciona o algoritmo,
imagine um jogo de cartas para a execução do qual cada jogador começa com cinco cartas e, a cada rodada,
deve pegar e inserir uma nova carta na mão.

início: parte-se do princípio de que a lista possui um único valor e, consequentemente, está ordenada.
iteração 1: parte-se do princípio de que um novo valor precisa ser inserido na lista; nesse caso,
ele é comparado com o valor já existente para saber se precisa ser feita uma troca de posição.
iteração 2: parte-se do princípio de que um novo valor precisa ser inserido na lista; nesse caso,
ele é comparado com os valores já existentes para saber se precisam ser feitas trocas de posição.
iteração N: parte-se do princípio de que um novo valor precisa ser inserido na lista; nesse caso,
ele é comparado com todos os valores já existentes (desde o início) para saber se precisam ser feitas trocas de posição.
"""

print('In [6]')

def executar_insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor_inserir = lista[i]
        j = i - 1

        while j>= 0 and lista [j] > valor_inserir:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_inserir
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
print(executar_insertion_sort(lista))