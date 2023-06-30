"""
Os objetos do tipo sequência são estruturas de dados capazes de armazenar mais de um valor.
Essas estruturas de dados representam sequências finitas indexadas por números não negativos.
O primeiro elemento de uma sequência ocupa o índice 0; o segundo, 1; o último elemento, a posição n - 1,
em que n é capacidade de armazenamento da sequência.
"""
# Sequência de Caracteres
print('In[1]')
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")

print()
print('==============================================================================================================')

print('In[2]')
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(texto.upper())
print(texto.replace("i", 'XX'))

print()
print('==============================================================================================================')

print('In[3]')

texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()

print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")

print()
print('==============================================================================================================')

print('In[4]')

texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor 
(Perkovic, p. 23, 2016).
"""

print(f"Tamanho do texto = {len(texto)}")

texto = texto.lower()
# função lower() a essa string para que tod_o o texto fique com letras minúsculas.
texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")
# função replace(), que age substituindo o primeiro parâmetro pelo segundo.
lista_palavras = texto.split()
# função split(), sempre que houver um espaço em branco, a string será cortada, criando um novo elemento na lista.

print(f"Tamanho da lista de palavras = {len(lista_palavras)}")

total = lista_palavras.count("string") + lista_palavras.count("strings")
# função count() para contar tanto a palavra "string" no singular quanto o seu plural "strings".

print(f"Quantidade de vezes que string ou strings aparecem = {total}")

print()
print('==============================================================================================================')


