"""
A primeira grande diferença entre o algoritmo de busca linear e o algoritmo de busca binária é que, com este último,
os valores precisam estar ordenados. A lógica é a seguinte:

Encontra o item no meio da sequência (meio da lista).
Se o valor procurado for igual ao item do meio, a busca se encerra.
Se não for, verifica-se se o valor buscado é maior ou menor que o valor central.
Se for maior, então a busca acontecerá na metade superior da sequência (a inferior é descartada); se não for, a busca acontecerá na metade inferior da sequência (a superior é descartada).

A busca binária possui complexidade O(log2 N).

Em Stephens (2013, p. 219), podemos encontrar o seguinte pseudocódigo para a busca binária:

Integer: BinarySearch(Data values[], Data target)

    Integer: min = 0

    Integer: max = - 1

    While (min <= max)

      // Find the dividing item.

      Integer: mid = (min + max) / 2

      // See if we need to search the left or right half.

      If (target < values[mid]) Then max = mid - 1

        Else If (target > values[mid]) Then min = mid + 1

      Else Return mid

    End While

    // If we get here, the target is not in the array.

    Return -1

  End BinarySearch
"""

print('In[7]')

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        # Verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True  # Se o valor for encontrado para aqui
    return False  # Se chegar até aqui, significa que o valor não foi encontrado

# In[8]:

lista = list(range(1, 50))
print(lista)
print('\n', executar_busca_binaria(lista=lista, valor=10))
print('\n', executar_busca_binaria(lista=lista, valor=200))

print()
print('==============================================================================================================')


"""
Como podemos alterar nossa função para que, en vez de retornar True ou False,
retorne a posição que o valor ocupa da sequência? A lógica é a mesma. No entanto,
agora vamos retornar a variável "meio", já que esta, se o valor for encontrado, será a posição.
"""

print('In[9]')

def procurar_valor(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return meio
    return None

# In[10]

vogais = ['a', 'e', 'i', 'o', 'u']
resultado = procurar_valor(lista=vogais, valor='u')

if resultado:
    print(f"Valor encontrado an posição {resultado}")
else:
    print("Valor não encontrado")