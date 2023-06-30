"""
Dado um valor em uma lista ordenada, à direita desse número existem somente números maiores que ele;
e à esquerda, somente os menores. Esse valor, chamado de pivô, é a estratégia central no algoritmo quicksort.
O algoritmo quicksort também trabalha com a estratégia de dividir para conquistar, pois, a partir do pivô,
quebrará uma lista em sublistas (direita e esquerda) – a cada escolha do pivô e a cada quebra da lista,
o processo de ordenação vai acontecendo.

A lógica é a seguinte:

primeira iteração: a lista original será quebrada através de um valor chamado de pivô.
Após a quebra, os valores que são menores que o pivô devem ficar à sua esquerda e os maiores à sua direita.
O pivô é inserido no local adequado, trocando a posição com o valor atual.
segunda iteração: agora há duas listas, a da direita e a da esquerda do pivô.
Novamente são escolhidos dois novos pivôs e é feito o mesmo processo,
de colocar à direita os menores e à esquerda os maiores. Ao final os novos pivôs ocupam suas posições corretas.
terceira iteração: olhando para as duas novas sublistas (direita e esquerda),
repete-se o processo de escolha dos pivôs e separação.
na última iteração, a lista estará ordenada, como resultado dos passos anteriores.
para nosso exemplo e implementação, vamos escolher o pivô como sempre o último valor da lista e das sublistas.
"""

print('In [8]: ')

def executar_quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quicksort(lista, inicio, pivo-1)
        executar_quicksort(lista, pivo+1, fim)
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

lista = [10, 9, 5, 8, 11, -1, 3]
print(executar_quicksort(lista, inicio=0, fim=len(lista)-1))

print()
print('==============================================================================================================')


"""
Para ajudar na compreensão do quicksort, veja esta outra implementação do algoritmo,
na qual usamos list comprehensions para criar uma lista de pivôs (agora o pivô é o primeiro valor da lista),
uma lista com os valores menores e uma com os valores maiores.
Esse processo é chamado recursivamente até que a lista esteja ordenada.
"""

print("In [2]: ")

def executar_quicksort_2(lista):
    if len(lista) <= 1: return lista
    pivo = lista[0]
    iguais = [valor for valor in lista if valor == pivo]
    menores = [valor for valor in lista if valor < pivo]
    maiores = [valor for valor in lista if valor > pivo]
    return executar_quicksort_2(menores) + iguais + executar_quicksort_2(maiores)

lista = [10, 9, 5, 8, 11, -1, 3]
print(executar_quicksort_2(lista))