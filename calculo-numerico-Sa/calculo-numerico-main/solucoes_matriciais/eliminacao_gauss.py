def get_A_gauss(A: list, b: list):
    n = len(b) - 1 # b tem tamanho n, mas começamos em 0, logo, len(b) - 1 = n - 1
    for j in range(n):
        for i in range(j+1, n+1):
            m = A[i][j]/A[j][j]
            A[i][j] = 0
            for k in range(j+1, n+1):
                A[i][k] -= m*A[j][k]
            b[i] -= m*b[j]

    return A


def gauss(A: list, b: list):
    A = get_A_gauss(A, b)
    n = len(b) - 1
    x = []
    for i in range(n + 1):
        x.append(None)
    

    x[n] = b[n]/A[n][n]
    for k in range(n, -1, -1):
        s = 0
        for j in range(k+1, n+1):
            s += A[k][j] * x[j]
            x[k] = (b[k] - s)/A[k][k]
    return x
