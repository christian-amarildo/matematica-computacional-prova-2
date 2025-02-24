import numpy as np


A = np.array([[10, 2, 1],
             [1, 5, 1],
             [2, 3, 10]])

b = np.array([7, -8, 6])

x = [0, 0, 0]

def gauss_jacobi(A: list, b: list, x: list, erro: float, max_iter: int):
    linha, coluna = A.shape
    H = np.zeros((linha, coluna))
    g = np.zeros(coluna)


    for i in range(0, linha):
        H[i, :] = -A[i,:]/A[i, i]
        g[i] = b[i]/A[i, i]
        H[i, i] = 0

    k = 0
    e = 1
    while e > erro and k < max_iter:
        xk = np.dot(H, x) + g
        dif = xk - x
        maxd = max(min(dif), max(dif, key=abs))
        maxxk = max(min(xk), max(xk, key=abs))
        e = abs(maxd)/abs(maxxk)
        k += 1
        x = xk
    
    return x

x = gauss_jacobi(A, b, x, 0.1, 30)
print(x)