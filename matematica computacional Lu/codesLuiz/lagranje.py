import numpy as np
import matplotlib.pyplot as plt

def lagrange_basis(x, pontos_x, k):
    n = len(pontos_x)
    L = 1
    for j in range(n):
        if j != k:
            L *= (x - pontos_x[j]) / (pontos_x[k] - pontos_x[j])
    return L

def interpolacao_lagrange(pontos_x, pontos_y):
    def polinomio(x):
        soma = 0
        for k in range(len(pontos_x)):
            soma += pontos_y[k] * lagrange_basis(x, pontos_x, k)
        return soma
    return polinomio

# exemplo polinomio definido por usuario
pontos_x = [-1, 0, 2]
pontos_y = [4, 1, -1]

polinomio = interpolacao_lagrange(pontos_x, pontos_y)

x_vals = np.linspace(min(pontos_x) - 1, max(pontos_x) + 1, 400)
y_vals = [polinomio(x) for x in x_vals]

plt.plot(x_vals, y_vals, label='Polinômio de Lagrange')
plt.scatter(pontos_x, pontos_y, color='green', label='pontos conhecidos')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('interpolação lagrange')
plt.show()