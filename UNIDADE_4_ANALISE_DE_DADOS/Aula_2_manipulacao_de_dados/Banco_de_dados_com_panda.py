"""
A biblioteca pandas possui dois métodos que permitem executar instruções SQL em banco de dados. Os métodos são:

* pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
* pandas.read_sql_query(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)

O mínimo de parâmetros que ambos métodos exigem é a instrução SQL e uma conexão com um banco de dados (con).
A conexão com o banco de dados, deve ser feita usando uma outra biblioteca, por exemplo,
sqlalchemy (suporte para diversos bancos), pyodbc para SQL Server, cx_Oracle para Oracle, psycopg2 para Postgresql,
dentre outras.
"""

import psycopg2
import pandas as pd

host = '192.168.0.1'
port = '8080'
database = 'XXXXX'
username = 'XXXXX'
password = 'XXXXX'
conn_str = fr"dbname='{database}' user='{username}' host='{host}' password='{password}' port='{port}'"
conn = psycopg2.connect(conn_str)
query = "select * from XXX.YYYY"
df = pd.read_sql(query, conn)
print(df)
print('\n===========================================================================================================\n')

import mysql.connector

host = '192.168.0.1'
port = '8080'
database = 'XXXXX'
username = 'XXXXX'
password = 'XXXXX'
conn_str = fr"host={host}, user={username}, passwd={password}, database={database}"
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")
query = "select * from XXX.YYYY"
df = pd.read_sql(query, conn)
