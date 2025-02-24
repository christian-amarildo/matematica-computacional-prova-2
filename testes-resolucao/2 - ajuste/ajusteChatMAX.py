import numpy as np
import matplotlib.pyplot as plt
import math


def ajuste_linear(x, y):
    """ Ajuste linear y = ax + b """
    n = len(x)
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = sum(x[i] * y[i] for i in range(n))
    soma_x2 = sum(x[i]**2 for i in range(n))

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
    b = (soma_y - a * soma_x) / n

    return lambda x: a * x + b, f"y = {a:.4f}x + {b:.4f}"


def ajuste_quadratico(x, y):
    """ Ajuste quadrático y = ax² + bx + c """
    n = len(x)
    soma_x = sum(x)
    soma_x2 = sum(x[i]**2 for i in range(n))
    soma_x3 = sum(x[i]**3 for i in range(n))
    soma_x4 = sum(x[i]**4 for i in range(n))
    soma_y = sum(y)
    soma_xy = sum(x[i] * y[i] for i in range(n))
    soma_x2y = sum(x[i]**2 * y[i] for i in range(n))

    A = [
        [n, soma_x, soma_x2],
        [soma_x, soma_x2, soma_x3],
        [soma_x2, soma_x3, soma_x4]
    ]
    B = [soma_y, soma_xy, soma_x2y]

    a, b, c = np.linalg.solve(A, B)

    return lambda x: a * x**2 + b * x + c, f"y = {a:.4f}x² + {b:.4f}x + {c:.4f}"


def ajuste_exponencial(x, y):
    """ Ajuste exponencial y = a * e^(bx) transformado para ln(y) = bx + ln(a) """
    n = len(x)
    y_log = [math.log(yi) for yi in y]  # ln(y)

    soma_x = sum(x)
    soma_y = sum(y_log)
    soma_xy = sum(x[i] * y_log[i] for i in range(n))
    soma_x2 = sum(x[i]**2 for i in range(n))

    b = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
    a = math.exp((soma_y - b * soma_x) / n)

    return lambda x: a * math.exp(b * x), f"y = {a:.4f} * e^({b:.4f}x)"


def calcular_erro(y_real, y_estimado):
    """ Calcula o erro médio absoluto (MAE) entre os valores reais e estimados """
    return sum(abs(y_real[i] - y_estimado[i]) for i in range(len(y_real))) / len(y_real)


def ajustar_melhor_funcao(x, y):
    """ Testa diferentes funções e escolhe a que tem menor erro """
    modelos = {
        "Linear": ajuste_linear(x, y),
        "Quadrático": ajuste_quadratico(x, y),
        "Exponencial": ajuste_exponencial(x, y)
    }

    erros = {}
    x_plot = np.linspace(min(x), max(x), 100)

    plt.scatter(x, y, color="black", label="Pontos Dados")

    for nome, (modelo, eq) in modelos.items():
        y_estimado = [modelo(xi) for xi in x]
        erro = calcular_erro(y, y_estimado)
        erros[nome] = erro

        y_plot = [modelo(xi) for xi in x_plot]
        plt.plot(x_plot, y_plot, label=f"{nome}: {eq}\nErro: {erro:.4f}")

    melhor_modelo = min(erros, key=erros.get)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.title(f"Ajuste de Curva - Melhor Modelo: {melhor_modelo}")
    plt.show()

    return f"O melhor modelo é {melhor_modelo} com erro {erros[melhor_modelo]:.4f}"


# 🔹 Teste com um conjunto de pontos
# x = [1, 2, 3, 4, 5]
# y = [2.7, 7.4, 20.1, 54.6, 148.4]

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

print(ajustar_melhor_funcao(x, y))
