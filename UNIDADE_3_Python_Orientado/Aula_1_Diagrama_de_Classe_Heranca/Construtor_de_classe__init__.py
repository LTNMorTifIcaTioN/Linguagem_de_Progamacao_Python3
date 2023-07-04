"""
Um atributo de instância é uma variável precedida com o parâmetro self, ou seja,
a sintaxe para criar e utilizar é self.nome_atributo.
Em Python, o método construtor é chamado de __init__().
"""

print('In [5]: ')
class Televisao:
    def __init__(self):
        self.volume = 10

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

tv = Televisao()
print("Volume ao ligar a tv = ", tv.volume)
tv.aumentar_volume()
print("Volume atual = ", tv.volume)

print()
print('==============================================================================================================')

"""
Variáveis e métodos privados - Em linguagens de programação OO, como Java e C#, as classes,
os atributos e os métodos são acompanhados de modificadores de acesso, que podem ser: public, private e protected.
Em Python, não existem modificadores de acesso e todos os recursos são públicos.
Para simbolizar que um atributo ou método é privado, por convenção, usa-se um sublinhado "_"  antes do nome;
por exemplo, _cpf, _calcular_desconto().
"""

#In [7]:
class ContaCorrente:
    def __init__(self):
        self._saldo = None

    def depositar(self, valor):
        self._saldo += valor

    def consultar_saldo(self):
        return self._saldo

"""
Em Python, atributos e métodos privados são apenas uma convenção, pois, na prática,
os recursos podem ser acessados de qualquer forma.
"""