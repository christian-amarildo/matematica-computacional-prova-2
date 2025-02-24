# V V V

def eliminacao(A, b):
    n = len(A)

    # Eliminação para transformar a matriz em triangular superior
    for k in range(n):
        for i in range(k+1, n):
            if A[k][k] == 0:
                raise ValueError("Matriz singular, não é possível continuar.")
            m = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= m * A[k][j]
            b[i] -= m * b[k]
    
    return A, b

def resolucao_sistema(A, b):
    n = len(A)
    x = [0] * n

    x[n-1] = b[n-1] / A[n-1][n-1]
    for k in range(n-2, -1, -1):
        s = 0
        for j in range(k+1, n):
            s += A[k][j] * x[j]
        x[k] = (b[k] - s) / A[k][k]

    return x

# Exemplo:
A = [
    [1, 1, 0, 3],
    [2, 1, -1, 1],
    [3, -1, -1, 2],
    [-1, 2, 3, -1]
]

b = [4, 1, -3, 4]

# Passo 1: Eliminação de Gauss
A, b = eliminacao(A, b)

# Passo 2: Substituição retroativa
x = resolucao_sistema(A, b)

print(x)
