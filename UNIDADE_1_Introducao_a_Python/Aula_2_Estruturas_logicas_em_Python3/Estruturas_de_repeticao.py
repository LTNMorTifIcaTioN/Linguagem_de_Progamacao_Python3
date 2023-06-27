"""
Veja a construção do comando while na entrada 6 (In [6]). Na linha 1, criamos uma variável chamada número com valor 1.
Na linha 2 criamos a estrutura de repetição, veja que o comando while possui uma condição:
o número tem que ser diferente de zero para o bloco executar.
Todo o bloco com a indentação de uma tabulação (4 espaços) faz parte da estrutura de repetição.
Lembre: todos os blocos de comandos em Python são controlados pela indentação.
"""

# In [6]
numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")
print()
print('===========================================================================================================')


"""
Na entrada 7 (In [7]) construímos nossa primeira estrutura de repetição com for. Vamos analisar a sintaxe da estrutura. 
Usamos o comando "for" seguido da variável de controle "c", na sequência o comando "in", que traduzindo significa "em", 
por fim, a sequência sobre a qual a estrutura deve iterar. 
Os dois pontos marcam o início do bloco que deve ser repetido.
"""

# In [7]
nome = "Guido"
for c in nome:
    print(c)
print()
print('===========================================================================================================')


# In [8]

nome = "Guido"
for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")
