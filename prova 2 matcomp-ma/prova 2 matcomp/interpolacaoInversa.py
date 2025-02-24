import numpy as np
import matplotlib.pyplot as plt

def quadratic_spline_interpolation_inverse(valores_x, valores_y, y_interp):
    """
    Função para calcular a interpolação spline quadrática inversa, estimando x para um dado y.
    
    :param valores_x: Lista com os valores de x conhecidos
    :param valores_y: Lista com os valores de y correspondentes
    :param y_interp: Valor de y para encontrar x
    :return: Valor estimado de x
    """
    n = len(valores_x) - 1  # Número de intervalos
    a = valores_x  # Invertendo x e y
    b = np.zeros(n)
    c = np.zeros(n + 1)
    h = [valores_y[i + 1] - valores_y[i] for i in range(n)]
    
    # Montando o sistema de equações para encontrar os coeficientes c
    A = np.zeros((n + 1, n + 1))
    B = np.zeros(n + 1)
    
    A[0][0] = 1  # Condição de contorno natural
    A[n][n] = 1  # Condição de contorno natural
    
    for i in range(1, n):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        B[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])
    
    # Resolvendo o sistema linear
    c = np.linalg.solve(A, B)
    
    # Calculando b e d
    d = np.zeros(n)
    for i in range(n):
        b[i] = (a[i + 1] - a[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
    
    # Encontrar o intervalo correto para y_interp
    for i in range(n):
        if valores_y[i] <= y_interp <= valores_y[i + 1]:
            dy = y_interp - valores_y[i]
            return a[i] + b[i] * dy + c[i] * dy**2 + d[i] * dy**3
    
    raise ValueError("y_interp está fora do intervalo fornecido.")

# Exemplo de uso:
valores_x = [1.0, 2.0, 3.0, 4.0]  # Valores conhecidos de x
valores_y = [2.0, 3.0, 5.0, 7.0]  # Correspondentes valores de y
y_interp = 3.5  # Valor de y para encontrar x

resultado_inversa = quadratic_spline_interpolation_inverse(valores_x, valores_y, y_interp)
print(f"Inversa Quadrática: x({y_interp}) = {resultado_inversa}")

# Plotando o gráfico
# Gerando a spline quadrática inversa
y_vals_fine = np.linspace(min(valores_y), max(valores_y), 500)
x_vals_spline = [quadratic_spline_interpolation_inverse(valores_x, valores_y, yi) for yi in y_vals_fine]

# Plotando os pontos conhecidos
plt.scatter(valores_y, valores_x, color='red', label="Pontos conhecidos (y, x)", zorder=5)

# Plotando a spline inversa
plt.plot(y_vals_fine, x_vals_spline, label="Spline Quadrática Inversa", color='blue')

# Plotando o ponto de interpolação
plt.scatter(y_interp, resultado_inversa, color='orange', zorder=5, label=f"Ponto interpolado (y={y_interp}, x={resultado_inversa})")

# Adicionando rótulos e título
plt.xlabel('y')
plt.ylabel('x')
plt.title('Interpolação Spline Quadrática Inversa')
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.show()
