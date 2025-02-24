import numpy as np
import matplotlib.pyplot as plt

def eliminacao(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(A)

    # Eliminação para transformar a matriz em triangular superior
    for k in range(n):
        for i in range(k+1, n):
            if A[k, k] == 0:
                raise ValueError("Matriz singular, não é possível continuar.")
            m = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] -= m * A[k, j]
            b[i] -= m * b[k]
    
    return A, b

def resolucao_sistema(A, b):
    n = len(A)
    x = np.zeros(n)
    
    x[n-1] = b[n-1] / A[n-1, n-1]
    for k in range(n-2, -1, -1):
        s = sum(A[k, j] * x[j] for j in range(k+1, n))
        x[k] = (b[k] - s) / A[k, k]
    
    return x

def vandermonde(x_points):
    n = len(x_points)
    V = np.vander(x_points, increasing=True)
    return V

# Pontos de interpolação
x_points = np.array([0, 1, 2, 3])
y_points = np.array([0, 1, 4, 9])

# Criando a matriz de Vandermonde
V = vandermonde(x_points)

# Resolvendo o sistema para encontrar coeficientes do polinômio
A_tri, b_tri = eliminacao(V.copy(), y_points.copy())
coeficientes = resolucao_sistema(A_tri, b_tri)

# Criando o polinômio
p = np.poly1d(coeficientes[::-1])  # Invertendo para usar corretamente no poly1d

# Plotando os pontos e o polinômio
x_range = np.linspace(min(x_points) - 1, max(x_points) + 1, 100)
y_range = p(x_range)

plt.scatter(x_points, y_points, color='red', label='Pontos de interpolação')
plt.plot(x_range, y_range, label='Polinômio interpolador')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolação usando a matriz de Vandermonde')
plt.grid()
plt.show()
