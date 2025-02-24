import numpy as np
import matplotlib.pyplot as plt

def interpolacao_sistema_linear(x, y):
    n = len(x)
    A = np.vander(x, n)
    coeficientes = np.linalg.solve(A, y)
    return np.poly1d(coeficientes)

# exemplo polinomio definido por usuario
x = [-1, 0, 2]
y = [4, 1, -1]

polinomio = interpolacao_sistema_linear(x, y)

x_vals = np.linspace(min(x) - 1, max(x) + 1, 400)
y_vals = polinomio(x)

plt.plot(x_vals, y_vals, label=f'oolinômio: {polinomio}')
plt.scatter(x, y, color='red', label='Pontos conhecidos')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('Interpolação Polinomial - Sistema Linear')
plt.show()