"""
Em Python, existem duas formas já programadas que nos permitem ordenar uma sequência:
a função built-in sorted() e o método sort(), presente nos objetos da classe list.

"""

print('In[1]')

lista = [10, 4, 1, 15, -3]
lista_ordenada1 = sorted(lista) # A função built-in sorted() cria uma nova lista para ordenar e a retorna
lista_ordenada2 = lista.sort()  # Por sua vez, o método sort(), da classe list, não cria uma nova lista,
                                # uma vez que faz a ordenação "inplace"

print('lista = ', lista, '\n')
print('lista_ordenada1 = ', lista_ordenada1)
print('lista_ordenada2 = ', lista_ordenada2)
print('lista = ', lista)

print()
print('==============================================================================================================')

print('In[2]')

lista = [7,4]

if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)

print()
print('==============================================================================================================')


print('In[3]')

lista = [5, -1]

if lista[0] > lista[1]:
    lista[0], lista[1] = lista[1], lista[0]

print(lista)

"""
complexidade O(N2): neste grupo estão os algoritmos selection sort, bubble sort e insertion sort.
Esses algoritmos são lentos para ordenação de grandes listas,
porém são mais intuitivos de entender e possuem uma codificação mais simples.
complexidade O(N log N): deste grupo, vamos estudar os algoritmos merge sort e quick sort.
Tais algoritmos possuem performance superior, porém são um pouco mais complexos de serem implementados.
"""