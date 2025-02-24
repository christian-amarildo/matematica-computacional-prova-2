import numpy as np
import matplotlib.pyplot as plt

from interpolacao.lagrange import lagrange


def plot(X: list, Y: list, newton_cotes, a: float, b: float, label: str):
    """
    X, Y para lagrange e "a" e "b" são intervalos de integração
    """

    x_vals = np.linspace(a, b, 100)
    y_vals = [lagrange(X, Y, x) for x in x_vals]

    integral = newton_cotes(X, Y, a, b)

    # Criando o gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=label, color="blue")
    plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área sob a curva")
    plt.scatter(X, Y, color="red", label="Pontos conhecidos")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Área sob a curva: {integral} - Interpolação de Lagrange")
    plt.legend()
    plt.grid()

    # Exibir o gráfico
    plt.show()