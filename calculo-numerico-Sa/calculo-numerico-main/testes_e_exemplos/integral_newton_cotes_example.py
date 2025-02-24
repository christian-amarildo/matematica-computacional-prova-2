from integrais.newton_cotes import newton_cotes_integral
from plot.plot_newton_cotes import plot


### EXEMPLO DE USO ###
X = [1, 1.3, 2] # A quantidade de elementos define a quantidade de Lj(x) (maior precisão...)
Y = [1/x for x in X]

a, b = 1, 2  # Intervalo de integração

plot(X, Y, newton_cotes_integral, a, b, "Newton-Cotes")
