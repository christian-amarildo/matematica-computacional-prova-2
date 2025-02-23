import numpy as np

def decomposicao_LU_pivot(A):
    """
    Realiza a decomposição LU com pivoteamento parcial.
    
    Parâmetros:
    A : np.array
        Matriz quadrada de coeficientes do sistema.

    Retorno:
    P, L, U : np.array, np.array, np.array
        Matrizes de permutação, triangular inferior e triangular superior, respectivamente.
    """
    n = len(A)
    P = np.eye(n)  # Matriz identidade para armazenar permutações
    L = np.eye(n)  # Matriz triangular inferior inicializada como identidade
    U = A.astype(float)  # Copia de A para iniciar U

    for k in range(n):
        # Pivoteamento parcial
        pivot = np.argmax(np.abs(U[k:, k])) + k
        if pivot != k:
            U[[k, pivot]] = U[[pivot, k]]  # Troca linhas em U
            P[[k, pivot]] = P[[pivot, k]]  # Troca linhas em P
            if k > 0:
                L[[k, pivot], :k] = L[[pivot, k], :k]  # Troca linhas em L

        # Eliminação para criar matriz triangular inferior e superior
        for i in range(k+1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    return P, L, U

def resolver_sistema_LU(A, b):
    """
    Resolve o sistema Ax = b usando decomposição LU com pivoteamento parcial.
    
    Parâmetros:
    A : np.array
        Matriz quadrada de coeficientes do sistema.
    b : np.array
        Vetor de termos independentes.

    Retorno:
    x : np.array
        Solução do sistema.
    """
    P, L, U = decomposicao_LU_pivot(A)
    
    # Resolver Pb = L(Ux) = b
    b_modificado = np.dot(P, b)

    # Resolução de Ly = Pb (substituição direta)
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b_modificado[i] - np.dot(L[i, :i], y[:i])

    # Resolução de Ux = y (substituição retroativa)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x

