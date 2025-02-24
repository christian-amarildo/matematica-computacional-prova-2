import numpy as np

from ajuste_de_curva.gauss_newton import gauss_newton
from plot.plot import plot


### EXEMPLO DE USO ###
## Exemplo exponencial ##
# def funcao_modelo(x, alpha1, alpha2):
#     return alpha1 * np.exp(-alpha2 * x)
#
#
# def f(x):
#     return coefs[0]*np.exp(coefs[1]*x)
#
#
# X = np.array([-1, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1])
# Y = np.array([36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246])


def funcao_modelo(x, a, b):
    return a*x + b


def f(x):
    return coefs[0]*x + coefs[1]


X = np.array([1, 3, 4])
Y = np.array([3, 7, 9])

# Chutes iniciais para os coeficientes (α₁, α₂)
chutes_iniciais = [1, 1] # Se a função modelo precisar de mais alphas, é só adicionar. Ex. [1, 1, 1]

# Resolver o sistema usando o método de Gauss-Newton
coefs = gauss_newton(chutes_iniciais, X, Y, funcao_modelo, max_iter=100)

plot(X, Y, f, -5, 5, "Gauss-Newton")
