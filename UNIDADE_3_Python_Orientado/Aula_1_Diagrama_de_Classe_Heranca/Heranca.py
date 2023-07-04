"""
A sintaxe para criar a herança é feita com parênteses após o nome da classe: class NomeClasseFilha(NomeClassePai).
Se for uma herança múltipla, cada superclasse deve ser separada por vírgula.
"""

print('In [8]: ')
class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = None
        self.salacio = None

    def bater_ponto(self):
    # código aqui
        pass

    def fazer_login(self):
    # código aqui
        pass

class Cliente(Pessoa):

    def __init__(self):
        self.codigo = None
        self.dataCadastro = None

    def fazer_compra(self):
        # código aqui
        pass

    def pagar_conta(self):
        # código aqui
        pass

f1 = Funcionario()
f1.nome = "Funcionário A"
print(f1.nome)
c1 = Cliente()
c1.cpf = "111.111.111-11"
print(c1.cpf)
print(dir(Pessoa()))
