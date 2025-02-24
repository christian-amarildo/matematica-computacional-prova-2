import numpy as np
import matplotlib.pyplot as plt

# Regra 1/3 de Simpson
def regra_simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1  # Garantir que o número de subdivisões seja par
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        soma += 2 * f(a + i * h)
    return soma * h / 3

# Exemplo de uso
def f(x):
    return x**2  # Função 

# Definição do intervalo e número de subdivisões
a, b = 0, np.pi
subdivisoes = [2, 4, 8, 16, 32]

# Cálculo e exibição dos resultados
for n in subdivisoes:
    resultado = regra_simpson(f, a, b, n)
    print(f'Regra 1/3 de Simpson com {n} subdivisões: {resultado}')

# Gráfico
x_vals = np.linspace(a, b, 100)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='Função Original')

for n in subdivisoes:
    x_sub = np.linspace(a, b, n+1)
    y_sub = f(x_sub)
    plt.plot(x_sub, y_sub, 'g--', alpha=0.6, label=f'Simpson ({n} subdivisões)')
    plt.scatter(x_sub, y_sub, color='green')

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Regra 1/3 de Simpson')
plt.grid()
plt.show()
