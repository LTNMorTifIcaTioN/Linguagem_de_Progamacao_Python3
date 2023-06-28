"""
A complexidade assintótica é definida pelo crescimento da complexidade para entradas suficientemente grandes.
Por exemplo, vamos supor que a função f(n) = an2 + bn + c (função do segundo grau)
é a função de tempo de um determinado algoritmo. Para expressar sua complexidade,
identifica-se qual é o termo dominante (nesse caso, o parâmetro com maior crescimento é n2).
Ignoram-se os termos de ordem inferior (nesse caso n) e ignoram-se as constantes (a, b, c), razão pela qual ficamos,
então, com a função f(n) = n2. Portanto,
a função de complexidade para esse algoritmo é denotada pela notação assintótica O(n2), chamada de Big-Oh (Grande-O).
"""

print('EXEMPLIFICANDO')
def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False
# f(N) = 1 * N, logo: O(N);

"""
Outras complexidades que são comumente encontradas são: O(log N), O(N2), O(N3). Vale ressaltar que,
em termos de eficiência, teremos que: O(1) < O(log N) < O(N) < O(N2) < O(N3) < O(2N), ou seja,
um algoritmo com complexidade O(N) é mais eficiente que O(N2).
"""