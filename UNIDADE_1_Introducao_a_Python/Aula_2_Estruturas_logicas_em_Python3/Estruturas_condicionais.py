"""
O código apresentado na entrada 1(In [1]) refere-se a uma estrutura condicional simples,
pois só existem ações caso a condição seja verdadeira.
"""

# In[1]
a = 5
b = 10
if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)
print()
print('===========================================================================================================')

"""
O código apresentado na entrada 2(In [2]) refere-se a uma estrutura condicional composta,
pois existem ações tanto para a condição verdadeira quanto para a falsa.
"""

# In[2]
a = 10
b = 5
if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)
else:
    print("a é maior do que b")
    r = a - b
    print(r)
print()
print('===========================================================================================================')

"""
Além das estruturas simples e compostas, existem as estruturas encadeadas. 
Em diversas linguagens como C, Java, C#, C++, etc, essa estrutura é construída como o comando switch..case. 
Em Python, não existe o comando switch . Para construir uma estrutura encadeada, devemos usar o comando "elif", 
que é uma abreviação de else if.
"""

# In [3]
codigo_compra = 5111
if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado")