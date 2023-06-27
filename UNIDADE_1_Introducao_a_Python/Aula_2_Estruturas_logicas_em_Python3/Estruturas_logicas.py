"""
No exemplo da entrada 4 (In [4]), fizemos a conversão do tipo string para numérico, encadeando funções.
Como já sabemos, primeiro são resolvidos os parênteses mais internos, ou seja, na linha 1,
será feita primeiro a função input(), em seguida, a entrada digitada será convertida para inteira com a função int().
A mesma lógica se aplica na linha 2, na qual a entrada é convertida para ponto flutuante.
Na linha 4 fizemos o teste condicional, primeiro são resolvidos os operadores relacionais, em seguida, os lógicos.
"""

# In [4]

qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))
if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
print()
print('===========================================================================================================')


"""
Na entrada 5 (In [5]), temos os seguintes casos:
Linha 5: True or False and False. Nesse caso será feito primeiro o and, que resulta em False, 
mas em seguida é feito o or, que então resulta em verdadeiro.
Linha 6: (True or False) and False. Nesse caso será feito primeiro o or, que resulta em True, 
mas em seguida é feito o and, que então resulta em falso, pois ambos teriam que ser verdadeiro para o and ser True.
"""

# In [5]
A = 15
B = 9
C = 9

print(B == C or A < B and A < C)
print((B == C or A < B) and A < C)
