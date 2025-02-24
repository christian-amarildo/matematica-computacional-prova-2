import numpy as np
import matplotlib.pyplot as plt

# Regra dos Trapézios
def regra_trapezios(f, a, b, n):
    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        soma += f(a + i * h)
    return soma * h

# Exemplo de uso
def f(x):
    return x**2

# Definição do intervalo e número de subdivisões
a, b = 0, 2
subdivisoes = [2, 4, 8, 16, 32]

# Cálculo e exibição dos resultados
for n in subdivisoes:
    resultado = regra_trapezios(f, a, b, n)
    print(f'Regra dos Trapézios com {n} subdivisões: {resultado}')

# Gráfico
x_vals = np.linspace(a, b, 100)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='Função Original')

for n in subdivisoes:
    x_sub = np.linspace(a, b, n+1)
    y_sub = f(x_sub)
    plt.plot(x_sub, y_sub, 'r--', alpha=0.6, label=f'Trapézios ({n} subdivisões)')
    plt.scatter(x_sub, y_sub, color='red')

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Regra dos Trapézios')
plt.grid()
plt.show()