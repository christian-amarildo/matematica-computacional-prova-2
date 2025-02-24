import numpy as np

def resolver_sistema_linear(A, b):
    """
    Resolve o sistema linear Ax = b usando o método de eliminação de Gauss
    seguido de substituição regressiva.

    Este método é usado para resolver sistemas lineares de equações na forma 
    Ax = b, onde A é uma matriz quadrada (de coeficientes) e b é um vetor 
    coluna (de termos independentes). A solução x é o vetor solução.

    A eliminação de Gauss envolve manipular a matriz A para transformá-la em 
    uma forma triangular superior, a partir da qual podemos resolver as equações
    por substituição regressiva.

    Parâmetros:
    A (numpy.ndarray): Matriz quadrada dos coeficientes do sistema (n x n).
    b (numpy.ndarray): Vetor coluna de termos independentes (n x 1).

    Retorna:
    numpy.ndarray: Vetor solução x do sistema Ax = b.

    Exemplo de uso:
    A = np.array([[2, 1, -1], [3, 3, 1], [1, 2, 2]], dtype=float)
    b = np.array([8, 18, 7], dtype=float)
    x = resolver_sistema_linear(A, b)
    print(x)  # Isso deve imprimir a solução do sistema.
    """
    # Garantir que A e b sejam arrays numpy de tipo float (ponto flutuante)
    A = A.astype(float)  # Converte a matriz A para tipo float se não for
    b = b.astype(float)  # Converte o vetor b para tipo float se não for

    n = len(b)  # O número de equações (ou o tamanho do vetor b) é o tamanho da matriz A

    # Etapa 1: Eliminação de Gauss
    for i in range(n):  # Laço para percorrer cada coluna da matriz A
        # Pivoteamento parcial (necessário para evitar divisão por zero e melhorar a estabilidade numérica)
        # Procura o maior valor absoluto na coluna i, a partir da linha i até a última linha
        max_row = np.argmax(np.abs(A[i:, i])) + i  # np.argmax retorna o índice do maior valor em uma parte da matriz
        if A[max_row, i] == 0:
            # Caso o maior valor absoluto na coluna seja zero, o sistema não tem solução única
            raise ValueError("Sistema sem solução ou com infinitas soluções.")

        # Troca de linhas, se necessário, para colocar o maior valor na diagonal
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]  # Troca as linhas i e max_row na matriz A
            b[[i, max_row]] = b[[max_row, i]]  # Troca as linhas i e max_row no vetor b

        # Agora, faremos a eliminação de Gauss: zerar os elementos abaixo da diagonal
        for j in range(i+1, n):  # Começando da linha abaixo da linha atual i
            # Fator de eliminação (para zerar o elemento A[j, i])
            fator = A[j, i] / A[i, i]  # Calcula o fator de multiplicação para eliminar A[j, i]
            A[j, i:] -= fator * A[i, i:]  # Subtrai da linha j um múltiplo da linha i
            b[j] -= fator * b[i]  # Subtrai do vetor b o mesmo múltiplo de b[i]

    # Nesse ponto, a matriz A se tornou uma matriz triangular superior, e a matriz b foi modificada
    # de acordo com os passos de eliminação. Agora, podemos resolver o sistema usando substituição regressiva.

    # Etapa 2: Substituição regressiva
    x = np.zeros(n)  # Inicializa o vetor solução x com zeros (solução inicial)
    
    # Começamos da última linha e vamos subindo, resolvendo para cada variável
    for i in range(n-1, -1, -1):  # Laço de i = n-1 até 0 (linha n-1 até a linha 0)
        # Substituição regressiva:
        # Para cada linha i, calcula o valor de x[i] a partir de b[i] e dos valores de x já calculados
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]  # Realiza a substituição regressiva
        
        # A fórmula (b[i] - np.dot(A[i, i+1:], x[i+1:])) calcula a soma dos produtos dos coeficientes
        # já resolvidos de x, subtrai de b[i], e depois divide pelo coeficiente A[i, i] para encontrar x[i].

    return x  # Retorna o vetor solução x, que contém as soluções das variáveis do sistema.






  
