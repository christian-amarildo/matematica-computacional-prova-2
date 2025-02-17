import numpy as np

def fatoracao_lu_com_pivoteamento_parcial(A):
    """
    Realiza a fatoração LU com pivoteamento parcial.

    Parâmetros:
        A (numpy.ndarray): Matriz quadrada de dimensão n x n.

    Retorna:
        P (numpy.ndarray): Matriz de permutação.
        L (numpy.ndarray): Matriz triangular inferior.
        U (numpy.ndarray): Matriz triangular superior.
    """
    n = A.shape[0]
    P = np.eye(n)  # Cria uma matriz identidade de dimensão n x n para representar a matriz de permutação.
    L = np.zeros_like(A, dtype=float)  # Inicializa a matriz L com zeros, mantendo o mesmo formato de A.
    U = A.copy().astype(float)  # Faz uma cópia da matriz A e a converte para o tipo float.

    for k in range(n):
        # Pivoteamento parcial
        linha_max = k + np.argmax(np.abs(U[k:, k]))  # Encontra o índice da linha com o maior valor absoluto na coluna k.
        if linha_max != k:
            # Troca as linhas em U
            U[[k, linha_max]] = U[[linha_max, k]]  # Troca as linhas k e linha_max na matriz U.
            # Troca as linhas em P
            P[[k, linha_max]] = P[[linha_max, k]]  # Troca as linhas k e linha_max na matriz de permutação P.
            # Troca as linhas em L (até a coluna k-1)
            if k > 0:
                L[[k, linha_max], :k] = L[[linha_max, k], :k]  # Troca as primeiras k-1 colunas entre as linhas k e linha_max em L.

        # Eliminação
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]  # Calcula o multiplicador para a linha i e coluna k.
            U[i, k:] -= L[i, k] * U[k, k:]  # Subtrai a linha k escalonada da linha i em U.

    np.fill_diagonal(L, 1)  # Preenche a diagonal principal de L com 1.
    return P, L, U

def resolver_com_lu(P, L, U, b):
    """
    Resolve o sistema linear Ax = b usando a fatoração LU e a matriz de permutação P.

    Parâmetros:
        P (numpy.ndarray): Matriz de permutação.
        L (numpy.ndarray): Matriz triangular inferior.
        U (numpy.ndarray): Matriz triangular superior.
        b (numpy.ndarray): Vetor de termos independentes.

    Retorna:
        x (numpy.ndarray): Solução do sistema.
    """
    # Ajusta b usando a matriz de permutação
    b_ajustado = np.dot(P, b)  # Multiplica P por b para ajustar os termos independentes conforme as trocas de linhas.

    # Substituição direta para resolver L * y = b_ajustado
    n = L.shape[0]
    y = np.zeros_like(b, dtype=float)  # Inicializa o vetor y com zeros, do mesmo formato que b.
    for i in range(n):
        y[i] = b_ajustado[i] - np.dot(L[i, :i], y[:i])  # Calcula y[i] subtraindo os produtos já calculados das colunas anteriores.

    # Substituição retroativa para resolver U * x = y
    x = np.zeros_like(b, dtype=float)  # Inicializa o vetor x com zeros, do mesmo formato que b.
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]  # Calcula x[i] resolvendo para a variável correspondente.

    return x

# Exemplo de uso
def escalonamento_por_FatLU(M):
    A = np.array(M[:,:-1])  # Define a matriz A.
    b = np.array(M[:,-1])  # Define o vetor de termos independentes b.
    P, L, U = fatoracao_lu_com_pivoteamento_parcial(A)

    print("Matriz P:")
    print(P)
    print("\nMatriz L:")
    print(L)
    print("\nMatriz U:")
    print(U)

    # Resolver o sistema linear
    x = resolver_com_lu(P, L, U, b)
    print("\nSolução x:")
    print(x)

    
if __name__ == "__main__":
    A = np.array([
        [2, 1, -1,8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3]
       ])
    escalonamento_por_FatLU(A)

    # # Fatoração LU com pivoteamento parcial
    