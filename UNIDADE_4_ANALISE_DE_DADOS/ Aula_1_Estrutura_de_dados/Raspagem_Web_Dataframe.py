"""
 Fazer a extração da notícia com o requestes.get() convertendo tudo para uma única string
"""

import requests

texto_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text
print(texto_string[:100])
print('===============================================================================================================')
print()

"""
Como temos um conteúdo em HTML é conveniente utilizar a biblioteca Beautiful Soup,
para converter a string em uma estrutura HTML e então filtrar determinadas tags.
"""

from bs4 import BeautifulSoup

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('span', attrs={'class':'short-desc'})

print(type(bsp_texto))
print(type(lista_noticias))
print(lista_noticias[5])
print(lista_noticias[5].contents)
print('===============================================================================================================')
print()

"""
Criamos uma lista vazia.
"""
dados = []

for noticia in lista_noticias:
    """
    O código noticia.contents[0] retorna: <strong>Jan. 25
    </strong>, ao acessar a propriedade text, eliminamos as tags,
    então temos Jan. 25. Usamos a função strip() para eliminar espaço em branco na string e concatenamos com o ano.
    """
    data = noticia.contents[0].text.strip() + ', 2017' # Dessa informação <strong>Jan. 25 </strong> vai extrair Jan. 25, 2017
    """
    O código contents[1] retorna: "“You had millions of people that now aren't insured anymore.”"
    usamos o strip() para eliminar espaços em branco e a função replace para substituir os caracteres especiais por nada.
    """
    comentario = noticia.contents[1].strip().replace("“", '').replace("”", '')
    """
    O código noticia.contents[2] retorna: 
    <a href="https://www.nytimes.com/2017/03/13/us/politics/fact-check-trump-obamacare-health-care.html" target="_blank"
    >(The real number is less than 1 million, according to the Urban Institute.)</a></span>,
    ao acessar a propriedade text, eliminamos as tags então temos (The real number is less than 1 million,
    according to the Urban Institute.), o qual ajustamos para elimar espaços e os parênteses
    """
    explicacao = noticia.contents[2].text.strip().replace("(", '').replace(")", '')
    """
    o código noticia.find('a')['href'] retorna:
    https://www.nytimes.com/2017/03/13/us/politics/fact-check-trump-obamacare-health-care.html
    """
    url = noticia.find('a')['href']
    dados.append((data, comentario, explicacao, url))


"""
Agora que temos nossa lista de tuplas com os dados,
podemos criar o DataFrame e disponibilizar para um cientista de dados fazer a análise de sentimentos.
"""
import pandas as pd

df_noticias = pd.DataFrame(dados, columns=['data', 'comentário', 'explicação', 'url'])

print(df_noticias.shape)
print(df_noticias.dtypes)
print(df_noticias.head())