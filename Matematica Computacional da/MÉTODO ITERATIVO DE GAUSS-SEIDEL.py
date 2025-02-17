import numpy as np

def resolver_sistema_linear_gauss_seidel(matriz, vetor, precisao=8, max_iteracoes=500):
    """
    Resolve um sistema linear Ax = b usando o método iterativo de Gauss-Seidel.

    Parâmetros:
        matriz (numpy array): Matriz dos coeficientes.
        vetor (numpy array): Vetor dos termos independentes.
        precisao (int): Precisão para o critério de parada (p). Default: 8.
        max_iteracoes (int): Número máximo de iterações. Default: 100.

    Retorna:
        solucao (numpy array): Vetor solução.
        iteracoes (int): Número de iterações realizadas.
    """
    tamanho = len(vetor)
    solucao = np.zeros_like(vetor, dtype=float)  # Chute inicial

    iteracoes = 0
    erro = 1

    while erro >= 10**(-precisao) and iteracoes <= max_iteracoes:
        solucao_antiga = np.copy(solucao)

        for i in range(tamanho):
            soma = sum(matriz[i, j] * solucao[j] for j in range(tamanho) if j != i)
            solucao[i] = (vetor[i] - soma) / matriz[i, i]

        erro = np.max(np.abs(solucao - solucao_antiga)) / np.max(np.abs(solucao))
        iteracoes += 1

    if iteracoes > max_iteracoes:
        raise Exception("O método não convergiu após o número máximo de iterações.")

    return solucao, iteracoes

def gerar_sistema_linear(tamanho):
    """
    Gera um sistema linear aleatório Ax = b sem garantir a diagonal dominante.

    Parâmetros:
        tamanho (int): Tamanho do sistema (número de variáveis e equações).

    Retorna:
        matriz (numpy array): Matriz dos coeficientes.
        vetor (numpy array): Vetor dos termos independentes.
    """
    matriz = np.random.randint(1, 10, size=(tamanho, tamanho))
    vetor = np.random.randint(1, 20, size=(tamanho, 1))
    return matriz, vetor

def verificar_matriz_adequada(matriz):
    """
    Avalia se a matriz é adequada para o método de Gauss-Seidel.

    Parâmetros:
        matriz (numpy array): Matriz dos coeficientes.

    Retorna:
        bool: True se a matriz for estritamente diagonal dominante, False caso contrário.
    """
    tamanho = matriz.shape[0]
    for i in range(tamanho):
        elemento_diagonal = abs(matriz[i, i])
        soma_fora_diagonal = sum(abs(matriz[i, j]) for j in range(tamanho) if j != i)
        if elemento_diagonal <= soma_fora_diagonal:
            return False
    return True

# Exemplo de uso
if __name__ == "__main__":
    # Gera um sistema linear aleatório
    tamanho = int(input("Digite o tamanho do sistema linear: "))
    matriz, vetor = gerar_sistema_linear(tamanho)

    print("Matriz A:")
    print(matriz)
    print("Vetor b:")
    print(vetor)

    if verificar_matriz_adequada(matriz):
        print("A matriz é adequada para o método de Gauss-Seidel.")
        try:
            solucao, iteracoes = resolver_sistema_linear_gauss_seidel(matriz, vetor)
            print("Solução:")
            print(solucao)
            print(f"Número de iterações: {iteracoes}")
        except Exception as e:
            print(e)
    else:
        print("A matriz NÃO é adequada para o método de Gauss-Seidel.")