# O que este código faz:
# Método de Eliminação de Gauss:

# A função resolve um sistema linear da forma 
# 𝐴
# 𝑥
# =
# 𝑏
# Ax=b, onde 
# 𝐴
# A é uma matriz dos coeficientes e 
# 𝑏
# b é o vetor dos termos independentes.
# O método de eliminar Gauss transforma a matriz 
# 𝐴
# A em uma forma triangular superior, de modo que a solução de 
# 𝑥
# x pode ser obtida por substituição regressiva (começando da última linha para a primeira).
# Pivoteamento Parcial:

# O pivoteamento parcial é utilizado para aumentar a estabilidade numérica durante a eliminação de Gauss. Ele troca as linhas de 
# 𝐴
# A para garantir que o maior valor absoluto em cada coluna esteja na diagonal principal antes de realizar as operações de eliminação.
# Isso ajuda a evitar erros de precisão quando os elementos da matriz 
# 𝐴
# A são muito pequenos.
# Substituição Regressiva:

# Após a eliminação de Gauss, a matriz 
# 𝐴
# A se torna triangular superior (ou seja, todos os elementos abaixo da diagonal principal são zero). O sistema resultante é fácil de resolver por substituição regressiva:
# Começamos da última equação (última linha) e resolvemos para a última variável.
# Depois substituímos esse valor nas equações anteriores, resolvendo para cada variável.
# Saída:

# O resultado da função é o vetor 
# 𝑥
# x, que contém as soluções do sistema linear.
# Como usar o código:
# Para usar a função resolver_sistema_linear, você precisa fornecer:
# A: Uma matriz quadrada 
# 𝑛
# ×
# 𝑛
# n×n de coeficientes do sistema linear.
# b: Um vetor coluna 
# 𝑛
# ×
# 1
# n×1 contendo os termos independentes do sistema.
# Exemplo de uso:
# python
# Copiar
# Editar
# # Definir a matriz A (coeficientes do sistema)
# A = np.array([[2, 1, -1], 
#               [3, 3, 1], 
#               [1, 2, 2]], dtype=float)

# # Definir o vetor b (termos independentes)
# b = np.array([8, 18, 7], dtype=float)

# # Chamar a função para resolver o sistema
# x = resolver_sistema_linear(A, b)

# # Exibir a solução
# print(x)
# Saída esperada:

# python
# Copiar
# Editar
# [2. 3. -1.]
# Isso significa que a solução do sistema é:

# 𝑥
# 1
# =
# 2
# x 
# 1
# ​
#  =2
# 𝑥
# 2
# =
# 3
# x 
# 2
# ​
#  =3
# 𝑥
# 3
# =
# −
# 1
# x 
# 3
# ​
#  =−1
# O que você pode modificar:
# Matriz 
# 𝐴
# A:

# Alterar a matriz 
# 𝐴
# A com os coeficientes do seu próprio sistema linear.
# Por exemplo, se o seu sistema tiver 4 equações com 4 incógnitas, você pode criar uma matriz 4x4.
# Vetor 
# 𝑏
# b:

# O vetor 
# 𝑏
# b contém os termos independentes de cada equação.
# Certifique-se de que 
# 𝑏
# b tenha o mesmo número de elementos que o número de linhas (ou colunas) de 
# 𝐴
# A.
# Verificação de Erros:

# Se a matriz 
# 𝐴
# A for singular (não invertível) ou o sistema não tiver uma solução única, o código irá levantar um erro: ValueError: Sistema sem solução ou com infinitas soluções.. Isso ocorre quando a matriz 
# 𝐴
# A tem uma linha de zeros (ou quando a solução do sistema é indeterminada).
# Eficiência:

# Este método é eficiente para sistemas de tamanho moderado. Para sistemas muito grandes, existem outros métodos numéricos mais avançados (como decomposições LU, QR, ou métodos iterativos) que são mais eficientes.
