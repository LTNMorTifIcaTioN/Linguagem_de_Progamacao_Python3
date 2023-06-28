"""
Você foi alocado em um projeto no qual precisa implementar uma função que faça a transformação
de dedup em uma lista de CPFs. Além do dedup, você também precisa remover os caracteres ponto e traço do CPF,
deixando somente números, e verificar se eles possuem 11 dígitos [caso contrário,
o CPF não deve ser incluído na lista de CPFs válidos].
"""

# Parte 1 - Implementar o algoritmo de busca linear
def executar_busca_linear(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return True
    return False

# Parte 2 - criar a função que faz o dedup e os tratamentos no cpf
def criar_lista_dedup(lista):
    lista_dedup = []
    for cpf in lista:
        cpf = str(cpf)
        cpf = cpf.replace("-", "").replace(".", "")
        if len(cpf) == 11:
            if not executar_busca_linear(lista_dedup, cpf):
                lista_dedup.append(cpf)
    return lista_dedup

# Parte 3 - Criar uma função de teste
def testar_funcao(lista_cpfs):
    lista_dedup = criar_lista_dedup(lista_cpfs)
    print(lista_dedup)

lista_cpfs = ['111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
testar_funcao(lista_cpfs)