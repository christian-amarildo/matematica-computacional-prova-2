import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(pontos, valores_x, valores_y, x_interp):
    """
    Função para calcular a interpolação de Lagrange.
    
    :param pontos: Número de pontos conhecidos
    :param valores_x: Lista com os valores de x conhecidos
    :param valores_y: Lista com os valores de y correspondentes
    :param x_interp: Valor de x a ser interpolado
    :return: Valor da interpolação em x_interp
    """
    coeficientes = []  # Lista para armazenar os coeficientes de Lagrange
    
    # Cálculo dos coeficientes L
    for i in range(pontos):
        L = 1  # Inicializa o coeficiente L_i
        for j in range(pontos):
            if i != j:
                L *= (x_interp - valores_x[j]) / (valores_x[i] - valores_x[j])
        coeficientes.append(L)
    
    # Cálculo da aproximação polinomial P(x)
    pn = 0
    for i in range(pontos):
        pn += valores_y[i] * coeficientes[i]
    
    return pn

# Exemplo de uso:
pontos = 3
valores_x = [1.0, 2.0, 3.0]  # Valores conhecidos de x
valores_y = [2.0, 3.0, 5.0]  # Valores correspondentes de y
x_interp = 2.5  # Valor de x a ser interpolado

# Gerando pontos para o gráfico
x_vals = np.linspace(min(valores_x), max(valores_x), 100)
y_vals = [lagrange_interpolation(pontos, valores_x, valores_y, x) for x in x_vals]

# Plotando o gráfico
plt.plot(x_vals, y_vals, label='Interpolação de Lagrange', color='blue')
plt.scatter(valores_x, valores_y, color='red', label='Pontos conhecidos')
plt.scatter(x_interp, lagrange_interpolation(pontos, valores_x, valores_y, x_interp), color='green', label=f'Interpolado ({x_interp})')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.legend()
plt.title('Interpolação de Lagrange')
plt.grid()
plt.show()
