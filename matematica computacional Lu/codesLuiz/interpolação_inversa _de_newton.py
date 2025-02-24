import numpy as np
import matplotlib.pyplot as plt

def calcular_diferencas_divididas(pontos_x, pontos_y):
    n = len(pontos_x)
    # inicializa a tabela de diferenças divididas
    tabela = np.zeros((n, n))
    tabela[:, 0] = pontos_y  

    # calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            tabela[i, j] = (tabela[i + 1, j - 1] - tabela[i, j - 1]) / (pontos_x[i + j] - pontos_x[i])
    
    return tabela[0, :]  # retorna 0 coeficientes do polinômio

def interpolacao_newton(pontos_x, pontos_y):
    coeficientes = calcular_diferencas_divididas(pontos_x, pontos_y)
    
    #  retorna o polinomio interpolador
    def polinomio(x):
        resultado = coeficientes[0]
        for i in range(1, len(coeficientes)):
            termo = coeficientes[i]
            for j in range(i):
                termo *= (x - pontos_x[j])
            resultado += termo
        return resultado
    
    return polinomio

def interpolacao_inversa(pontos_x, pontos_y, valor_y):
    # inverte x e y para interpolação inversa
    polinomio_inverso = interpolacao_newton(pontos_y, pontos_x)
    return polinomio_inverso(valor_y)

pontos_x = []
pontos_y = []

valor_y = 2.0

# encontrar x tal que f(x) = valor_y
x_interpolado = interpolacao_inversa(pontos_x, pontos_y, valor_y)

print(f" valor de x tal que f(x) = {valor_y} e aproximadamente: {x_interpolado:.6f}")

x_vals = np.linspace(min(pontos_x), max(pontos_x), 400)
y_vals = interpolacao_newton(pontos_x, pontos_y)(x_vals)

plt.plot(x_vals, y_vals, label='polinômio Interpolador')
plt.scatter(pontos_x, pontos_y, color='green', label='pontos conhecidos')
plt.axhline(y=valor_y, color='green', linestyle='--', label=f'f(x) = {valor_y}')
plt.axvline(x=x_interpolado, color='purple', linestyle='--', label=f'x = {x_interpolado:.6f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('interpolação inversa  de Newton')
plt.show()