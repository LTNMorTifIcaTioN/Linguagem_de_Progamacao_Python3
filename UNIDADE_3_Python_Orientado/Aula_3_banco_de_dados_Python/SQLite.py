"""
O primeiro passo é importar o módulo sqlite3. Como o módulo está baseado na especificação DB-API 2.0
descrita pelo PEP 249, ele utiliza o método connnect() para se conectar a um banco de dados.
Em razão da natureza do SQLite (ser um arquivo no disco rígido), ao nos conectarmos a um banco,
o arquivo é imediatamente criado na pasta do projeto (se estiver usando o projeto Anaconda,
o arquivo é criado na mesma pasta em que está o Jupyter Notebook).
"""

import sqlite3

conn = sqlite3.connect('aulaDB.db')
print(type(conn))

"""
Criando uma tabela - Agora que temos uma conexão com um banco de dados,
vamos utilizar uma instrução DDL da linguagem SQL para criar a tabela fornecedor.
O comando SQL que cria a tabela fornecedor está no código a seguir e foi guardado em uma variável chamada ddl_create.
"""

ddl_create = """
CREATE TABLE fornecedor (
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    cidade TEXT, 
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL
);
"""

"""
Já temos a conexão e a DDL. Agora basta utilizar um mecanismo para que esse comando seja executado no banco.
Esse mecanismo, deve estar implementado em um método chamado execute() de um objeto cursor.
Os cursores desempenham o papel de pontes entre os conjuntos fornecidos como respostas das consultas
e as linguagens de programação que não suportam conjuntos.
Portanto, sempre que precisarmos executar um comando SQL no banco usando a linguagem Python,
usaremos um cursor para construir essa ponte. 
"""

cursor = conn.cursor()
cursor.execute(ddl_create)

print(type(cursor))
print("Tabela criada!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)

cursor.close()
conn.close()