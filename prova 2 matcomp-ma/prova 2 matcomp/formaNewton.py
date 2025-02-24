import numpy as np
import matplotlib.pyplot as plt

def newton_interpolation(pontos, valores_x, valores_y, x_interp):
    """
    Função para calcular a interpolação de Newton.
    
    :param pontos: Número de pontos conhecidos
    :param valores_x: Lista com os valores de x conhecidos
    :param valores_y: Lista com os valores de y correspondentes
    :param x_interp: Valor de x a ser interpolado
    :return: Valor da interpolação em x_interp
    """
    tabela = [valores_y.copy()]
    
    # Construção da tabela de diferenças divididas
    for n in range(1, pontos):
        ordem = []
        for m in range(pontos - n):
            difDividida = (tabela[n - 1][m + 1] - tabela[n - 1][m]) / (valores_x[m + n] - valores_x[m])
            ordem.append(difDividida)
        tabela.append(ordem)
    
    # Cálculo da interpolação de Newton
    pn = tabela[0][0]
    termo = 1
    for i in range(1, pontos):
        termo *= (x_interp - valores_x[i - 1])
        pn += tabela[i][0] * termo
    
    return pn

# Exemplo de uso:
pontos = 3
valores_x = [1.0, 2.0, 3.0]  # Valores conhecidos de x
valores_y = [2.0, 3.0, 5.0]  # Valores correspondentes de y
x_interp = 2.5  # Valor de x a ser interpolado

resultado = newton_interpolation(pontos, valores_x, valores_y, x_interp)
print(f"p({x_interp}) = {resultado}")

# Plotando o gráfico
x_vals = np.linspace(0, 4, 100)  # Geração de valores para o eixo x
y_vals = (x_vals**3 - 2*x_vals + 1)  # Usando uma função exemplo para plotar a curva (modifique conforme necessário)

# Plot da função original (apenas como exemplo)
plt.plot(x_vals, y_vals, label="Função Original f(x)", color='blue')

# Plot dos pontos conhecidos
plt.scatter(valores_x, valores_y, color='red', label="Pontos conhecidos", zorder=5)

# Plot da interpolação de Newton
x_interp_vals = np.linspace(min(valores_x), max(valores_x), 100)
y_interp_vals = [newton_interpolation(pontos, valores_x, valores_y, xi) for xi in x_interp_vals]
plt.plot(x_interp_vals, y_interp_vals, label="Interpolação de Newton", color='green', linestyle='--')

# Plotando o ponto interpolado
plt.scatter(x_interp, resultado, color='orange', zorder=5, label=f"Ponto interpolado (x={x_interp}, y={resultado})")

# Adicionando rótulos e título
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolação de Newton')
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.show()
