import numpy as np

from solucoes_matriciais.fatoracao_lu import resolver_sistema_lu
from ajuste_de_curva.linearizar import ajustar_valores
from ajuste_de_curva.minimos_quadrados_nao_linear import minimos_quadrados_nao_lineares
from plot.plot import plot


### EXEMPLO DE USO ###

## Exemplo exponencial ## -------------------------------------------------
# def f(x):
#     return coefs[1]*np.exp(coefs[0]*x) # função real, sem tirar nem pôr

# X = [-1, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1]
# Y = [36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246]

# Y_ajustado = Y.copy()
# Y_ajustado = ajustar_valores(Y_ajustado, lambda y: np.log(y))
# # ajuste de valores em Y (se ajustar, passar o Y_ajustado como parâmetro)

# g_list = [lambda x: np.exp(x), lambda x: x**0] # se a função é b*e^(a*x), então são necessários dois coeficientes
# coefs = minimos_quadrados_nao_lineares(X, Y_ajustado, g_list, resolver_sistema_lu)
# plot(X, Y, f, a=-2, b=2, label="MMQ - Exponencial") # Modificar valores de a e b conforme mín e máx de X

# -------------------------------------------------------------------------

## Exemplo linear ## ------------------------------------------------------
# def f(x):
#     return coefs[1] + coefs[0]*x

# X = [x for x in range(1, 9)]
# Y = [0.5, 0.6, 0.9, 0.8, 1.2, 1.5, 1.7, 2]

# g_list = [lambda x: x, lambda x: 1]
# coefs = minimos_quadrados_nao_lineares(X, Y, g_list, resolver_sistema_lu)
# plot(X, Y, f, a=0, b=9, label="MMQ - Linear") # Modificar valores de a e b conforme mín e máx de X

# -------------------------------------------------------------------------

## Exemplo quadrático ## --------------------------------------------------
# def f(x):
#     return coefs[0]*x**2 + coefs[1]*x + coefs[2]

# X = [-1, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1]
# Y = [2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]

# g_list = [lambda x: x**2, lambda x: x, lambda x: x**0]
# coefs = minimos_quadrados_nao_lineares(X, Y, g_list, resolver_sistema_lu)
# plot(X, Y, f, a=-2, b=2, label="MMQ - Quadrática") # Modificar valores de a e b conforme mín e máx de X

# -------------------------------------------------------------------------
