"""
Foi lhe dada a missão de escolher uma ferramenta para desenvolver um protótipo para o cliente que fabrica peças
automotivas. Ao tabular os dados do gráfico, aparece um valor interessante na coluna que mostra o aumento mês após mês.
De acordo com as informações o aumento tem sido constante.
Se o aumento é constante, podemos usar uma função do primeiro grau para prever qual será o resultado em qualquer mês.
A função será r = c * mes, onde, r é o resultado que queremos, c é a constante de crescimento e mes é a variável de
entrada. Dessa forma, ao obter um mês qualquer (2, 4, 30, etc) podemos dizer qual o resultado.
mes = 2; c = 200 -> r = 200 * 2 = 400 (Valor correto para o mês 2.
mes = 3; c = 200 -> r = 200 * 3 = 600 (Valor correto para o mês 3.
mes = 4; c = 200 -> r = 200 * 4 = 800 (Valor correto para o mês 4.
mes = 5; c = 200 -> r = 200 * 5 = 1000 (Valor correto para o mês 5.
"""
C = (200)
mes = input('Digite o mês que quer saber o resultado: ')
mes = int(mes)
r = C * mes
print(f'A quantidade de peças para o mês {mes} será de {r} peças.')
