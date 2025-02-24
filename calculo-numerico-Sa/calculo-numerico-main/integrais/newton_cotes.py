import numpy as np

from interpolacao.lagrange import lagrange


def newton_cotes_integral(X, Y, a, b, div=100):
    x_divisions = np.linspace(a, b, div)
    h = (b - a) / (div - 1)  # Espaçamento entre os pontos
    integral = 0
    
    for i, x in enumerate(x_divisions):
        weight = 2 if (i != 0 and i != div - 1) else 1  # Peso 1 nos extremos, 2 nos intermediários (Regra dos Trapézios)
        integral += weight * lagrange(X, Y, x)
    
    integral *= h / 2  # Ajuste final para a regra dos trapézios
    return integral
