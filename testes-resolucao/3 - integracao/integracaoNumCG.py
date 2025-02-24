import matplotlib.pyplot as plt
import numpy as np


def regra_trapezio(f, a, b, n):
    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        soma += f(a + i * h)

    return h * soma


# Teste com gráfico
def f(x): return x**2


a, b, n = 0, 2, 5
x_vals = np.linspace(a, b, n+1)
y_vals = f(x_vals)

integral_aproximada = regra_trapezio(f, a, b, n)

plt.plot(x_vals, y_vals, 'bo-', label="Aproximação Trapézios")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="blue")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.title(
    f"Regra do Trapézio - Integral Aproximada: {integral_aproximada:.4f}")
plt.show()


print(f"Integral aproximada (Trapézio) de x^2: {regra_trapezio(f, 0, 2, 10)}")


def regra_simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1  # Garantir que n seja par
    h = (b - a) / n
    soma = f(a) + f(b)

    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)

    for i in range(2, n-1, 2):
        soma += 2 * f(a + i * h)

    return (h / 3) * soma


# Teste com gráfico
def f(x): return x**2


a, b, n = 0, 2, 6
x_vals = np.linspace(a, b, n+1)
y_vals = f(x_vals)

integral_aproximada = regra_simpson(f, a, b, n)

plt.plot(x_vals, y_vals, 'go-', label="Aproximação Simpson")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="green")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.title(f"Regra de Simpson - Integral Aproximada: {integral_aproximada:.4f}")
plt.show()

# Teste
print(f"Integral aproximada (Simpson) de x^2: {regra_simpson(f, 0, 2, 10)}")
