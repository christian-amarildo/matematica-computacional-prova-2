# V

def fatoracao_LU(A, b):
    n = len(A)

    # Verificação se a matriz é quadrada
    for row in A:
        if len(row) != n:
            raise ValueError("A matriz deve ser quadrada")
    
    # Inicializando L e U
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    # Decomposição LU (Eliminação de Gauss)
    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        for j in range(i, n):
            if i == j:
                L[i][i] = 1
            else:
                L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    # Substituição para frente: Resolver Ly = b
    y = [0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    # Substituição para trás: Resolver Ux = y
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if U[i][i] == 0:
            raise ValueError("Sistema não tem solução única (divisão por zero detectada).")
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return x  # Retorna o vetor solução

# Exemplo:
A = [
    [4, 3],
    [6, 3]
]
b = [10, 12]

x = fatoracao_LU(A, b)
print("Solução:", x)
