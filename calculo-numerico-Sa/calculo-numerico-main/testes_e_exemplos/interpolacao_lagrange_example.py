from interpolacao.lagrange import lagrange
from plot.plot import plot


### EXEMPLO DE USO ###
def f(x):
    return lagrange(X, Y, x)


# X = [1, 2, 3]
# Y = [0, 1, 4]
X = [-2, 0, 1, 2]
Y = [-47, -3, 0, 41]

plot(X, Y, f, -3, 3, "Interpolação de Lagrange")
