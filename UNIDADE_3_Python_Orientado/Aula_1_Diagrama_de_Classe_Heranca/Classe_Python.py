"""
Objetos são os componentes de um programa OO.
Uma classe é um modelo para um objeto.
Portanto, a classe é o modelo e o objeto é a existência física, em memória, do objeto.

Atributos - Os dados armazenados em um objeto representam o estado do objeto.

Métodos - O comportamento de um objeto representa o que este pode fazer.

Encapsulamento - O ato de combinar os atributos e métodos na mesma entidade.

Herança - A herança permite que uma classe herde os atributos e métodos de outra classe.

Polimorfismo - Em uma hierarquia de herança, todas as subclasses herdam as interfaces de sua superclasse.
No entanto, como toda subclasse é uma entidade separada,
cada uma delas pode exigir uma resposta separada para a mesma mensagem.
"""

print('In [1]: ')
class PrimeiraClasse:

    def imprimir_mensagem(self, nome): # Criando um método
        print(f"Olá {nome}, seja bem vindo!")

objeto1 = PrimeiraClasse() # Instanciando um objeto do tipo PrimeiraClasse
objeto1.imprimir_mensagem('João') # Invocando o método

print()
print('==============================================================================================================')


"""
Todo método em uma classe deve receber como primeiro parâmetro uma variável que indica a referência à classe;
por convenção, adota-se o parâmetro self.
"""

print('In [3]:')
class Calculadora:
    def somar(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1 * n2

    def dividir(self, n1, n2):
        return n1 / n2

    def dividir_resto(self, n1, n2):
        return n1 % n2

calc = Calculadora()
print('Soma:', calc.somar(4, 3))
print('Subtração:', calc.subtrair(13, 7))
print('Multiplicação:', calc.multiplicar(2, 4))
print('Divisão:', calc.dividir(16, 5))
print('Resto da divisão:', calc.dividir_resto(7, 3))