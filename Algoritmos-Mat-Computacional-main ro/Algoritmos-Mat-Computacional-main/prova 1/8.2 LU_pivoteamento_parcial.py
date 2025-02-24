# V

def lu_decomposition_with_pivoting(A, b):
    n = len(A)

    # Inicialização dos vetores
    p = list(range(n))

    # Decomposição LU com pivotamento
    for k in range(n - 1):
        # Encontra o pivô
        pv = abs(A[k][k])
        r = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > pv:
                pv = abs(A[i][k])
                r = i

        if pv == 0:
            raise ValueError("A matriz A é singular.")

        # Troca as linhas caso necessário
        if r != k:
            p[k], p[r] = p[r], p[k]
            A[k], A[r] = A[r], A[k]

        # Atualização da matriz A
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            A[i][k] = m
            for j in range(k + 1, n):
                A[i][j] -= m * A[k][j]

    # Substituição de Pb
    c = [0] * n
    for i in range(n):
        r = p[i]
        c[i] = b[r]

    # Substituição direta Ly = c
    y = [0] * n
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += A[i][j] * y[j]
        y[i] = c[i] - soma

    # Substituição retroativa Ux = y
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += A[i][j] * x[j]
        x[i] = (y[i] - soma) / A[i][i]

    return x

# Exemplo de uso:
A = [[2, -1, -2],
     [-4, 6, 3],
     [-4, -2, 8]]
b = [1, 2, 3]

x = lu_decomposition_with_pivoting(A, b)
print("Solução:", x)
