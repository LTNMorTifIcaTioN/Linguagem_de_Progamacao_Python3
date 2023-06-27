"""
Sobre os argumentos que uma função pode receber, para nosso estudo, vamos classificar em seis grupos:

parâmetro posicional, obrigatório, sem valor default (padrão).
parâmetro posicional, obrigatório, com valor default (padrão).
parâmetro nominal, obrigatório, sem valor default (padrão).
parâmetro nominal, obrigatório, com valor default (padrão).
parâmetro posicional e não obrigatório (args).
parâmetro nominal e não obrigatório (kwargs).
"""

# In [7]
def somar(a, b):
    return a + b

print('Digite dois números')
# a = int(input('Primeiro número: '))
# b = int(input('Segundo número: '))
# r = input(somar(a, b))
r = somar(3, 6)
print(r)

print()
print('==============================================================================================================')


"""
A função "calcular_desconto" na entrada 8 (In [8]) foi definida de modo a receber dois parâmetros: "valor" e "desconto".
O parâmetro "valor" não possui valor default, já o parâmetro "desconto" possui zero como valor default, ou seja, 
se a função for invocada e o segundo parâmetro não for passado, será usado o valor padrão definido para o argumento.
"""
# In[8]
def calcular_desconto(valor, desconto=0):  # O parâmetro desconto possui zero valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100)  # Não aplicar nenhum desconto
valor2 = calcular_desconto(100, 0.25)  # Aplicar desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")

print()
print('==============================================================================================================')


#In[9]
def cadastrar_pessoa(nome, idade, cidade):
    print("\nDados a serem cadastrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

cadastrar_pessoa("João", 23, "São Paulo")   # resultado exatamente o que esperávamos
cadastrar_pessoa("São Paulo", "João", 23)   # erro lógico, pois os dados não foram atribuídos às variáveis corretas

print()
print('==============================================================================================================')


# In [10]
def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()

texto = converter_maiuscula(flag_maiuscula=True, texto="João") # Passagem nominal de parâmetros
print(texto)

print()
print('==============================================================================================================')


#In[11]
def converter_minuscula(texto, flag_minuscula=True):  # O parâmetro flag_minuscula possui True como valor default
    if flag_minuscula:
        return texto.lower()
    else:
        return texto.upper()

texto1 = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de Programação")
print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")

print()
print('==============================================================================================================')


"""
Existem casos em que esses parâmetros podem ser arbitrários, ou seja,
a função poderá receber um número diferente de parâmetros a cada invocação. 
Esse cenário é o que carateriza os grupos 5 e 6 de funções que vamos estudar.
No grupo 5, temos parâmetros posicionais indefinidos, ou seja, a passagem de valores é feita de modo posicial, 
porém a quantidade não é conhecida. Observe a função "obter_parametros" a seguir.
"""
# In[12]
def imprimir_parametros(*args): # A função "imprimir_parametros" na entrada 12 (In [12]) foi definida de modo a obter
                                # parâmetros arbitrários. Tal construção é feita, passando como parâmetro o *args.
                                # O parâmetro não precisa ser chamado de args, mas é uma boa prática.
                                # Já o asterisco antes do parâmetro é obrigatório.
    qtde_parametros = len(args) # usamos a função built-in len() (length)
                                # para saber a quantidade de parâmetros que foram passados.
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros("São Paulo", 10, 23.78, "João")
print("\nChamada 2")
imprimir_parametros(10, "São Paulo")

print()
print('==============================================================================================================')


# In[13]
def imprimir_parametros(**kwargs):  # A função "imprimir_parametros" na entrada 13 (In [13]) foi definida de modo a
                                    # obter parâmetros nominais arbitrários. Tal construção é feita, passando como
                                    # parâmetro o **kwargs. O parâmetro não precisa ser chamado de kwargs,
                                    # mas é uma boa prática. Já os dois asteriscos antes do parâmetro é obrigatório.
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    for chave, valor in kwargs.items(): # A função items não é built-in, ela pertence aos objetos do tipo dicionário,
                                        # por isso a chamada é feita como "kwargs.items()" (ou seja, objeto.função).
        print(f"variável = {chave}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros(cidade="São Paulo", idade=33, nome="João")
print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)