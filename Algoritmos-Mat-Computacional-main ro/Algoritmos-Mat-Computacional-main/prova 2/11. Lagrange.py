import numpy as np
import matplotlib.pyplot as plt

def Lagrange(x, x_tab, y_tab):
    """
    Calcula o valor do polinômio interpolador de Lagrange em um ponto x
    
    Parâmetros:
    x -- ponto onde calcular o valor do polinômio
    x_tab -- array numpy com os pontos x de interpolação
    y_tab -- array numpy com os valores correspondentes y
    
    Retorna:
    Valor do polinômio interpolador em x
    """
    n = len(x_tab)
    soma = np.zeros_like(x)  # Inicializa com zeros usando o dtype correto
    
    for i in range(n):
        l = np.ones_like(x)  # Inicializa o polinômio base L_k(x)
        
        for j in range(n):
            if i != j:  
                l *= (x - x_tab[j]) / (x_tab[i] - x_tab[j]) # fórmula principal de lagrange
                
        soma += y_tab[i] * l
        
    return soma

# Exemplo de uso
x_tab = np.array([-1., 0., 2.])  # Pontos x de exemplo       --> x0, x1, x2
y_tab = np.array([4., 1., -1.])  # Valores y correspondentes --> y0, y1, y2

# 1° grau - 2 pontos
# 2° grau - 3 pontos
# 3° grau - 4 pontos
# ...

# Criar pontos para plotagem suave
x_plot = np.linspace(min(x_tab)-0.5, max(x_tab)+0.5, 1000)
y_plot = Lagrange(x_plot, x_tab, y_tab)

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, 'b-', label='Polinômio Interpolador')
plt.scatter(x_tab, y_tab, color='red', marker='o', s=100, 
           label='Pontos de Interpolação')

plt.grid(True)
plt.legend()
plt.title('Interpolação Polinomial de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.show()