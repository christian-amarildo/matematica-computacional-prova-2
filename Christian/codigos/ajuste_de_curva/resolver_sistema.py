import numpy as np  # Importando a biblioteca numpy, que oferece funções para manipulação de arrays e operações matemáticas

def decomposicao_LU_pivot(A):
    """
    Realiza a decomposição LU com pivoteamento parcial.
    A decomposição LU transforma uma matriz quadrada A em um produto de duas matrizes: L (triangular inferior)
    e U (triangular superior). O pivoteamento parcial é usado para garantir a estabilidade numérica durante o processo.
    
    Parâmetros:
    A : np.array
        Matriz quadrada de coeficientes do sistema, que será decomposta.

    Retorno:
    P, L, U : np.array, np.array, np.array
        Matrizes de permutação (P), triangular inferior (L) e triangular superior (U).
        Essas matrizes representam a decomposição LU da matriz A.
    """
    n = len(A)  # Obtendo a ordem (número de linhas ou colunas) da matriz quadrada A
    P = np.eye(n)  # Inicializando a matriz de permutação como a matriz identidade de tamanho n
    L = np.eye(n)  # Inicializando a matriz triangular inferior L como a matriz identidade de tamanho n
    U = A.astype(float)  # Copiando A para U (em formato float, pois pode ocorrer divisão)

    # Loop principal que percorre cada coluna da matriz (k = índice da coluna)
    for k in range(n):
        # Pivoteamento parcial: escolhe o maior elemento na coluna k (abaixo ou na diagonal)
        pivot = np.argmax(np.abs(U[k:, k])) + k  # Encontrando o índice do maior valor absoluto na coluna k
        if pivot != k:
            # Se o pivô não estiver na posição esperada, trocamos as linhas de U e também ajustamos P
            U[[k, pivot]] = U[[pivot, k]]  # Troca as linhas k e pivot na matriz U
            P[[k, pivot]] = P[[pivot, k]]  # Troca as linhas k e pivot na matriz P (matriz de permutação)
            if k > 0:
                L[[k, pivot], :k] = L[[pivot, k], :k]  # Troca as linhas de L para manter a estrutura triangular

        # Eliminação para criar a matriz triangular inferior (L) e superior (U)
        for i in range(k + 1, n):  # Loop para as linhas abaixo da diagonal
            L[i, k] = U[i, k] / U[k, k]  # Calculando os multiplicadores da eliminação e armazenando em L
            U[i, k:] -= L[i, k] * U[k, k:]  # Subtraímos da linha i da matriz U a multiplicação da linha k

    # Retorna as três matrizes: P, L e U que representam a decomposição LU com pivoteamento
    return P, L, U

def resolver_sistema_LU(A, b):
    """
    Resolve o sistema linear Ax = b usando a decomposição LU com pivoteamento parcial.
    A solução é obtida em duas etapas: substituição direta para resolver Ly = Pb e substituição retroativa para resolver Ux = y.
    
    Parâmetros:
    A : np.array
        Matriz quadrada de coeficientes do sistema.
    b : np.array
        Vetor coluna com os termos independentes do sistema.

    Retorno:
    x : np.array
        Vetor solução do sistema.
    """
    # Chamamos a função decomposicao_LU_pivot para obter as matrizes P, L e U a partir de A
    P, L, U = decomposicao_LU_pivot(A)

    # Primeira etapa: resolver Pb = L(Ux) = b. Isso envolve modificar b com a matriz de permutação P.
    b_modificado = np.dot(P, b)  # Aplica a matriz de permutação P ao vetor b, ou seja, b' = P * b

    # Segunda etapa: resolver Ly = Pb (substituição direta)
    # O vetor y é o vetor intermediário entre Pb e a solução final x
    n = len(b)  # Obtém o número de variáveis (tamanho de b)
    y = np.zeros(n)  # Inicializa o vetor y, que armazenará as soluções intermediárias

    # Realiza a substituição direta para resolver Ly = Pb
    # Para cada linha i, calculamos o valor de y[i] a partir das equações da matriz triangular inferior L
    for i in range(n):  # Passa por todas as linhas de L
        y[i] = b_modificado[i] - np.dot(L[i, :i], y[:i])  # Subtrai a soma dos produtos já calculados para y

    # Terceira etapa: resolver Ux = y (substituição retroativa)
    # O vetor x será calculado da última linha para a primeira, já que U é triangular superior
    x = np.zeros(n)  # Inicializa o vetor x, que armazenará a solução final

    # Realiza a substituição retroativa para resolver Ux = y
    for i in range(n - 1, -1, -1):  # Passa pelas linhas de U de baixo para cima
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]  # Calcula x[i] com base nas equações de U

    # Retorna a solução do sistema, que é o vetor x
    return x










