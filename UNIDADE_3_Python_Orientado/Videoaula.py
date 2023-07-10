# CLASSES E MÉTODOS
"""
ORIENTADO A OBJETOS:
* Uma receita (CLASSE) abstraí em um bolo (OBJETO) através das características (ATRIBUTOS) e do passo a passo (MÉTODOS).
* A CLASSE é uma maneira de organizar Dados e Funções juntos.
ps: Um método de classe (def) deve sempre chamar a si mesmo no argumento (self).

MÉTODO CONSTRUTOR DE CLASSE:
* O construtor é um método reservado chamado __init__;
* O parâmetro self é obrigatório e os demais são definidos pelo programador.

ex:
    class Pessoa:
        def __init__(self, nome, telefone):
            self.nome = nome
            self.telefone = telefone
"""

# class Conta:
#     def __init__(self, nome, numero):
#         self.cliente = nome
#         self.num = numero
#         self.saldo = 0.0
#
#     def Saldo(self):
#         return self.saldo
#
#     def getCLiente(self):
#         return self.cliente
#
#     def Depositar(self, valor):
#         self.saldo += valor
#
# conta1 = Conta('Joao', 1)
# conta1.Depositar(100.0)
# print(conta1.Saldo())
# print(conta1.getCLiente())
#
# conta2 = Conta('Maria', 2)
# conta2.Depositar((200.0))
# print(conta2.Saldo())


# BIBLIOTECAS E MÓDULOS
"""
BIBLIOTECAS:
* Math: Funções Matemáticas;
* Pillow: Imagens;
* Matplotlib: Gráficos e Plotagens;
* Numpy: Processamento de Matrizes;
* Panda: Análise de Dados;
import nomebiblioteca

MODULARIDADE EM PYTHON:
* Reuso;
* Necessidade de objetos, comandos e ferramentas específicas;
* .py;
* Quando módulo é importado, todos os comandos nele são executados.
* Um módulo pode conter tanto instruções executáveis, quanto definições de funções e classes.

MÉTODO MAIN EM PYTHON:
* Função que sempre irá ocorrer ao executar o programa;
* Não passui retorno;
    if __name__ == '__main__':
        main()
"""

class Conta:
    def __init__(self, nome, numero):
        self.cliente = nome
        self.num = numero
        self.saldo = 0.0

    def Saldo(self):
        return self.saldo

    def getCLiente(self):
        return self.cliente

    def Depositar(self, valor):
        self.saldo += valor

    def Transferencia(self, conta, valor):
        self.saldo = self.saldo-valor
        conta.saldo = conta.saldo + valor


# Banco de Dados
"""
CONEXÃO DE BANCO DE DADOS SQL EM PYTHON
* Importar o módulo: import sqlite3
* Conexão do python com o BD:
    conector = sqlite3.connect("nome.db")
* Arquivo gerado é em formato binário e para manipulá-lo, usaremos o SQLite Studio.
"""

import sqlite3

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()
sql = """
    create table cadastro (codigo integer, nome txt, idade integer)
    """
cursor.execute(sql)

sql = """
    insert into cadastro (codigo, nome, idade) values (1284, 'Pedro Oliveira', 32)
    """
cursor.execute(sql)

sql = """
    insert into cadastro (codigo, nome, idade) values (1309, 'Maria Lúcia Machado', 37)
    """
cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()

"""
CRUD
Create (criação);
Read (consulta);
Update (atualização);
Delete (deletar);
"""

# READ (consulta)
def Read():
    sql = "select * from cadastro"  # seleciona todos os dados se chamar execute
    cursor.execute(sql)
    dados = cursor.fetchall()   # retorna todos os registros selecionados em uma lista de dados
    cursor.close()  # fecha cursor
    conector.close()    # fecha conector
    for d in dados:
        print(d[0], d[1], d[2])

# UPDATE (atualização)
def Update(Cod, new):   # new: novo valor adicionado; # Cod: valor a se buscar;
    cursor.execute("""
    UPDATE cadastro
    SET idade = ?
    where codigo = ?
    """, (new, Cod))    # ordem dos parâmetros a serem alterados
    conector.commit()

# Delete (deletar)
def ExcluiCliente(Cod):
    sql = "delete from cadastro where codigo = :param"
    cursor.execute(sql, {'param' : Cod})
    conector.commit()
    return "Cliente {} Excluído".format(Cod)