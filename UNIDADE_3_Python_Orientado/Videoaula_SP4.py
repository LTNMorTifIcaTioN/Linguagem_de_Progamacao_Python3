import sqlite3

def ExcluirCliente(Cod):
    sql = "delete from cadastro where codigo = :param"
    cursor.execute(sql, {'param' : Cod})
    conector.commit()
    return print(f'Cliente {Cod}  excluído')

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()

ExcluirCliente(1284)