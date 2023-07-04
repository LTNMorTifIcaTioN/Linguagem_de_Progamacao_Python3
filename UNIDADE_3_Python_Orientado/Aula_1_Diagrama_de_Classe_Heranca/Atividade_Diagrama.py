"""
Como desenvolvedor em uma empresa de consultoria de software,
você foi alocado para iniciar a implementação de um sistema de vendas. Nesta primeira etapa,
os engenheiros de software fizeram um levantamento de requisitos e identificaram que o sistema vai atender
a três tipos distintos de clientes: pessoas físicas (PF) que compram com assiduidade,
pessoas físicas que compram esporadicamente e pessoas jurídicas (PJ).

Os clientes VIPs podem comprar um número ilimitado de itens. Por sua vez, os clientes PF que não são VIPs,
só podem comprar até 20 itens, e os clientes PJ podem comprar até 50 itens. No levantamento de requisitos,
também foi determinado que cada tipo de cliente terá um cupom de desconto que será usado para conceder benefícios
nas compras. Os clientes VIPs terão um desconto de 20% a cada compra.

Os clientes esporádicos (PF) terão um desconto de 5%. Por sua vez, os clientes com CNPJ terão um desconto de 10%.
O cupom de desconto deverá ser encapsulado em um método.
"""

class Cliente:
    def __init__(self):
        self.nome = None
        self.email = None
        self.telefone = None
        self._cupom_desconto = 0

    def get_cupom_desconto(self):
        return self._cupom_desconto

    def realizar_compras(self, lista_itens):
        pass

class ClienteVipPF(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.2

    def realizar_compras(self, lista_itens):
        return f"Quantidade total de itens comprados = {len(lista_itens)}"

class ClientePF(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.05

    def realizar_compras(self, lista_itens):
        if len(lista_itens) <= 20:
            return f"Quantidade total de itens comprados = {len(lista_itens)}"
        else:
            return "Quantidade de itens superior ao limite permitido."

class ClientePJ(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.1

    def realizar_compras(self, lista_itens):
        if len(lista_itens) <= 50:
            return f"Quantidade total de itens comprados = {len(lista_itens)}"
        else:
            return "Quantidade de itens superior ao limite permitido."

cli1 = ClienteVipPF()
cli1.nome = "Maria"
print(cli1)
print(cli1.get_cupom_desconto())
print(cli1.realizar_compras(['item1', 'item2', 'item3']))