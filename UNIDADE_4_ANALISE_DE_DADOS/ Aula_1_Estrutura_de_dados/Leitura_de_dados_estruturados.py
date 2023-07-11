"""
A biblioteca possui uma série de métodos "read", cuja sintaxe é:
pandas.read_XXXXX() onde a sequência de X representa as diversas opções disponíveis.
* Método pandas.read_html()
parâmetros: pandas.read_html(io, match='.+', flavor=None, header=None, index_col=None, skiprows=None, attrs=None,
            parse_dates=False, thousands=',', encoding=None, decimal='.', converters=None, na_values=None,
            keep_default_na=True, displayed_only=True)
* Dentre todos, somente o "io" é o que recebe a URL a ser usada.
* Esse método procura por tags <table> na estrutura do código HTML e devolve uma lista de DataFrames contendo as tabelas que localizou.
"""
import pandas as pd

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))
print('===============================================================================================================')
print()
df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)
print(df_bancos.head())