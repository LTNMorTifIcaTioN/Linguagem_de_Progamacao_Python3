"""
print(), para imprimir um valor na tela.
enumerate(), para retornar a posição de um valor em uma sequência.
input(), para capturar um valor digitado no teclado.
int() e float(), para converter um valor no tipo inteiro ou float.
range(), para criar uma sequência numérica.
type(), para saber qual o tipo de um objeto (variável).
https://docs.python.org/3/library/functions.html
"""

# In[1]
a = 2
b = 1
equacao = input("Digite a fórmula geral da equação linear (a * x + b): ")
print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")
for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")

"""
A função eval() usada no código recebe como entrada uma string (sequência de caracteres) digitada pelo usuário, 
que nesse caso é uma equação linear. Essa entrada é analisada e avaliada como uma expressão Python pela função eval(). 
Veja que, para cada valor de x, a fórmula é executada como uma expressão matemática (linha 8) e 
retorna um valor diferente.
"""