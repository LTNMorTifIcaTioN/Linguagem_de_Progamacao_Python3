"""
Seaborn é outra biblioteca Python, também baseada na matplotlib,
que foi desenvolvida especificamente para criação de gráficos. Seaborn pode ser instalado via pip install:
pip install seaborn
e para utilizar no projeto existe uma convenção para sintaxe:
import seaborn as sns.
"""
import seaborn as sns


# Configurando o visual do gráfico. Leia mais em https://seaborn.pydata.org/generated/seaborn.set.html#seaborn.set
sns.set(style="whitegrid") # opções: darkgrid, whitegrid, dark, white, ticks
df_tips = sns.load_dataset('tips')
print(df_tips.info())
df_tips.head()
print('\n===========================================================================================================\n')

"""
O tipo de dados que uma coluna possui é muito importante para a biblioteca seborn,
uma vez que as funções usadas para construir os gráficos são dividas em grupos:
relacional, categóricos,distribuição, regressão, matriz e grids.
"""

# Função Barplot ()
"""
Dentro do grupo de funções para gráficos de variáveis categóricas, temos o barplot(),
que permite criar gráficos de barras, mas por que usaríamos essa função e não a da biblioteca pandas?
A resposta está nas opções de parâmetros que cada biblioteca suporta. Veja o construtor da função barplot:
seaborn.barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, estimator=function mean, ci=95,
n_boot=1000, units=None, seed=None, orient=None, color=None, palette=None, saturation=0.75, errcolor='.26',
errwidth=None, capsize=None, dodge=True, ax=None, **kwargs). 
"""
from matplotlib import pyplot as plt

fig, ax = plt.subplots(1, 3, figsize=(15, 5))
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
plt.show()

# A biblioteca seaborn integra totalmente com a matplotlib. Vamos criar um gráfico que nos mostre o valor médio diário de venda.

plt.figure(figsize=(10, 5))
ax = sns.barplot(x="day", y="total_bill", data=df_tips)
ax.axes.set_title("Venda média diária", fontsize=14)
ax.set_xlabel("Dia", fontsize=14)
ax.set_ylabel("Venda média ", fontsize=14)
ax.tick_params(labelsize=14)
plt.show()
print('\n===========================================================================================================\n')


# Função Scartterplot ()
"""
Os gráficos do grupo relacional, permitem avaliar, de forma visual a relação entre duas variáveis: x, y.
A função possui a seguinte sintaxe:
seaborn.scatterplot(x=None, y=None, hue=None, style=None, size=None, data=None, palette=None, hue_order=None,
hue_norm=None, sizes=None, size_order=None, size_norm=None, markers=True, style_order=None, x_bins=None, y_bins=None,
units=None, estimator=None, ci=95, n_boot=1000, alpha='auto', x_jitter=None,
y_jitter=None, legend='brief', ax=None, **kwargs).
"""

plt.figure(figsize=(10, 5))
sns.scatterplot(data=df_tips, x="total_bill", y="tip")
plt.show()