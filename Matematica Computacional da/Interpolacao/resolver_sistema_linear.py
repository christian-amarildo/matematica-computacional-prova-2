import numpy as np

def resolver_sistema_linear(A, b):
    """
    Resolve o sistema linear Ax = b usando eliminação de Gauss e substituição regressiva.

    Parâmetros:
    A (numpy.ndarray): Matriz quadrada dos coeficientes.
    b (numpy.ndarray): Vetor dos termos independentes.

    Retorna:
    numpy.ndarray: Vetor solução x.
    """
    A = A.astype(float)  # Garantir que a matriz seja de ponto flutuante
    b = b.astype(float)
    n = len(b)

    # Eliminação de Gauss
    for i in range(n):
        # Pivoteamento parcial (troca de linhas se necessário)
        max_row = np.argmax(np.abs(A[i:, i])) + i
        if A[max_row, i] == 0:
            raise ValueError("Sistema sem solução ou com infinitas soluções.")

        # Troca de linha se necessário
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]

        # Eliminação
        for j in range(i+1, n):
            fator = A[j, i] / A[i, i]
            A[j, i:] -= fator * A[i, i:]
            b[j] -= fator * b[i]

    # Substituição regressiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x
