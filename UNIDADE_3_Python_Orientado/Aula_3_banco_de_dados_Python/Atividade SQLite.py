import sqlite3

class DDLSQLite:
    def _conectar(self, nome_banco):
        nome_banco += '.db'
        conn = sqlite3.connect(nome_banco)
        return conn

    def criar_banco_de_dados(self,nome_banco):
        nome_banco += '.db'
        sqlite3.connect(nome_banco).close()
        print(f"O banco de dados {nome_banco} foi criado com sucesso!")
        return None

    def criar_tabela(self, nome_banco, ddl_create):
        conn = self._conectar(nome_banco)
        cursor = conn.cursor()
        cursor.execute(ddl_create)
        cursor.close()
        conn.close()
        print(f"Tabela criada com sucesso!")
        return None

    def apagar_tabela(self, nome_banco, tabela):
        conn = self._conectar(nome_banco)
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE {tabela}")
        cursor.close()
        conn.close()
        print(f"A tabela {tabela} foi excluída com sucesso!")
        return None


class CrudSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco + '.db'

    def _conectar(self):
        conn = sqlite3.connect(self.nome_banco)
        return conn

    def inserir_registro(self, tabela, registro):
        colunas = tuple(registro.keys())
        valores = tuple(registro.values())
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""INSERT INTO {tabela} {colunas} VALUES {valores}"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dados inseridos com sucesso!")
        return None

    def ler_registros(self, tabela):
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""SELECT * FROM {tabela}"""
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado

    def atualizar_registro(self, tabela, dado, condicao):
        campo_alterar = list(dado.keys())[0]
        valor_alterar = dado.get(campo_alterar)
        campo_condicao = list(condicao.keys())[0]
        valor_condicao = condicao.get(campo_condicao)
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""UPDATE {tabela} SET {campo_alterar} = '{valor_alterar}' WHERE {campo_condicao} = {valor_condicao}"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dado atualizado com sucesso!")
        return None

    def apagar_registro(self, tabela, condicao):
        campo_condicao = list(condicao.keys())[0]
        valor_condicao = condicao.get(campo_condicao)
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""DELETE FROM {tabela} WHERE {campo_condicao} = {valor_condicao}"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dado excluído com sucesso!")
        return None


# instancia um objeto
objeto_ddl = DDLSQLite()

# Cria um banco de dados
objeto_ddl.criar_banco_de_dados('desafio')
# Cria uma tabela chamada cliente
ddl_create = """
CREATE TABLE cliente (
id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome_cliente TEXT NOT NULL,
cpf VARCHAR(14) NOT NULL,
email TEXT NOT NULL,
telefone VARCHAR(15),
cidade TEXT,
estado VARCHAR(2) NOT NULL,
data_cadastro DATE NOT NULL
);
"""

# objeto_ddl.criar_tabela(nome_banco='desafio', ddl_create=ddl_create)

# Caso precise excluir a tabela, o comando a seguir deverá ser usado
#objeto_ddl.apagar_tabela(nome_banco='desafio', tabela='cliente')

objeto_dml = CrudSQLite(nome_banco='desafio')

# Inserir registros
dados = [
    {
        'nome_cliente': 'João',
        'cpf': '111.111.111-11',
        'email': 'joao@servidor',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'data_cadastro': '2020-01-01'
    },
    {
        'nome_cliente': 'Maria',
        'cpf': '222.222.222-22',
        'email': 'maria@servidor',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'data_cadastro': '2020-01-01'
    },
]

# Para cada dicionário na lista de dados, invoca o método de inserção:
for valor in dados:
    objeto_dml.inserir_registro(tabela='cliente', registro=valor)

# Carrega dados salvos
dados_carregados = objeto_dml.ler_registros(tabela='cliente')
for dado in dados_carregados:
    print(dado)

# Atualiza registro
dado_atualizar = {'telefone': '(11)1.1111-1111'}
condicao = {'id_cliente': 1}
objeto_dml.atualizar_registro(tabela='cliente', dado=dado_atualizar, condicao=condicao)
dados_carregados = objeto_dml.ler_registros(tabela='cliente')
for dado in dados_carregados:
    print(dado)

# Apaga registro
condicao = {'id_cliente': 2}
objeto_dml.apagar_registro(tabela='cliente', condicao=condicao)
for dado in dados_carregados:
    print(dado)