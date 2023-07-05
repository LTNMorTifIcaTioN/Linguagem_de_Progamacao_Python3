"""
Matplotlib é uma biblioteca com funcionalidades para criar gráficos.
É importante ressaltar que, da forma pela qual fizemos a importação,
ambos os arquivos .py precisam estar no mesmo nível de pasta.
"""

# ler o arquivo salvo
file = open('relatorio_jogos.txt', 'r')
print('file = ', file, '\n')
info_relatorio = file.readlines()
file.close()
print("linha 1 = ", info_relatorio[0])

# Extrair somente a parta 'dd/mm' da linha
datas = [linha[1:6] for linha in info_relatorio]
print(sorted(datas))

datas_count = [(data, datas.count(data)) for data in set(datas)]
print(datas_count)

datas_count = dict(datas_count)
print(datas_count)

import matplotlib.pyplot as plt

eixo_x = datas_count.keys()
eixo_y = datas_count.values()
plt.figure(figsize=(15, 5))
plt.xlabel('Dia do mês')
plt.ylabel('Quantidade de jogos')
plt.xticks(rotation=45)
plt.bar(eixo_x, eixo_y)
plt.show()