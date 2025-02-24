import numpy as np
import matplotlib.pyplot as plt


def tabela_diferencas_divididas(x, y):
    """
    Constrói a tabela de diferenças divididas para Interpolação de Newton.
    Retorna a tabela completa e imprime no console.
    """
    n = len(x)
    tabela = np.zeros((n, n))
    tabela[:, 0] = y  # Primeira coluna recebe os valores de y

    for j in range(1, n):
        for i in range(n - j):
            tabela[i, j] = (tabela[i + 1, j - 1] -
                            tabela[i, j - 1]) / (x[i + j] - x[i])

    # Imprime a tabela formatada no console
    print("\n=== Tabela de Diferenças Divididas ===")
    print("\nx[i] | f(xi) | f(xi, xi+1) | f(xi, ..., xi+2) | f(xi, ..., ..., xi+3) |")
    for i in range(n):
        linha = [f"{tabela[i, j]:.6f}" if j <=
                 n - i - 1 else " " for j in range(n)]
        print(f"x[{i}] = {x[i]:.2f} | " + "  ".join(linha))

    return tabela


def interpolacao_newton(x, y, xp):
    """
    Realiza a interpolação pelo método de Newton, utilizando a tabela de diferenças divididas.
    """
    tabela = tabela_diferencas_divididas(x, y)
    coef = tabela[0, :]  # Coeficientes do polinômio de Newton

    resultado = coef[0]
    termo_x = 1
    for j in range(1, len(x)):
        termo_x *= (xp - x[j - 1])
        resultado += coef[j] * termo_x

    return resultado


def plotar_interpolacao_newton(x, y):
    """
    Plota o polinômio interpolador de Newton junto com os pontos dados.
    """
    xp = np.linspace(min(x), max(x), 100)
    yp = [interpolacao_newton(x, y, xi) for xi in xp]

    plt.scatter(x, y, color='red', label="Pontos Dados")
    plt.plot(xp, yp, color='blue', label="Interpolação de Newton")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.title("Interpolação de Newton")
    plt.show()


# 🔹 Teste com um conjunto de pontos
x = np.array([1, 2, 3, 4])
y = np.array([2, 3, 5, 8])
xp = 2.5

print(f"\nInterpolação em x={xp}: {interpolacao_newton(x, y, xp):.6f}")
plotar_interpolacao_newton(x, y)
