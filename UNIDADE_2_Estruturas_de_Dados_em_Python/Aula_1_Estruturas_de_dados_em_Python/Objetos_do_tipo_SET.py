"""
Um objeto do tipo set habilita operações matemáticas de conjuntos, tais como:
união 'union()'
intersecção 'intersection()'
diferença 'difference()'
Esse tipo de estrutura pode ser usado em testes de associação e remoção de valores duplicados de uma sequência.

Das operações que já conhecemos sobre sequências, conseguimos usar nessa nova estrutura:
len(s)
x in s
x not in s

Em Python, os objetos do tipo set podem ser construídos destas maneiras:

Usando um par de chaves e elementos separados por vírgulas: set1 = {'a', 'b', 'c'}
Usando o construtor de tipo: set(iterable)
PS: Não é possível criar um set vazio, com set = {}, pois essa é a forma de construção de um dicionário.
"""

print('In[18]')

vogais_1 = {'aeiou'}  # sem uso do construtor

print(type(vogais_1), vogais_1)

vogais_2 = set('aeiouaaaaaa')  # construtor com string

print(type(vogais_2), vogais_2)

vogais_3 = set(['a', 'e', 'i', 'o', 'u'])  # construtor com lista

print(type(vogais_3), vogais_3)

vogais_4 = set(('a', 'e', 'i', 'o', 'u'))  # construtor com tupla

print(type(vogais_4), vogais_4)

print()
print('==============================================================================================================')


print('IN[19]')

def create_report():
    componentes_verificados = set([
        'caixas de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub',
         'impressora', 'joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break',
         'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner', 'teclado', 'webcam'
    ])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])
    qtde_componentes_verificados = len(componentes_verificados)
    qtde_componentes_com_defeito = len(componentes_com_defeito)
    componentes_ok = componentes_verificados.difference(componentes_com_defeito)
    # Essa operação também poderia ser feita com o sinal de subtração:
    # componentes_ok = componentes_verificados - componentes_com_defeito

    print(f"Foram verificados {qtde_componentes_verificados} componentes.\n")
    print(f"{qtde_componentes_com_defeito} componentes apresentaram defeito.\n")
    print("Os componentes que podem ser vendidos são:")

    for item in componentes_ok:
        print(item)

create_report()