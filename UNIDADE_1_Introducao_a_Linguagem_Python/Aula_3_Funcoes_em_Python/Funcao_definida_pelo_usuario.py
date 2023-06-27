# In [2]
# def nome_funcao():
# bloco de comandos


# In[3]
def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}.")

imprimir_mensagem("Python", "ADS")
print()
print('==============================================================================================================')

#In[4]
def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}.")

resultado = imprimir_mensagem("Python", "ADS")
print(f"Resultado = {resultado}")
print()
print('==============================================================================================================')


"""
Para que o resultado de uma função possa ser guardado em uma variável, a função precisa ter o comando "return". 
A instrução "return", retorna um valor de uma função. Veja a nova versão da função "imprimir_mensagem", agora, 
em vez de imprimir a mensagem, ela retorna a mensagem para chamada.
"""
# In[5]
def imprimir_mensagem(disciplina, curso):
    return f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}."

mensagem = imprimir_mensagem("Python", "ADS")
print(mensagem)
print()
print('==============================================================================================================')


"""
Vamos implementar uma função que recebe uma data no formato dd/mm/aaaa e converte o mês para extenso. 
Então, ao se receber a data 10/05/2020, a função deverá retornar: 10 de maio de 2020.
"""
# In[6]
def converter_mes_para_extenso(data):   # Definimos o nome da função e os parâmetros que ela recebe.
    mes = '''janeiro fevereiro março
      abril maio junho julho agosto
      setembro outubro novembro
      dezembro'''.split()   # Criamos uma lista com os meses, por extenso.
                            # Veja que criamos uma string e usamos a função split(),
                            #  que "quebra" a string a cada espaço em branco,
                            # criando uma lista e elementos.
    d, m, a = data.split('/')   # Usamos novamente a função split(), mas agora passando como parâmetro o caractere '/',
                                # isso quer dizer que a string será cortada sempre que ele aparecer.
    mes_extenso = mes[int(m) - 1]   # Aqui estamos fazendo a conversão do mês para extenso.
                                    # Veja que buscamos na lista "mes" a posição m - 1, pois, a posição inicia em 0.
                                    # Por exemplo, para o mês 5, o valor "maio", estará na quarta posição a lista "mes".
    return f'{d} de {mes_extenso} de {a}'   # Retornamos a mensagem, agora com o mês em extenso.

print(converter_mes_para_extenso('10/05/2021')) # Invocamos a função, passando como parâmetro a data a ser convertida.