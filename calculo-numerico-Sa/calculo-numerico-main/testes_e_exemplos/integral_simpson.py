from ajuste_de_curva.minimos_quadrados_nao_linear import get_A, get_B
from solucoes_matriciais.fatoracao_lu import resolver_sistema_lu
from integrais.simpson import simpson
from plot.plot_simpson import plot


### EXEMPLO DE USO ###
def f(x):
    return coefs[0]*x**2 + coefs[1]*x + coefs[2]

X = [1, 3, 5]
Y = [5, 12, 9]

g_list = [lambda x: x**2, lambda x: x, lambda x: x**0]

A = get_A(X, g_list)
b = get_B(X, Y, g_list)
coefs = resolver_sistema_lu(A, b)
print("coefs: ", coefs)

a, b = 1, 5 # Intervalo de integração

integral = simpson(f, a, b)

plot(X, Y, 0, 6, integral, "Regra de Simpson")
