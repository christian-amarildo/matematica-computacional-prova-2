import math
import numpy as np
import matplotlib.pyplot as plt


def linear_fit(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi**2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Resolvendo o sistema linear
    denom = n * sum_x2 - sum_x**2
    a = (n * sum_xy - sum_x * sum_y) / denom
    b = (sum_x2 * sum_y - sum_x * sum_xy) / denom

    return a, b


# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Ajuste linear
a, b = linear_fit(x, y)
print(f"Coeficientes: a = {a}, b = {b}")

# Gerando pontos para a reta ajustada
x_fit = [min(x), max(x)]
y_fit = [a * xi + b for xi in x_fit]

# Plotando
plt.scatter(x, y, color='blue', label='Dados')
plt.plot(x_fit, y_fit, color='red', label=f'Ajuste: y = {a:.2f}x + {b:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste Linear')
plt.grid(True)
plt.show()


def exponential_fit(x, y):
    # Linearização: ln(y) = ln(alpha) + beta * x
    ln_y = [math.log(yi) for yi in y]

    # Ajuste linear nos pontos (x, ln(y))
    a, b = linear_fit(x, ln_y)

    # Convertendo de volta para a forma exponencial
    alpha = math.exp(b)
    beta = a

    return alpha, beta


# Dados
# x = [1, 2, 3, 4, 5]
# y = [2.7, 7.4, 20.1, 54.6, 148.4]

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Ajuste exponencial
alpha, beta = exponential_fit(x, y)
print(f"Coeficientes: alpha = {alpha}, beta = {beta}")

# Gerando pontos para a curva ajustada
x_fit = [min(x) + i * 0.1 for i in range(int((max(x) - min(x)) * 10 + 1))]
y_fit = [alpha * math.exp(beta * xi) for xi in x_fit]

# Plotando
plt.scatter(x, y, color='blue', label='Dados')
plt.plot(x_fit, y_fit, color='red',
         label=f'Ajuste: y = {alpha:.2f}e^({beta:.2f}x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste Exponencial')
plt.grid(True)
plt.show()


def polynomial_fit(x, y, degree):
    n = len(x)
    A = []
    b = []

    # Construindo a matriz A e o vetor b
    for k in range(degree + 1):
        row = []
        for j in range(degree + 1):
            row.append(sum(xi**(k + j) for xi in x))
        A.append(row)
        b.append(sum(yi * xi**k for xi, yi in zip(x, y)))

    # Resolvendo o sistema linear
    coeffs = np.linalg.solve(A, b)
    return coeffs


# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
degree = 2

# Ajuste polinomial
coeffs = polynomial_fit(x, y, degree)
print(f"Coeficientes: a = {coeffs[2]}, b = {coeffs[1]}, c = {coeffs[0]}")

# Gerando pontos para a parábola ajustada
x_fit = [min(x) + i * 0.1 for i in range(int((max(x) - min(x)) * 10 + 1))]
y_fit = [coeffs[2] * xi**2 + coeffs[1] * xi + coeffs[0] for xi in x_fit]

# Plotando
plt.scatter(x, y, color='blue', label='Dados')
plt.plot(x_fit, y_fit, color='red',
         label=f'Ajuste: y = {coeffs[2]:.2f}x² + {coeffs[1]:.2f}x + {coeffs[0]:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste Polinomial (Grau 2)')
plt.grid(True)
plt.show()

# import numpy as np


# def least_squares(x, y, degree):
#     A = np.vander(x, degree + 1)
#     coeffs = np.linalg.lstsq(A, y, rcond=None)[0]
#     return coeffs


# # Exemplo
# x = np.array([-1, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1.0])
# y = np.array([2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05])
# degree = 2
# coeffs = least_squares(x, y, degree)
# print(coeffs)  # Coeficientes do polinômio
