import numpy as np
import matplotlib.pyplot as plt
from math import log, exp

# Função para ajuste linear


def linear_fit(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi**2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    denom = n * sum_x2 - sum_x**2
    a = (n * sum_xy - sum_x * sum_y) / denom
    b = (sum_x2 * sum_y - sum_x * sum_xy) / denom

    return a, b

# Função para ajuste quadrático


def quadratic_fit(x, y):
    n = len(x)
    A = np.zeros((3, 3))
    b = np.zeros(3)

    A[0, 0] = n
    A[0, 1] = A[1, 0] = sum(x)
    A[0, 2] = A[1, 1] = A[2, 0] = sum(xi**2 for xi in x)
    A[1, 2] = A[2, 1] = sum(xi**3 for xi in x)
    A[2, 2] = sum(xi**4 for xi in x)

    b[0] = sum(y)
    b[1] = sum(xi * yi for xi, yi in zip(x, y))
    b[2] = sum(xi**2 * yi for xi, yi in zip(x, y))

    coeffs = np.linalg.solve(A, b)
    return coeffs

# Função para ajuste exponencial


def exponential_fit(x, y):
    ln_y = [log(yi) for yi in y]
    a, b = linear_fit(x, ln_y)
    alpha = exp(b)
    beta = a
    return alpha, beta

# Função para calcular o erro quadrático médio (MSE)


def mse(y_real, y_pred):
    return sum((yi - yj)**2 for yi, yj in zip(y_real, y_pred)) / len(y_real)

# Função para ajustar automaticamente e comparar modelos


def auto_fit(x, y):
    # Ajuste linear
    a_linear, b_linear = linear_fit(x, y)
    y_linear = [a_linear * xi + b_linear for xi in x]
    mse_linear = mse(y, y_linear)

    # Ajuste quadrático
    coeffs_quad = quadratic_fit(x, y)
    y_quad = [coeffs_quad[0] + coeffs_quad[1] *
              xi + coeffs_quad[2] * xi**2 for xi in x]
    mse_quad = mse(y, y_quad)

    # Ajuste exponencial
    alpha_exp, beta_exp = exponential_fit(x, y)
    y_exp = [alpha_exp * exp(beta_exp * xi) for xi in x]
    mse_exp = mse(y, y_exp)

    # Escolha do melhor modelo
    models = {
        "Linear": (mse_linear, y_linear),
        "Quadrático": (mse_quad, y_quad),
        "Exponencial": (mse_exp, y_exp)
    }
    best_model = min(models, key=lambda k: models[k][0])

    # Plotando os resultados
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='black', label='Dados')

    x_fit = np.linspace(min(x), max(x), 100)

    # Linear
    y_linear_fit = [a_linear * xi + b_linear for xi in x_fit]
    plt.plot(x_fit, y_linear_fit,
             label=f'Linear (MSE: {mse_linear:.2f})', linestyle='--')

    # Quadrático
    y_quad_fit = [coeffs_quad[0] + coeffs_quad[1] *
                  xi + coeffs_quad[2] * xi**2 for xi in x_fit]
    plt.plot(x_fit, y_quad_fit,
             label=f'Quadrático (MSE: {mse_quad:.2f})', linestyle='-.')

    # Exponencial
    y_exp_fit = [alpha_exp * exp(beta_exp * xi) for xi in x_fit]
    plt.plot(x_fit, y_exp_fit,
             label=f'Exponencial (MSE: {mse_exp:.2f})', linestyle=':')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title(
        f'Melhor modelo: {best_model} (MSE: {models[best_model][0]:.2f})')
    plt.grid(True)
    plt.show()

    return best_model, models[best_model][1]


# Exemplo de uso
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

best_model, y_pred = auto_fit(x, y)
print(f"Melhor modelo: {best_model}")
