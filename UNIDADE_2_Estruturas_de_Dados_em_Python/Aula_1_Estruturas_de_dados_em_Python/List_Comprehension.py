"""
A listcomp, é uma forma pythônica de criar uma lista com base em um objeto iterável.
Esse tipo de técnica é utilizada quando, dada uma sequência, deseja-se criar uma nova sequência,
porém com as informações originais transformadas ou filtradas por um critério.
"""

print('In[9]')
linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
# linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # Essa sintaxe produz o mesmo resultado que a linha 1

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)

"""
A listcomp é uma forma pythônica de escrever um for.
O código da entrada 9 poderia ser escrito conforme mostrado a seguir, e o resultado é o mesmo:

In [10]
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
print("Antes da listcomp = ", linguagens)

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()

print("\nDepois da listcomp = ", linguagens)
"""

print()
print('==============================================================================================================')


"""
Usar a listcomp para construir uma lista que contém somente as linguagens que possuem "Java" no texto:
"""

print('In[11]')

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_java = [item for item in linguagens if "Java" in item]

print(linguagens_java)

"""
A listcomp da entrada 11 poderia ser escrita conforme o código a seguir. 
Veja que precisaríamos digitar muito mais instruções:

In [12]
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_java = []

for item in linguagens:
    if "Java" in item:
        linguagens_java.append(item)

print(linguagens_java)
"""
