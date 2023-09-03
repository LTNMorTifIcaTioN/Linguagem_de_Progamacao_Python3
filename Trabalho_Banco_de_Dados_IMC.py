import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pytz

print(f'\033[1m C   O   N   T   R   O   L   E      D   E      I   M   C \033[0m\n ')
print(f'Projeto de Algoritmos em Python, Desenvolvido por Nayan Couto, Blumenau-SC em 2023\n')

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def salvar_dados(nome, peso, altura):
    imc = peso / (altura ** 2)

    # Carregar o arquivo CSV existente em um DataFrame, se existir
    try:
        df = pd.read_csv('dados.csv')
    except FileNotFoundError:
        df = pd.DataFrame()

    # Obter a data e hora atual em UTC-3 Brasil
    tz = pytz.timezone('America/Sao_Paulo')
    data_hora = datetime.now(tz).date().strftime('%Y%m%d')

    # Criar um dicionário com os novos dados
    novo_dado = {'Nome': nome, 'Peso': peso, 'Altura': altura, 'IMC': imc, 'Data': int(data_hora)}

    # Adicionar os novos dados ao DataFrame existente
    novo_df = pd.DataFrame(novo_dado, index=[0])
    df = pd.concat([df, novo_df], ignore_index=True)

    # Salvar o DataFrame atualizado em um arquivo CSV
    df.to_csv('dados.csv', index=False)

    print("Dados salvos com sucesso!")


def listar_dados():
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv('dados.csv')

    # Verificar se o DataFrame está vazio
    if df.empty:
        print("Nenhum dado registrado.")
    else:
        # Exibir os dados registrados
        print(df)


def desempilhar_dados():
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv('dados.csv')

    # Verificar se o DataFrame está vazio
    if df.empty:
        print("Nenhum dado registrado para desempilhar.")
    else:
        # Remover a última linha do DataFrame
        df = df[:-1]

        # Salvar o DataFrame atualizado em um arquivo CSV
        df.to_csv('dados.csv', index=False)

        print("Dados desempilhados com sucesso!")


def apagar_dados():
    # Verificar se o arquivo CSV existe
    if os.path.exists('dados.csv'):
        # Remover o arquivo CSV
        os.remove('dados.csv')
        print("Dados apagados com sucesso!")
    else:
        print("Nenhum dado registrado para apagar.")


def plot_histograma_dispersao_estatisticas():
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv('dados.csv')

    # Verificar se o DataFrame está vazio
    if df.empty:
        print("Nenhum dado registrado para exibir o histograma de dispersão e as estatísticas.")
    else:
        # Plotar o histograma de dispersão
        plt.scatter(df['Data'], df['IMC'])
        plt.xlabel('Data')
        plt.ylabel('IMC')
        plt.title('Histograma de Dispersão')

        # Adicionar uma linha de tendência
        z = np.polyfit(df['Data'], df['IMC'], 1)
        p = np.poly1d(z)
        plt.plot(df['Data'], p(df['Data']), color='red')

        plt.show()

        # Imprimir as estatísticas
        print("Estatísticas:")
        print(f"Média:")
        print(f"Peso: {df['Peso'].mean()}, Altura: {df['Altura'].mean()}, IMC: {df['IMC'].mean()}")
        print(f"\nMediana:")
        print(f"Peso: {df['Peso'].median()}, Altura: {df['Altura'].median()}, IMC: {df['IMC'].median()}")
        print(f"\nModa:")
        print(
            f"Peso: {df['Peso'].mode().iloc[0]}, Altura: {df['Altura'].mode().iloc[0]}, IMC: {df['IMC'].mode().iloc[0]}")
        print(f"\nDesvio Padrão:")
        print(f"Peso: {df['Peso'].std()}, Altura: {df['Altura'].std()}, IMC: {df['IMC'].std()}")
        print(f"\nQuantis:")
        print(
            f"Peso:\n {df['Peso'].quantile([0.25, 0.5, 0.75])}, \nAltura:\n {df['Altura'].quantile([0.25, 0.5, 0.75])}, \nIMC:\n {df['IMC'].quantile([0.25, 0.5, 0.75])}")


print(f"""\033[1m Digite: 
    1 para INSERIR novos dados.
    2 para LISTAR os dados salvos.
    3 para DESEMPILHAR os dados salvos.
    4 para APAGAR todos os dados salvos.
    5 para DADOS ESTATÍSTICOS dos dados salvos.
    \033[0m""")

option = input(f'\nDigite sua opção: ')

while option != 9:
    if option == '1':
        try:
            nome = str(input("\nDigite o seu Nome: "))
            peso = float(input("\nDigite o seu peso em quilogramas: "))
            altura = float(input("\nDigite a sua altura em metros: "))
            imc = calcular_imc(peso, altura)
            print("\nO seu IMC é: \n", imc)
            salvar = input('\nSalvar dados? s/n: ')
            while str() in salvar:
                if 's' in salvar:
                    salvar_dados(nome, peso, altura)
                    break
                elif 'S' in salvar:
                    salvar_dados(nome, peso, altura)
                    break
                if 'n' in salvar:
                    break
                elif 'N' in salvar:
                    break
                else:
                    print("Opção inválida. Por favor, tente novamente.")
                    salvar = input('\nSalvar dados? s/n: ')
        except:
            print('Erro de Sintaxe, tente novamente!')
            pass
    elif option == '2':
        try:
            listar_dados()
        except:
            pass
    elif option == '3':
        try:
            desempilhar_dados()
        except:
            pass
    elif option == '4':
        try:
            apagar_dados()
        except:
            pass
    elif option == '5':
        try:
            plot_histograma_dispersao_estatisticas()
        except:
            pass
    elif option == '9':
        print(f'ENCERRANDO PROGRAMA')
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")

    print(f"""\033[1m Digite: 
        1 para INSERIR novos dados.
        2 para LISTAR os dados registrados.
        3 para DELETAR os dados salvos.
        4 para APAGAR todos os dados salvos.
        5 para DADOS ESTATÍSTICOS dos dados salvos.
        ou 9 para SAIR.
        \033[0m""")

    option = input(f'\nDigite sua opção: ')
