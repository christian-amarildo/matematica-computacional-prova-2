import numpy as np
import matplotlib.pyplot as plt

def calcular_diferencas_divididas(x, y):
    n = len(x)
    # Inicializa a tabela de diferenças divididas
    tabela = np.zeros((n, n))
    tabela[:, 0] = y  

    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            tabela[i, j] = (tabela[i + 1, j - 1] - tabela[i, j - 1]) / (x[i + j] - x[i])
    
    return tabela[0, :]  # retorna coeficientes do polinomio

def interpolacao_newton(x, y):
    coeficientes = calcular_diferencas_divididas(x, y)
    
    # Função que retorna o polinômio interpolador
    def polinomio(x):
        resultado = coeficientes[0]
        for i in range(1, len(coeficientes)):
            termo = coeficientes[i]
            for j in range(i):
                termo *= (x - x[j])
            resultado += termo
        return resultado
    
    return polinomio

# exemplo polinomio definido por usuario
x = []
y = []

polinomio = interpolacao_newton(x, y)

x_vals = np.linspace(min(x) - 1, max(x) + 1, 400)
y_vals = polinomio(x_vals)

plt.plot(x_vals, y_vals, label=f'polinomio: {polinomio}')
plt.scatter(x, y, color='gree', label='Pontos conhecidos')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title( 'interpolacao newton ')
plt.show()