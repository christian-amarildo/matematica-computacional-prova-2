
import numpy as np


def ler_matriz_de_arquivo():
    with open("seu_arquivo.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    n = int(linhas[0].strip())  # Número de linhas da matriz
    matriz = []
    
    for linha in linhas[1:]:
        elementos = list(map(float, linha.split()))
        matriz.append(elementos)

    return n, matriz



def gauss_seidel(matriz, b, epsilon=1e-5, max_iter=100):
    n = len(matriz)
    x = np.zeros(n)
    diferenca_relativa = np.inf
    iteracao = 0
    
    while diferenca_relativa > epsilon and iteracao < max_iter:
        x_antigo = np.copy(x)
        
        for i in range(n):
            soma = sum(matriz[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - soma) / matriz[i][i]
        
        diferenca_relativa = np.max(np.abs(x - x_antigo) / np.abs(x))
        iteracao += 1

    if iteracao == max_iter:
        return None
    else:
        return x



def jacobi(matriz, b, epsilon=1e-5, max_iter=100):
    n = len(matriz)
    x = np.zeros(n)
    x_antigo = np.zeros(n)
    diferenca_relativa = np.inf
    iteracao = 0

    while diferenca_relativa > epsilon and iteracao < max_iter:
        for i in range(n):
            soma = sum(matriz[i][j] * x_antigo[j] for j in range(n) if j != i)
            x[i] = (b[i] - soma) / matriz[i][i]

        diferenca_relativa = np.max(np.abs(x - x_antigo) / np.abs(x))
        x_antigo = np.copy(x)
        iteracao += 1

    if iteracao == max_iter:
        return None
    else:
        return x





n, matriz = ler_matriz_de_arquivo()

A = np.array([linha[:n] for linha in matriz])
b = np.array([linha[n] for linha in matriz])

print("Matriz original:")
for linha in matriz:
    print(" ".join(map(str, linha)))

# Matriz condicionada (A deve ser diagonalmente dominante para convergência)
A_condicionada = A + np.diag(np.sum(np.abs(A), axis=1) * 0.5)

print("\nMatriz condicionada:")
for linha in A_condicionada:
    print(" ".join(map(str, linha)))

# Vetor inicial
x_inicial = np.zeros(n)
print("\nVetor inicial:")
print(x_inicial)

# Gauss-Seidel
print("\nValores sucessivos do vetor x (Gauss-Seidel):")
solucao_gauss_seidel = gauss_seidel(A_condicionada, b)
if solucao_gauss_seidel is not None:
    for valor in solucao_gauss_seidel:
        print(valor)
    print("\nVetor solução (Gauss-Seidel):")
    print(solucao_gauss_seidel)
else:
    print("\nO método de Gauss-Seidel falhou.")

# Jacobi
print("\nValores sucessivos do vetor x (Jacobi):")
solucao_jacobi = jacobi(A_condicionada, b)
if solucao_jacobi is not None:
    for valor in solucao_jacobi:
        print(valor)
    print("\nVetor solução (Jacobi):")
    print(solucao_jacobi)
else:
    print("\nO método de Jacobi falhou.")
