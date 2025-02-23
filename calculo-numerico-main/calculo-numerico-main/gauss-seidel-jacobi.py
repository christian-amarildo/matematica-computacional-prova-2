
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


def testa_se_diagonalmente_dominante(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        # soma_abs recebe a soma do valor absoluto de todas as posições exceto diagonal principal 
        soma_abs = sum(abs(matriz[i][j]) for j in range(colunas) if j != i)
        if abs(matriz[i][i]) <= soma_abs:
            return False

    return True


def gauss_seidel(matriz, b, x0, epsilon=1e-5, max_iter=100):

    if (testa_se_diagonalmente_dominante(matriz) == False):
        print("Não possui diagonal dominante")
        return None
    
    n = len(matriz)
    x = x0.copy()
    
    iteracoes = 0
    while iteracoes < max_iter:
        iteracoes += 1
        x_antigo = x.copy()

        for lin in range(n):
            soma = 0
            for col in range(n):
                if col != lin:
                    soma += matriz[lin][col] * x[col] / matriz[lin][lin]
                    
                x[lin] = (b[lin] / matriz[lin][lin]) - soma

        # Cálculo da diferença relativa em norma infinito
        diff_rel = max(abs(x[i] - x_antigo[i]) / abs(x[i]) for i in range(n))
        
        print(iteracoes, x_antigo, '    \t', diff_rel)
        if diff_rel < epsilon:
            return x
        
    return None  # Falha


def gauss_jacobi(matriz, b, x0, epsilon=1e-5, max_iter=100):

    if (testa_se_diagonalmente_dominante(matriz) == False):
        print("Não possui diagonal dominante")
        return None
    
    n = len(matriz)
    x = x0.copy()
    
    iteracoes = 0
    while iteracoes < max_iter:
        iteracoes += 1
        x_antigo = x.copy()

        for lin in range(n):
            soma = 0
            for col in range(n):
                if col != lin:
                    soma += matriz[lin][col] * x_antigo[col] / matriz[lin][lin]
                    
                x[lin] = (b[lin] / matriz[lin][lin]) - soma

        # Cálculo da diferença relativa em norma infinito
        diff_rel = max(abs(x[i] - x_antigo[i]) / abs(x[i]) for i in range(n))
        
        print(iteracoes, x_antigo, '    \t', diff_rel)
        if diff_rel < epsilon:
            return x
        
    return None  # Falha




n, matriz = ler_matriz_de_arquivo()

print("Matriz original:")
imprimir_matriz(matriz)

# Separa a matriz dos termos independentes
A = [[matriz[i][j] for j in range(n)] for i in range(n)]
B = [matriz[i][n] for i in range(n)]

# Define o vetor inicial
x0 = [0] * n

# Ax = b
print("\nMatriz A:")
imprimir_matriz(A)

print("\nVetor inicial:")
print(x0)

# Resolve pelo método de Gauss-Seidel
solucao_gauss_seidel = gauss_seidel(A, B, x0)

if solucao_gauss_seidel:
    print("\nSolução pelo método de Gauss-Seidel:")
    print(solucao_gauss_seidel)
else:
    print("\nFalha ao encontrar a solução pelo método de Gauss-Seidel.")

# Resolve pelo método de Jacobi
solucao_jacobi = gauss_jacobi(A, B, x0)

if solucao_jacobi:
    print("\nSolução pelo método de Jacobi:")
    print(solucao_jacobi)
else:
    print("\nFalha ao encontrar a solução pelo método de Jacobi.")
