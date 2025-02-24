import numpy as np
import matplotlib.pyplot as plt


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h


def simpson_rule(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)
    return result * h / 3


# Função a ser integrada
def f(x): return np.sin(x)


a, b = 0, np.pi
n = 100

# Calculando as integrais
trap_result = trapezoidal_rule(f, a, b, n)
simp_result = simpson_rule(f, a, b, n)
print(f"Trapézios: {trap_result}, Simpson: {simp_result}")

# Plotando a função e a área sob a curva
x_vals = np.linspace(a, b, 1000)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='f(x) = sin(x)')
plt.fill_between(x_vals, y_vals, alpha=0.2, label='Área sob a curva')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Integração Numérica')
plt.grid(True)
plt.show()
