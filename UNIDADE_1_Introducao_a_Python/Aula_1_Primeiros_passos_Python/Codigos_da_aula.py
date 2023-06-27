# IN[2]:
x = 10
nome = 'aluno'
nota = 8.75
fez_inscricao = True
print()
print('===========================================================================================================')


# IN[3]:
print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))
print()
print('===========================================================================================================')


# IN[4]:
nome = input("Digite um nome: ")
print(nome)
print()
print('===========================================================================================================')


# IN[5]: Modo 1 - usando formatadores de caracteres (igual na linguagem C) para imprimir variável e texto
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world" % (nome))
print()
print('===========================================================================================================')


# IN[6]: Modo 2 - usando a função format() para imprimir variável e texto
print("Olá {}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world".format(nome))
print()
print('===========================================================================================================')


# IN[7]: Modo 3 - usando strings formatadas
print(f"Olá {nome}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world")
print()
print('===========================================================================================================')


# IN[8]: Qual o resultado armazendo na variável operacao_1: 25 ou 17?
operacao_1 = 2 + 3 * 5
# Qual o resultado armazendo na variável operacao_2: 25 ou 17?
operacao_2 = (2 + 3) * 5
# Qual o resultado armazendo na variável operacao_3: 4 ou 1?
operacao_3 = 4 / 2 ** 2
# Qual o resultado armazendo na variável operacao_4: 1 ou 5?
operacao_4 = 13 % 3 + 4

print(f"Resultado em operacao_1 = {operacao_1}")
print(f"Resultado em operacao_2 = {operacao_2}")
print(f"Resultado em operacao_3 = {operacao_3}")
print(f"Resultado em operacao_4 = {operacao_4}")
