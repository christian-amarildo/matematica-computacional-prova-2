import matplotlib.pyplot as plt
import numpy as np


def ajuste_linear_manual(x, y):
    """
    Calcula o ajuste linear da forma y = ax + b usando Mínimos Quadrados,
    sem usar bibliotecas como NumPy.
    """
    n = len(x)

    # Cálculo das somas necessárias
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = sum(x[i] * y[i] for i in range(n))
    soma_x2 = sum(x[i]**2 for i in range(n))

    # Cálculo de 'a' e 'b'
    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
    b = (soma_y - a * soma_x) / n

    return a, b


# Teste com gráfico
x = [1, 2, 3, 4]
y = [2.1, 2.9, 3.8, 5.1]
a, b = ajuste_linear_manual(x, y)

# Criando a linha ajustada
xp = np.linspace(min(x), max(x), 100)
yp = [a * xi + b for xi in xp]

plt.scatter(x, y, color='red', label="Pontos Dados")
plt.plot(xp, yp, color='blue', label=f"Ajuste Linear: y = {a:.2f}x + {b:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.title("Ajuste Linear - Mínimos Quadrados")
plt.show()
