
def ler_matriz_de_arquivo():
    with open("entrada.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    n = int(linhas[0])  # Número de linhas da matriz
    matriz = []

    for i in range(1, n + 1):
        elementos = list(map(float, linhas[i].split()))
        matriz.append(elementos)
    
    return n, matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        print("\t".join(map(str, linha)))


def pivotear_matriz(matriz):
    n = len(matriz)
    
    for k in range(n):
        # Pivoteamento
        max_element = abs(matriz[k][k])
        max_row = k

        for i in range(k, n):
            if abs(matriz[i][k]) > max_element:
                max_element = abs(matriz[i][k])
                max_row = i

        # Faz a troca de posição
        if max_row != k:
            temp = matriz[k]
            matriz[k] = matriz[max_row]
            matriz[max_row] = temp

    
    return matriz

def eliminacao_gauss(matriz):
    n = len(matriz)

    print('eliminacao_gauss')
    imprimir_matriz(matriz)

    # Eliminação Gauss
    for k in range(n - 1):
        for i in range(k + 1, n):
            fator = matriz[i][k] / matriz[k][k]
            for j in range(k, n + 1):
                matriz[i][j] -= fator * matriz[k][j]
    
    # Verifica se a matriz é singular
    for i in range(n):
        if matriz[i][i] == 0:
            return None
    
    # Resolução do sistema por retrosubstituição
    # criando array x com a quantidade de elementos n
    x = [0] * n

    # loop for de n-1 até valor -1, indo de -1 em -1
    for i in range(n - 1, -1, -1):
        x[i] = matriz[i][n] / matriz[i][i]
        for j in range(i - 1, -1, -1):
            matriz[j][n] -= matriz[j][i] * x[i]
    
    return x




n, matriz = ler_matriz_de_arquivo()

print("Matriz original:")
imprimir_matriz(matriz)


matriz_pivoteada = pivotear_matriz(matriz)
solucao = eliminacao_gauss(matriz_pivoteada)


if solucao:
    print("\nMatriz pivoteada:")
    imprimir_matriz(matriz_pivoteada)
    
    print("\nVetor de solução:", solucao)
else:
    print("\nA matriz é singular. Não há solução.")