# Explicação Detalhada do Código
# 1. Função decomposicao_LU_pivot
# Esta função realiza a decomposição LU com pivoteamento parcial, que é um método utilizado para decompor uma matriz quadrada 
# 𝐴
# A em duas matrizes triangulares 
# 𝐿
# L (triangular inferior) e 
# 𝑈
# U (triangular superior), com uma matriz de permutação 
# 𝑃
# P para garantir a estabilidade numérica.

# Objetivo: Decompor a matriz 
# 𝐴
# A em 
# 𝐿
# L e 
# 𝑈
# U tal que 
# 𝐴
# =
# 𝑃
# ⋅
# 𝐿
# ⋅
# 𝑈
# A=P⋅L⋅U. Aqui, 
# 𝑃
# P é a matriz de permutação que troca linhas da matriz 
# 𝐴
# A para garantir que o maior valor possível seja usado como pivô (elemento diagonal) para cada etapa da eliminação.

# Processo de Pivoteamento: Em cada iteração do algoritmo, seleciona-se o maior elemento da coluna 
# 𝑘
# k a partir da linha 
# 𝑘
# k até o final para garantir a estabilidade numérica. Esse elemento será o pivô e, caso necessário, as linhas são trocadas para colocá-lo na posição desejada.

# Eliminação: A partir do pivô, elimina-se os elementos abaixo dele na coluna 
# 𝑘
# k para transformar 
# 𝐴
# A em uma matriz triangular superior 
# 𝑈
# U, enquanto a matriz 
# 𝐿
# L acumula os multiplicadores usados durante a eliminação.

# 2. Função resolver_sistema_LU
# Essa função resolve um sistema linear da forma 
# 𝐴
# 𝑥
# =
# 𝑏
# Ax=b utilizando a decomposição LU obtida pela função anterior.

# Etapa 1 (Substituição Direta):

# Primeiro, modificamos o vetor 
# 𝑏
# b pela matriz de permutação 
# 𝑃
# P (calculada na decomposição LU). Isso é feito para garantir que as permutações feitas em 
# 𝐴
# A também sejam refletidas em 
# 𝑏
# b.
# Depois, resolvemos o sistema 
# 𝐿
# 𝑦
# =
# 𝑃
# 𝑏
# Ly=Pb utilizando substituição direta. A matriz 
# 𝐿
# L é triangular inferior, o que permite que resolvamos 
# 𝑦
# y em um único passo linha por linha.
# Etapa 2 (Substituição Retroativa):

# Depois de calcular 
# 𝑦
# y, resolvemos o sistema 
# 𝑈
# 𝑥
# =
# 𝑦
# Ux=y utilizando substituição retroativa, já que 
# 𝑈
# U é triangular superior. Começamos pela última linha e vamos subindo até a primeira, resolvendo para cada variável 
# 𝑥
# [
# 𝑖
# ]
# x[i].
# 3. Como Usar o Código
# Entrada:
# A matriz 
# 𝐴
# A deve ser uma matriz quadrada (ou seja, o número de linhas deve ser igual ao número de colunas). Essa matriz representa os coeficientes do sistema linear.
# O vetor 
# 𝑏
# b deve ser um vetor coluna com os termos independentes do sistema.
# Saída:
# A função resolver_sistema_LU retorna o vetor 
# 𝑥
# x, que é a solução do sistema 
# 𝐴
# 𝑥
# =
# 𝑏
# Ax=b.
# 4. Como Modificar ou Adaptar o Código
# Alterar o método de decomposição: Se você não quiser usar LU com pivoteamento, pode modificar a função decomposicao_LU_pivot para uma decomposição LU sem pivoteamento, removendo a parte do código que realiza a troca de linhas.

# Sistemas não quadrados: O código apresentado funciona apenas para matrizes quadradas. Para sistemas retangulares, é necessário utilizar outras abordagens, como a decomposição QR.

# Estabilidade numérica: O pivoteamento parcial ajuda a evitar problemas numéricos, especialmente em sistemas mal condicionados. Se você quiser implementar o pivoteamento total, que também troca colunas, pode ser feito, mas o algoritmo fica mais complexo.

# 5. Exemplo de Uso
# Para resolver um sistema de equações 
# 𝐴
# 𝑥
# =
# 𝑏
# Ax=b com este código:

# python
# Copiar
# Editar
# A = np.array([[3, -2,  5], [1,  1,  2], [2,  4, -1]], dtype=float)  # Exemplo de matriz A
# b = np.array([1, 2, 3], dtype=float)  # Exemplo de vetor b

# x = resolver_sistema_LU(A, b)  # Resolver o sistema Ax = b

# print("Solução do sistema: ", x)  # Exibe a solução
# Esse código vai resolver o sistema linear utilizando decomposição LU com pivoteamento parcial.

