"""
CRUD é um acrônimo para as quatro operações de DML que podemos fazer em uma tabela no banco de dados.
Podemos inserir informações (create), ler (read), atualizar (update) e apagar (delete).
Os passos necessários para efetuar uma das operações do CRUD são sempre os mesmos:
(i) estabelecer a conexão com um banco;
(ii) criar um cursor e executar o comando;
(iii) gravar a operação;
(iv) fechar o cursor e a conexão.
"""

# Create - Vamos começar inserindo registros na tabela fornecedor.
# Só é preciso importar a biblioteca uma vez. Importamos novamente para manter to_do o código em uma única célula

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
""")

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa B', '22.222.222/2222-22', 'Rio de Janeiro', 'RJ', '22222-222', '2020-01-01')
""")

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa C', '33.333.333/3333-33', 'Curitiba', 'PR', '33333-333', '2020-01-01')
""")

conn.commit()

print("Dados inseridos!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)

cursor.close()
conn.close()

"""
Uma maneira mais prática de inserir vários registros é passar uma lista de tuplas,
na qual cada uma destas contém os dados a serem inseridos em uma linha.
Nesse caso, teremos que usar o método executemany() do cursor.
"""

# Só é preciso importar a biblioteca uma vez. Importamos novamente para manter to_do o código em uma única célula

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

dados = [
    ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01'),
    ('Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01'),
    ('Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')
]

cursor.executemany("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES (?, ?, ?, ?, ?, ?)""", dados)

conn.commit()

print("Dados inseridos!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)

cursor.close()
conn.close()