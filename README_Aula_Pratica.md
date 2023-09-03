# Linguagem_de_Programacao_Python3
Aulas da matéria de Linguagem de Programação em Python 3 da Faculdade de Ciência de Dados

AULA PRÁTICA
OBJETIVOS
Definição dos objetivos da aula prática:
Criar um programa que calcule IMC (Índice de Massa Corpórea) utilizando a ferramenta Google cloud Shell Editor, utilizando a linguagem de programação Python.

PROCEDIMENTOS PRÁTICOS
Criação de um programa de cálculo de IMC, utilizando o programa o Google cloud Shell Editor.

ATIVIDADE PROPOSTA:
Criação de um programa de cálculo de IMC utilizando a ferramenta Google cloud Shell Editor e descrever como é o funcionamento desse modelo, utilizando a linguagem de programação Python.
Criar um relatório no final da atividade.

PROCEDIMENTOS PARA A REALIZAÇÃO DA ATIVIDADE:

Você deverá:
Utilizando o Google cloud Shell Editor você irá criar um programa de cálculo de IMC, utilizando a linguagem de programação Python.
Descrever as características da ferramenta Google cloud Shell Editor e a linguagem utilizada (Python).


CHECKLIST:
Instalar o sistema Google cloud Shell Editor. Para criação e edição de arquivo simples, inicie o editor executando Code. no terminal do Cloud Shell. Essa ação abre o editor com o diretório de trabalho ativo definido no terminal. Para abrir um arquivo diretamente para edição rápida, execute code <filename> para abrir o editor sem o explorador de arquivos;

Descrição da experiência:
O Google Shell Editor é uma forma de acessar a tecnologia de computação do Google para realizar programação em nuvem de várias linguagens, sem a necessidade de uma máquina robusta para a atividade, virtualizando todo o processamento de dados. Minha experiência pessoal não foi bastante positiva, pois considero o ambiente bastante confuso e poluído, cheio de informações confusas e de difícil acesso, atrapalhando usuários novos a terem acesso as funções da ferramenta. Foi bastante trabalhoso para poder me localizar.

CRIAR UM PROGRAMA QUE FAÇA CÁLCULO DO IMC;
https://github.com/LTNMorTifIcaTioN/Linguagem_de_Programacao_Python3/commit/c43803f9bcf58bfe0436766b2979eb2b52d2b776

CRIAR UM RELATÓRIO NO FINAL DA ATIVIDADE.
1) Para este programa foram utilizados os suprimentos das bibliotecas Pandas, OS, Mathplotlib e Numpy.
2) O IMC é calculado dividindo o peso (em quilogramas) pelo quadrado da altura (em metros). O IMC calculado é então retornado como resultado.
3) O IMC é calculado da mesma forma que na função anterior. Em seguida, os dados são armazenados em um dicionário, que é usado para criar um DataFrame usando a biblioteca pandas. O DataFrame é então salvo em um arquivo CSV chamado "dados.csv".
4) O arquivo CSV é carregado em um DataFrame usando a função read_csv da biblioteca pandas. Em seguida, é verificado se o DataFrame está vazio. Se estiver vazio, é exibida uma mensagem informando que nenhum dado foi registrado. Caso contrário, os dados registrados são exibidos.
5) Como no caso anterior, o arquivo CSV é carregado em um DataFrame usando a função read_csv da biblioteca pandas. Em seguida, é verificado se o DataFrame está vazio. Se estiver vazio, é exibida uma mensagem informando que não há dados para desempilhar. Caso contrário, a última linha do DataFrame é removida usando a sintaxe df[:-1]. O DataFrame atualizado é então salvo no arquivo CSV.
6) É verificado se o arquivo CSV existe usando a função os.path.exists. Se o arquivo existir, ele é removido usando a função os.remove. Caso contrário, é exibida uma mensagem informando que não há dados para apagar.
7) Novamente o arquivo CSV é carregado em um DataFrame usando a função read_csv da biblioteca pandas. Em seguida, é verificado se o DataFrame está vazio. Se estiver vazio, é exibida uma mensagem informando que não há dados para exibir o histograma de dispersão. Caso contrário, é plotado um histograma de dispersão usando a função scatter da biblioteca matplotlib, com o peso no eixo x e a altura no eixo y. O gráfico é exibido usando a função show. Após plotar o histograma de dispersão, são exibidas as estatísticas dos dados. A função mean é usada para calcular a média, median para calcular a mediana, mode para calcular a moda, std para calcular o desvio padrão e quantile para calcular os quantis. Os resultados são impressos na saída.
8) O programa é um laço sem fim tratado contra erros, que pode ser encerrado o digitar o numeral ‘9’ no menu.
