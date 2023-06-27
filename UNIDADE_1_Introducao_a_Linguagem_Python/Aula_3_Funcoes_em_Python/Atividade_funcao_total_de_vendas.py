"""
Após uma primeira reunião, a equipe fez um levantamento de requisitos e concluiu que a
função a ser construída precisa considerar os seguintes itens:

o valor do produto (obrigatório).
a quantidade do produto (obrigatório).
a moeda em que deve ser feito o cálculo (obrigatório, sendo padrão o real).
a porcentagem do desconto que será concedida na compra (opcional).
a porcentagem de acréscimo, que depende da forma de pagamento (opcional).

Uma conta não pode ter desconto e acréscimo ao mesmo tempo. Nessa primeira versão, você deve considerar
o valor do dólar em R$ 5,00 e do euro 5,70. Ainda não foram definidos os detalhes de como os dados serão capturados
e tratados após serem digitados e submetidos. Porém, você deve entregar a versão inicial da função,
para que a equipe comece a fazer os primeiros testes.
"""

print('In[1]')
def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):
    v_bruto = valor_prod * qtde
    if desconto:
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif acrescimo:
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        v_liquido = v_bruto
    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0

valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")

print()
print('==============================================================================================================')

print('In[2]')
def calcular_valor(valor_prod, qtde, moeda="real", **kwargs):
    v_bruto = valor_prod * qtde
    if 'desconto' in kwargs:
        desconto = kwargs['desconto']
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif 'acrescimo' in kwargs:
        acrescimo = kwargs['acrescimo']
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        v_liquido = v_bruto
    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0

valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")