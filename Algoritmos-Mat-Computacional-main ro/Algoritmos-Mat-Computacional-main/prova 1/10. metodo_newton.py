# V

def eliminacao_gauss(A, b):
    # A: matriz dos coeficientes
    # b: vetor dos termos independentes

    n = len(b)

    # Eliminação direta
    for i in range(n):
        # Escolha do pivô
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if max_row != i:
            # Troca de linhas na matriz A
            A[i], A[max_row] = A[max_row], A[i]
            # Troca no vetor b
            b[i], b[max_row] = b[max_row], b[i]

        # Garantir que o pivô não é zero
        if A[i][i] == 0:
            raise ValueError("A matriz é singular e não pode ser resolvida.")

        # Eliminação das entradas abaixo do pivô
        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]
            A[j][i] = 0  # Já definimos o elemento como 0 para clareza

            for k in range(i + 1, n):
                A[j][k] -= fator * A[i][k]
            
            b[j] -= fator * b[i]

    # Substituição reversa
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = b[i]
        for j in range(i + 1, n):
            soma -= A[i][j] * x[j]
        x[i] = soma / A[i][i]

    return x 

# Exemplo:
x1, x2 = None, None

A = [x1 + x2 - 3, x1**2 + x2**2 - 9]

J = [[1, 1], [2*x1, 2*x2]]