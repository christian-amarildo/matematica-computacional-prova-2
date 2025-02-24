import numpy as np

def quadratic_spline_interpolation(valores_x, valores_y, x_interp):
    """
    Função para calcular a interpolação spline quadrática.
    
    :param valores_x: Lista com os valores de x conhecidos
    :param valores_y: Lista com os valores de y correspondentes
    :param x_interp: Valor de x a ser interpolado
    :return: Valor interpolado
    """
    n = len(valores_x) - 1  # Número de intervalos
    a = valores_y
    b = np.zeros(n)
    c = np.zeros(n + 1)
    h = [valores_x[i + 1] - valores_x[i] for i in range(n)]
    
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
    
    # Encontrar o intervalo correto para x_interp
    for i in range(n):
        if valores_x[i] <= x_interp <= valores_x[i + 1]:
            dx = x_interp - valores_x[i]
            return a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
    
    raise ValueError("x_interp está fora do intervalo fornecido.")

# Exemplo de uso:
valores_x = [1.0, 2.0, 3.0, 4.0]  # Valores conhecidos de x
valores_y = [2.0, 3.0, 5.0, 7.0]  # Correspondentes valores de y
x_interp = 2.5  # Valor de x a ser interpolado

resultado_spline_quadratica = quadratic_spline_interpolation(valores_x, valores_y, x_interp)
print(f"Spline Quadrática: p({x_interp}) = {resultado_spline_quadratica}")
