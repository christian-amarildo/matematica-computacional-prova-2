import numpy as np


def lagrange_interpolation(x, y, x_interp):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_interp - x[j]) / (x[i] - x[j])
        result += term
    return result


# Exemplo
x = [-1, 0, 2]
y = [4, 1, -1]
x_interp = 1
print(lagrange_interpolation(x, y, x_interp))  # Resultado:


def newton_interpolation(x, y, x_interp):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

    result = coef[0][0]
    for j in range(1, n):
        term = coef[0][j]
        for k in range(j):
            term *= (x_interp - x[k])
        result += term
    return result


# Exemplo
x = [-1, 0, 2]
y = [4, 1, -1]
x_interp = 1
print(newton_interpolation(x, y, x_interp))  # Resultado:


def inverse_interpolation(x, y, y_interp):
    from scipy.interpolate import interp1d
    f = interp1d(y, x, kind='linear')
    return f(y_interp)


# Exemplo
x = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y = [1.65, 1.82, 2.01, 2.23, 2.46, 2.72]
y_interp = 2.0
print(inverse_interpolation(x, y, y_interp))  # Resultado:
