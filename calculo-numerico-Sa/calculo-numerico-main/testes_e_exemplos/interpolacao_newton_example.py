from interpolacao.newton import newton, newton_coeficients
from plot.plot import plot


### EXEMPLO DE USO ###
def f(x):
    return newton(x, coef_in_first_line, X)


X = [-2, 0, 1]
Y = [2, 1, 3]

matrix = newton_coeficients(X, Y)
for line in matrix:
    print(line)

coef_in_first_line = matrix[0]

plot(X, Y, f, -3, 2, "Forma de Newton")
