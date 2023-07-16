# Matplotlib
"""
A instalação da biblioteca pode ser feita via pip install:
pip install matplotlib
lembrando que em ambientes como o projeto Anaconda e o Colab esse recurso já está disponível.
O módulo pyplot possui uma coleção de funções que permitem criar e personalizar os gráficos.
Existem duas sintaxes que são amplamente adotadas para importar essa biblioteca para o projeto:
* import matplotlib.pyplot as plt
* from matplotlib import pyplot as plt
"""

from matplotlib import pyplot as plt
import random


dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)
print(plt.plot(dados1, dados2)) # pyplot gerencia a figura e o eixo
plt.show()

"""
Existem essencialmente duas maneiras de usar o Matplotlib:

1 - Deixar para o pyplot criar e gerenciar automaticamente figuras e eixos, e usar as funções do pyplot para plotagem.
2 - Criar explicitamente figuras e eixos e chamar métodos sobre eles (o "estilo orientado a objetos (OO)").
"""

# Figura com eixo variável
"""
Vamos explorar o estilo orientado a objetos, começando pela criação de eixos de forma explícita,
ou seja com atribuição a uma variável. Vamos criar uma figura com 1 linha 2 duas colunas, ou seja, teremos dois eixos.
Pense nos eixos como uma matriz, na qual cada eixo é uma posição que pode ter uma figura alocada.
Vale ressaltar que sobre um eixo (sobre uma figura), podem ser plotados diversos gráficos.
Para criar essa estrutura usamos a sintaxe: fig, ax = plt.subplots(1, 2),
onde fig e ax são os nomes das variáveis escolhidas. A variável ax, é do tipo array numpy, ou seja,
os eixos nada mais são, que uma matriz de contêineres para se criar os plots.
Como a figura possui dois eixos, temos que especificar em qual vamos plotar,
para isso informamos qual contêiner vamos usar: ax[0] ou ax[1].
"""

import numpy as np

x = range(5)
x = np.array(x) # temos que converter para um array numpy, senão o plot não consegue fazer operações.
fig, ax = plt.subplots(1, 2, figsize=(12, 5)) # Cria figura com subplots: 1 linha, 2 colunas e eixos

print("Tipo de ax = ", type(ax))
print("Conteúdo de ax[0] = ", ax[0])
print("Conteúdo de ax[1] = ", ax[1])

ax[0].plot(x, x, label='eq_1') # cria gráfico sobre eixo 0
ax[0].plot(x, x**2, label='eq_2') # cria gráfico sobre eixo 0
ax[0].plot(x, x**3, label='eq_3') # cria gráfico sobre eixo 0
ax[0].set_xlabel('Eixo x')
ax[0].set_ylabel('Eixo y')
ax[0].set_title("Gráfico 1")
ax[0].legend()

ax[1].plot(x, x, 'r--', label='eq_1') # cria gráfico sobre eixo 1
ax[1].plot(x**2, x, 'b--', label='eq_2') # cria gráfico sobre eixo 1
ax[1].plot(x**3, x, 'g--', label='eq_3') # cria gráfico sobre eixo 1
ax[1].set_xlabel('Novo Eixo x')
ax[1].set_ylabel('Novo Eixo y')
ax[1].set_title("Gráfico 2")
ax[1].legend()
plt.show()
