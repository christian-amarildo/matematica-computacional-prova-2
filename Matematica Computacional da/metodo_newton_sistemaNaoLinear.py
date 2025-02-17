import numpy as np

def f(x):
    """
    Função que representa o sistema de equações não lineares.
    Substitua os valores nesta função para alterar o sistema.

    Parâmetros:
    x : list
        Vetor com as variáveis do sistema.

    Retorna:
    b : list
        Vetor com os resultados das funções não lineares.
    """
    N = len(x)
    b = [0] * N
    # Sistema de equações não lineares
    b[0] = x[0]**2 + x[1]**2 - 2
    b[1] = x[0]**2 - (x[1]**2) / 9 - 1
    return b

def J(x):
    """
    Função que calcula a matriz Jacobiana do sistema.
    Substitua os valores nesta função para alterar o sistema.

    Parâmetros:
    x : list
        Vetor com as variáveis do sistema.

    Retorna:
    A : list of lists
        Matriz Jacobiana calculada no ponto x.
    """
    # Inicialização da matriz Jacobiana
    A = [[0, 0], [0, 0]]
    # Derivadas parciais do sistema
    A[0][0] = 2 * x[0]
    A[0][1] = 2 * x[1]
    A[1][0] = 2 * x[0]
    A[1][1] = (-2 / 9) * x[1]
    return A

# Parâmetros do método de Newton
x0 = [1, 1]  # Chute inicial
max_iter = 50  # Número máximo de iterações
eps = 0.0001  # Tolerância para convergência
div = 10**20  # Critério para divergência

# Impressão inicial
print("Iteração 0: ", x0)

# Loop do método de Newton
iter = 0
while iter < max_iter:
    # Calcula a matriz Jacobiana no ponto atual
    A = np.array(J(x0))
    # Calcula o vetor de funções no ponto atual
    b = np.array(f(x0))
    # Resolve o sistema linear J(x) * s = -f(x)
    s = np.linalg.solve(A, -b)
    # Atualiza o valor de x
    x1 = np.array(x0) + s
    iter += 1

    # Exibe a iteração atual
    print(f"Iteração {iter}: {x1}")

    # Verifica critério de convergência
    if (np.linalg.norm(s, np.inf) < eps) or (np.linalg.norm(b, np.inf) < eps):
        print("\nConvergiu!")
        print("Precisão alcançada: ", np.linalg.norm(s, np.inf))
        print("Solução encontrada: ", x1)
        print("Verificação da solução: f(x1) = ", f(x1))
        break

    # Verifica critério de divergência
    if np.linalg.norm(b, np.inf) > div:
        print("\nDivergiu!")
        break

    # Atualiza x0 para a próxima iteração
    x0 = x1
else:
    print("\nNúmero máximo de iterações atingido. Não convergiu.")

# Finaliza o código
print("\nProcesso concluído.")
