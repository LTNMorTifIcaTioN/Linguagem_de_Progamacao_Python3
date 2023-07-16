import pandas as pd
import sqlite3

conector = sqlite3.connect("conta.db")

df = pd.read_sql_query("SELECT * from cadastro", conector)
print(df.head())

data = pd.DataFrame([[200, 'blusa', 59.9], [101, 'calça', 89.9], [203, 'camisa', 99.9]],
                    columns= ['id', 'descrição', 'valor'])

data.to_sql('Produto', conector)