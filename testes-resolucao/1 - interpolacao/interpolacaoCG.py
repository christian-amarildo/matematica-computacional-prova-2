import numpy as np
import matplotlib.pyplot as plt


def resolver_sistema_linear(A, b):
    return np.linalg.solve(A, b)


def interpolacao_vandermonde(x, y, xp):
    n = len(x)
    A = np.vander(x, increasing=True)
    coef = resolver_sistema_linear(A, y)

    # Avaliação do polinômio
    yp = sum(coef[i] * (xp ** i) for i in range(n))
    return yp


# Teste
x = np.array([-1, 0, 1, 2])
y = np.array([4, 1, -1, 7])
xp = 1.5

print(f"Interpolação em x={xp}: {interpolacao_vandermonde(x, y, xp)}")


def lagrange(x, y, xp):
    n = len(x)
    yp = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += p * y[i]
    return yp


# Teste
print(f"Interpolação de Lagrange em x={xp}: {lagrange(x, y, xp)}")


def interpolacao_newton(x, y, xp):
    n = len(x)
    tabela = np.zeros((n, n))
    tabela[:, 0] = y  # Preenche a primeira coluna com os valores de y

    for j in range(1, n):
        for i in range(n - j):
            tabela[i, j] = (tabela[i + 1, j - 1] -
                            tabela[i, j - 1]) / (x[i + j] - x[i])

    coef = tabela[0, :]
    resultado = coef[0]
    termo_x = 1
    for j in range(1, n):
        termo_x *= (xp - x[j - 1])
        resultado += coef[j] * termo_x

    return resultado


# Teste com gráfico
x = np.array([-1, 0, 1, 2])
y = np.array([4, 1, -1, 7])
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


# Teste
print(f"Interpolação de Newton em x={xp}: {interpolacao_newton(x, y, xp)}")
