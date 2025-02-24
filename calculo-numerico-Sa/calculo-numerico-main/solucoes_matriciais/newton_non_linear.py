import numpy as np
import math

def non_linear_newton(chutes: list, F: list, J: list, max_iter: int, tol=1e-6):
    """
    Método de Newton para sistemas de equações não lineares.
    
    :param chutes: Lista de chutes iniciais para as variáveis [x1, x2, ..., xn]
    :param F: Lista de funções não lineares [f1, f2, ..., fn]
    :param J: Lista de listas representando a matriz jacobiana J[i][j]
    :param max_iter: Número máximo de iterações
    :param tol: Tolerância para convergência
    :return: Aproximação da solução
    """
    
    x = np.array(chutes, dtype=float)  # Converter chutes para um array NumPy

    for _ in range(max_iter):
        # Resolve cada função de F no ponto x_k
        F_eval = np.array([f(*x) for f in F], dtype=float)

        # Preenchimento da matriz jacobiana com o resulatdo de cada função derivada no ponto x_k.
        J_eval = np.array([[J[i][j](*x) if callable(J[i][j]) else J[i][j] 
                            for j in range(len(x))] for i in range(len(F))], dtype=float)

        # Resolver o sistema J(x) * Δx = -F(x)
        try:
            delta_x = np.linalg.solve(J_eval, -F_eval)
            print("delta_x", delta_x)
        except np.linalg.LinAlgError:
            raise ValueError("A matriz jacobiana é singular, o método falhou.")

        # Atualizar a estimativa de x
        x += delta_x

        # Critério de parada
        if np.linalg.norm(delta_x, ord=np.inf) < tol:
            return x

    raise ValueError("O método não convergiu dentro do número máximo de iterações.")

# EXEMPLO DE USO

# # Definir o sistema de equações não lineares
# F = [
#     lambda x1, x2, x3: 3*x1 - math.cos(x2*x3) - 0.5,
#     lambda x1, x2, x3: (x1**2) - 81*((x2+0.1)**2) + math.sin(x3) + 1.06,
#     lambda x1, x2, x3: math.exp(-x1*x2) + 20*x3 + (10*math.pi - 3)/3
# ]

# # Definir a matriz jacobiana
# J = [
#     [lambda x1, x2, x3: 3, lambda x1, x2, x3: x3 * math.sin(x2*x3), lambda x1, x2, x3: x2 * math.sin(x2*x3)],
#     [lambda x1, x2, x3: 2*x1, lambda x1, x2, x3: -162*(x2 + 0.1), lambda x1, x2, x3: math.cos(x3)],
#     [lambda x1, x2, x3: -x2 * math.exp(-x1*x2), lambda x1, x2, x3: -x1 * math.exp(-x1*x2), lambda x1, x2, x3: 20]
# ]

# # Chutes iniciais
# chutes = [0.1, 0.1, -0.1]

# # Resolver o sistema usando Newton-Raphson
# solucao = non_linear_newton(chutes, F, J, max_iter=10)

# print("Solução aproximada:", solucao)
