"""
Também podemos criar uma figura, sem atribuir o eixo a uma variável. Nesse caso,
temos que usar a função plt.subplot(n_rows, n_cols2, plot_number), para definir onde será plotado o gráfico.
"""
from matplotlib import pyplot as plt
import numpy as np
import random

x = range(5)
x = np.array(x) # temos que converter para um array numpy, senão o plot não consegue fazer operações.
fig = plt.subplots(figsize=(12, 5)) # Cria figura sem eixo
plt.subplot(121) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 1
plt.plot(x, x, label='eq_1')
plt.plot(x, x**2, label='eq_2')
plt.plot(x, x**3, label='eq_3')
plt.title("Gráfico 1")
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.legend()
plt.subplot(122) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 2
plt.plot(x, x, 'r--', label='eq_1')
plt.plot(x**2, x, 'b--', label='eq_2')
plt.plot(x**3, x, 'g--', label='eq_3')
plt.title("Gráfico 2")
plt.xlabel('Novo eixo x')
plt.ylabel('Novo eixo y')
plt.legend()
plt.show()
print('\n===========================================================================================================\n')

"""
o optar por utilizar eixos como variáveis ou não, o desenvolvedor deve ficar atento somente as regras de sintaxe
e as funções disponíveis para cada opção. Podemos então resumir que:

plt.subplots() é usado para criar um layout de figura e subplots. 
plt.subplot() é usado para adicionar um subplot em um figura existente. 
"""

# Biblioteca pandas
"""
As principais estruturas de dados da biblioteca pandas (Series e DataFrame) possuem o método plot(),
construído com base no matplotlib e que permite criar gráficos a partir dos dados nas estruturas. 
"""
import pandas as pd

dados = {
    'turma':['A', 'B', 'C'],
    'qtde_alunos':[33, 50, 45]
    }

df = pd.DataFrame(dados)
print(df)
print('\n===========================================================================================================\n')


# A partir de um DataFrame, podemos invocar o método: df.plot(*args, **kwargs) para criar os gráficos.
df.plot(x='turma', y='qtde_alunos', kind='bar')
print(df)
print('\n===========================================================================================================\n')


df.plot(x='turma', y='qtde_alunos', kind='barh')
print(df)
print('\n===========================================================================================================\n')


df.plot(x='turma', y='qtde_alunos', kind='line')
print(df)
print('\n===========================================================================================================\n')


"""
Veja a seguir, fazemos a transformação no DF seguido do plot com o tipo pie.
Esse tipo de sintaxe é chamado de encadeamento, pois ao invés de fazermos a transformação,
salvar em um novo objeto e depois plotar, fazemos tudo em uma única linha, sem precisar criar o novo objeto.
"""
df.set_index('turma').plot(y='qtde_alunos', kind='pie')
print(df)
print('\n===========================================================================================================\n')
plt.show()

"""
Vale ressaltar que para todos os gráficos criados, a biblioteca oferece uma segunda opção de sintaxe, 
que é invocar o tipo de gráfico como método, por exemplo:

df.plot.bar(x='turma', y='qtde_alunos')
df.plot.line(x='turma', y='qtde_alunos')
df.set_index('turma').plot.pie(y='qtde_alunos')
"""
