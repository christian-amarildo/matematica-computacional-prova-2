import numpy as np
import matplotlib.pyplot as plt

def ajuste_minimos_quadrados(x, y, grau):

    coeficientes = np.polyfit(x, y, grau)
    return coeficientes

def plot_ajuste(x, y, coeficientes):

    plt.scatter(x, y, color='green', label='Pontos Originais')
    x_novo = np.linspace(min(x), max(x), 100)
    y_ajustado = np.polyval(coeficientes, x_novo)
    plt.plot(x_novo, y_ajustado, label='curva Ajustada', color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# exemplo polinomio definido por usuario
x = np.array([])
y = np.array([])
grau = 2 

coef = ajuste_minimos_quadrados(x, y, grau)
print("coeficientes do polinômio ajustado:", coef)
plot_ajuste(x, y, coef)