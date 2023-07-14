"""
Todos os métodos capazes de fazer a leitura dos dados estruturados possuem prefixo pd.read_XXX,
onde pd é o apelido dado no momento da importação da biblioteca e XXX é o restante da sintaxe do método.
Dentre todos os possíveis métodos para leitura, nessa aula vamos estudar o read_json, o read_csv e a função read_sql,
que contempla a função read_sql_query.
"""

"""
JSON (JavaScript Object Notation - Notação de Objetos JavaScript) é uma formatação leve de troca de dados
e independente de linguagem de programação. Os dados nesse formato podem ser encontrados como
uma coleção de pares chave/valor ou uma lista ordenada de valores.
Uma chave pode conter uma outra estrutura interna, criando um arquivo com multiníveis.
"""

"""
CSV (comma-separated values - valores separados por vírgula) é um formato de arquivo,
nos quais os dados são separados por um delimitador. Originalmente, esse delimitador é uma vírgula (por isso o nome),
mas na prática um arquivo CSV pode ser criado com qualquer delimitador,
por exemplo, por ponto e vírgula (;), por pipe (|), dentre outros. Por ser um arquivo de texto,
é fácil de ser lido em qualquer sistema, por isso se tornou tão democrático.
"""

# Leitura de JSON e CVS com

import pandas as pd

"""
A leitura de um arquivo JSON deve ser feita com o método:
pandas.read_json(path_or_buf=None, orient=None, typ='frame', dtype=None, convert_axes=None, convert_dates=True,
keep_default_dates=True, numpy=False, precise_float=False, date_unit=None, encoding=None, lines=False, chunksize=None,
compression='infer'). 
"""

print(pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head())
print('===============================================================================================================')
print()
"""
A leitura de um arquivo CSV deve ser feita com o método:
pandas.read_csv(filepath_or_buffer: Union[str, pathlib.Path, IO[~ AnyStr]], sep=',', delimiter=None, header='infer',
names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None,
converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None,
na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False,
infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False,
chunksize=None, compression='infer', thousands=None, decimal: str = '.', lineterminator=None, quotechar='"', quoting=0,
doublequote=True, escapechar=None, comment=None, encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True,
delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None).
"""

print(pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv").head())