"""
Além das operações de CRUD, é importante sabermos extrair informações estruturais do banco de dados e das tabelas.
Por exemplo, considerado um banco de dados:
Quais tabelas existem ali?
Quais são os campos de uma tabela?
Qual é a estrutura da tabela, ou seja, qual DDL foi usada para gerá-la?
Os comandos necessários para extrair essas informações podem mudar entre os bancos,
mas vamos ver como extraí-las do SQLite. No código a seguir,
temos uma instrução SQL capaz de retornar as tabelas no banco SQLite e outra capaz de extrair as DDLs
usadas para gerar as tabelas.
"""

# Só é preciso importar a biblioteca uma vez. Importamos novamente para manter to.do o código em uma única célula

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

# Lista as tabelas do banco de dados

cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")
print('Tabelas:')

for tabela in cursor.fetchall():
    print(tabela)

# Captura a DDL usada para criar a tabela
tabela = 'fornecedor'
cursor.execute(f"""SELECT sql FROM sqlite_master WHERE type='table' AND name='{tabela}'""")
print(f'\nDDL da tabela {tabela}:')

for schema in cursor.fetchall():
    print("%s" % (schema))
    cursor.close()

conn.close()