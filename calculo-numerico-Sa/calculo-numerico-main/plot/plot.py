import numpy as np
import matplotlib.pyplot as plt


def plot(X: list, Y: list, f, a: int, b: int, label: str):
    # Geração dos valores de x de a até b
    x_vals = np.linspace(a, b, 100)
    y_vals = [f(x) for x in x_vals]

    # Plotando o gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=r'teste', color='b')
    
    # Destacando os pontos X e Y fornecidos
    plt.scatter(X, Y, color='red', zorder=5, label='Pontos dados')  # Pontos vermelhos

    # Adicionando linhas de grade e rótulos
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Legenda e rótulos
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(label)
    
    # Exibindo o gráfico
    plt.show()
