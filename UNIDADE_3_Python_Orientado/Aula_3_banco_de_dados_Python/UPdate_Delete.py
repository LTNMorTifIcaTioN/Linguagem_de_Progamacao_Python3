"""
Ao inserir um registro no banco, pode ser necessário alterar o valor de uma coluna,
o que pode ser feito por meio da instrução SQL UPDATE.
"""

# Só é preciso importar a biblioteca uma vez. Importamos novamente para manter to_do o código em uma única célula

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()
cursor.execute("UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 5")
conn.commit()
cursor.execute("SELECT * FROM fornecedor")

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()

"""
Delete - Ao inserir um registro no banco, pode ser necessário removê-lo no futuro,
o que pode ser feito por meio da instrução SQL DELETE.
"""

# Só é preciso importar a biblioteca uma vez. Importamos novamente para manter todo o código em uma única célula

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = 2")
conn.commit()
cursor.execute("SELECT * FROM fornecedor")

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()