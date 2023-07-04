"""
Python permite que uma classe-filha herde recursos de mais de uma superclasse.
Para isso, basta declarar cada classe a ser herdada separada por vírgula.
"""

"""
Vamos implementar a solução na qual temos uma classe-base chamada ContaCorrente com os seguintes campos:

* Nome, que é do tipo string e deve ser público.
* Email, que é do tipo string e deve ser público.
* Telefone, que é do tipo string e deve ser público.
* Saldo, que é do tipo ponto flutuante e deve ser público.

A classe-base conta ainda com os métodos: 
* Depositar, que recebe como parâmetro um valor, não retorna nada e deve ser público.
* Obter saldo, que não recebe nenhum parâmetro, retorna um ponto flutuante e deve ser público.
* Sacar, que recebe como parâmetro um valor, retorna se foi possível sacar (booleano) e deve ser público.
* Checar saldo, que não recebe nenhum parâmetro, retorna um booleano e deve ser privado, ou seja,
será usado internamente pela própria classe.
"""

class ContaCorrente:
    def __init__(self,nome):
        self.nome = nome
        self.email = None
        self.telefone = None
        self._saldo = 0

    def _checar_saldo(self, valor):
        return self._saldo >= valor

    def depositar(self, valor):
        self._saldo+= valor

    def sacar(self, valor):
        if self._checar_saldo(valor):
            self._saldo -= valor
            return True
        else:
            return False

    def obter_saldo(self):
        return self._saldo


class ContaPF(ContaCorrente):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf

    def solicitar_emprestimo(self, valor):
        return self.obter_saldo() >= 500


class ContaPJ(ContaCorrente):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj

    def sacar_emprestimo(self, valor):
        return valor <= 5000


conta_pf1 = ContaPF("João", '111.111.111-11')
conta_pf1.depositar(1000)
print('Saldo atual é', conta_pf1.obter_saldo())
print('Receberá empréstimo = ', conta_pf1.solicitar_emprestimo(2000))
conta_pf1.sacar(800)
print('Saldo atual é', conta_pf1.obter_saldo())
print('Receberá empréstimo = ', conta_pf1.solicitar_emprestimo(2000))

print()
print('==============================================================================================================')


conta_pj1 = ContaPJ("Empresa A", "11.111.111/1111-11")
print('Saldo atual é', conta_pj1.obter_saldo())
print('Receberá empréstimo = ', conta_pj1.sacar_emprestimo(3000))