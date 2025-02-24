def get_A(X: list, functions: list):
    matriz = []
    m = len(X)
    n = len(functions)

    for i in range(n):
        linhas = []
        for j in range(n):
            a = 0
            for k in range(m):
                g_i = functions[i]
                g_j = functions[j]
                a += g_i(X[k]) * g_j(X[k])
            
            linhas.append(a)
        matriz.append(linhas)
    
    for linha in matriz:
        print(linha)

    return matriz


def get_B(X, Y, functions):
    n = len(functions)
    B = [0] * n
    m = len(X)

    for i in range(n):
        soma = 0
        for k in range(m):
            g_i = functions[i]
            soma += Y[k] * g_i(X[k])
        B[i] = soma

    return B


def minimos_quadrados_nao_lineares(X: list, Y: list, functions: list, solver) -> list:
    A = get_A(X, functions)
    b = get_B(X, Y, functions)
    coefs = solver(A, b)
    print("coefs: ", coefs)
    return coefs
