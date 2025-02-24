import numpy as np
from solucoes_matriciais.fatoracao_lu import resolver_sistema_lu

def jacobian(f, x, h=1e-5):
    """
    Calcula a matriz jacobiana de uma função vetorial f em um ponto x.

    :param f: Função vetorial que recebe um array x e retorna um array.
    :param x: Ponto no qual a matriz jacobiana será calculada.
    :param h: Tamanho do passo para a diferença finita (default: 1e-5).
    :return: Matriz jacobiana (numpy array).
    """
    n = len(x)  # Número de variáveis
    f0 = f(x)   # Avalia a função no ponto x
    m = len(f0) # Número de funções (dimensão da saída de f)
    J = np.zeros((m, n))  # Inicializa a matriz jacobiana

    for i in range(n):
        # Cria um vetor de perturbação
        x_perturbed = np.copy(x)
        x_perturbed[i] += h  # Perturba a i-ésima variável

        # Calcula a derivada parcial usando diferença finita
        J[:, i] = (f(x_perturbed) - f0) / h

    return J

def gauss_newton(chutes, X, Y, modelo, max_iter, tol=1e-6):
    """
    Método de Gauss-Newton para resolver o problema de mínimos quadrados não lineares.

    :param chutes: Lista de chutes iniciais para os coeficientes Ex. [α₁, α₂]
    :param X: Lista de valores de X
    :param Y: Lista de valores de Y
    :param modelo: Função do modelo φ(x, coefs) que recebe x e os coeficientes.
    :param max_iter: Número máximo de iterações
    :param tol: Tolerância para convergência
    :return: Aproximação da solução dos coeficientes (α₁, α₂)
    """
    # Inicializa os coeficientes (chutes iniciais)
    coefs = np.array(chutes, dtype=float)

    for _ in range(max_iter):
        # Avaliar erro (resíduos)
        F_eval = Y - modelo(X, *coefs)
        
        # Avaliar Jacobiana
        J_eval = jacobian(lambda c: modelo(X, *c), coefs)
        
        J_T_J = J_eval.T @ J_eval  # J^T J
        J_T_F = J_eval.T @ F_eval  # J^T F
        delta_x = resolver_sistema_lu(J_T_J, J_T_F)

        # Atualizar os coeficientes
        new_coefs = coefs + delta_x
        
        # Verificar a convergência (diferença entre os coeficientes)
        coef_diff = np.abs(new_coefs - coefs)  # Diferença absoluta entre os coeficientes
        
        if np.all(coef_diff < tol):  # Verifica se todas as diferenças são menores que a tolerância
            return new_coefs
        
        coefs = new_coefs  # Atualizar coeficientes para a próxima iteração
    
    raise ValueError("O método não convergiu dentro do número máximo de iterações.")
