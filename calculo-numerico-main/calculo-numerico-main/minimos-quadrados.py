import math


def ler_dados_de_arquivo():
    with open("entrada-pontos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    n = int(linhas[0])  # Número de linhas da matriz
    pontosXY = []

    for i in range(1, n + 1):
        pontos = list(map(float, linhas[i].split()))
        pontosXY.append(pontos)
    
    return n, pontosXY


def imprimir_array(array):
    print("\n")
    for linha in array:
        print("\t".join(map(str, linha)))
    print("\n")


def imprimir_resultado(coeficientes, desvio_padrao, tipo="linear"):
    print("\n")
    print("Função", tipo)
    print("Coeficientes:", coeficientes)
    if (tipo == "linear"):
        print(f"{coeficientes[1]}x + {coeficientes[0]}")

    if (tipo == "quadratica"):
        print(f"{coeficientes[2]}x² + {coeficientes[1]}x + {coeficientes[0]}")

    if (tipo == "exponencial-simples"):
        print(f"{coeficientes[0]} e^{coeficientes[1]}x")

    if (tipo == "exponencial-produto"):
        print(f"{coeficientes[1]} xe^{coeficientes[0]}x")


    print(f"Desvio padrao: {desvio_padrao} \n\n")



def resolve_sistema_gauss_seidel(matriz, b, x0, epsilon=1e-8, max_iter=1000):

    n = len(matriz)
    x = x0.copy()
    
    iteracoes = 0
    while iteracoes < max_iter:
        iteracoes += 1
        x_antigo = x.copy()

        for lin in range(n):
            soma = 0
            for col in range(n):
                if col != lin:
                    soma += matriz[lin][col] * x[col] / matriz[lin][lin]
                    
                x[lin] = (b[lin] / matriz[lin][lin]) - soma

        # Cálculo da diferença relativa em norma infinito
        diff_rel = max(abs(x[i] - x_antigo[i]) / abs(x[i]) for i in range(n))
        
        if diff_rel < epsilon or iteracoes == max_iter:
            return [round(xi, 9) for xi in x]
        
    return None  # Falha




def minimos_quadrados_linear(num_pontos, pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]

    somatorio_x = sum(x)
    somatorio_y = sum(y)
    somatorio_x2 = sum(xi**2 for xi in x)

    somatorio_xy = 0
    for xy in pontos:
        somatorio_xy += xy[0] * xy[1]


    #print([num_pontos, somatorio_x, somatorio_y])
    #print([somatorio_x, somatorio_x2, somatorio_xy])

    # Calcula os coeficientes a0 e a1
    a1 = (num_pontos * somatorio_xy - somatorio_x * somatorio_y) / (num_pontos * somatorio_x2 - somatorio_x**2)
    a0 = (somatorio_y - a1 * somatorio_x) / num_pontos

    # Calcula os valores preditos y_pred
    y_pred = [a0 + a1 * xi for xi in x]

    # Calcula os resíduos
    residuos = [yi - y_predi for yi, y_predi in zip(y, y_pred)]

    # Calcula a raiz da média quadrática dos resíduos
    desvio_padrao = (sum(residual**2 for residual in residuos) / num_pontos)**0.5

    return [a0, a1], desvio_padrao


def calcular_regressao_quadratica(num_pontos, pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]

    somatorio_x = sum(x)
    somatorio_y = sum(y)
    somatorio_x2 = sum(xi**2 for xi in x)
    somatorio_x3 = sum(xi**3 for xi in x)
    somatorio_x4 = sum(xi**4 for xi in x)
    
    somatorio_xy = 0
    for ponto in pontos:
        somatorio_xy += ponto[0] * ponto[1]

    somatorio_x2y = 0
    for ponto in pontos:
        somatorio_x2y += ponto[0] * ponto[0] * ponto[1]


    # Resolve o sistema linear
    coeficientes = resolve_sistema_gauss_seidel(
        [
            [num_pontos, somatorio_x, somatorio_x2],
            [somatorio_x, somatorio_x2, somatorio_x3],
            [somatorio_x2, somatorio_x3, somatorio_x4],
        ],
        [somatorio_y, somatorio_xy, somatorio_x2y],
        [0, 0, 0]
    )

    # Calcula os valores preditos y_pred
    y_pred = [(coeficientes[0] + coeficientes[1] * xi + coeficientes[2] * xi**2) for xi in x]

    # Calcula os resíduos
    residuos = []
    for i in range(0, num_pontos):  # estava percorrendo de 0 até 3 só
        residuos.append(y[i] - y_pred[i])

    # Calcula a raiz da média quadrática dos resíduos
    desvio_padrao = (sum(residual**2 for residual in residuos) / num_pontos) ** (1/2)


    return coeficientes, desvio_padrao


def minimos_quadrados_exponencial(num_pontos, pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]

    # Aplica o logaritmo natural aos valores de y para linearizar
    y_log = [math.log(yi) for yi in y]

    novos_pontos = []
    for i in range(num_pontos):
        novos_pontos.append([x[i], y_log[i]])

    # Calcula os coeficientes a0' e a1' com a função linearizada
    coeficientes_log, desvio_padrao = minimos_quadrados_linear(num_pontos, novos_pontos)

    # Converte a0' para a0 e mantém a1 inalterado
    a0 = math.exp(coeficientes_log[0])
    a1 = coeficientes_log[1]

    return [a0, a1], desvio_padrao


def minimos_quadrados_produto_exponencial(num_pontos, pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]

    # Aplica o logaritmo natural aos valores de x e y para linearizar
    x_log = [math.log(xi) for xi in x]
    y_log = [math.log(yi) for yi in y]

    novos_pontos = []
    for i in range(num_pontos):
        novos_pontos.append([x_log[i], y_log[i]])

    # Calcula os coeficientes a0' e a1' com a função linearizada
    coeficientes_log, desvio_padrao = minimos_quadrados_linear(num_pontos, novos_pontos)

    # Converte ln de a0 para a0 e mantém a1 inalterado
    a0 = math.exp(coeficientes_log[0])
    a1 = coeficientes_log[1]

    return [a0, a1], desvio_padrao


def minimos_quadrados_soma_exponencial(num_pontos, pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]

    # Linearização do termo a0e^x
    exp_positivo_linearizado = [math.log(a0) - xi for xi, a0 in zip(x, y)]

    # Linearização do termo a1e^{-x}
    exp_negativo_linearizado = [math.log(a1) - xi for xi, a1 in zip(x, y)]

    # Construção da matriz X
    X = [[1, xi] for xi in x]

    # Adição das partes linearizadas à matriz X
    for i in range(num_pontos):
        X[i].append(exp_positivo_linearizado[i])
        X[i].append(exp_negativo_linearizado[i])

    print('X', X)
    # Calcula os coeficientes a0', a1', a2'
    coeficientes_log, desvio_padrao = minimos_quadrados_linear(num_pontos, X, y)

    # Converte a0' e a1' para a0 e a1
    a0 = math.exp(coeficientes_log[0])
    a1 = coeficientes_log[1]

    return [a0, a1], desvio_padrao


def minimos_quadrados_exponencial_inversa(num_pontos, pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]

    # Linearização do termo a0e^x
    exp_positivo_linearizado = [math.log(a0) - xi for xi, a0 in zip(x, y)]

    # Linearização do termo a1e^{-x}
    exp_negativo_linearizado = [math.log(a1) - xi for xi, a1 in zip(x, y)]

    # Construção da matriz X
    X = [[1, xi] for xi in x]

    # Adição das partes linearizadas à matriz X
    for i in range(num_pontos):
        X[i].append(exp_positivo_linearizado[i])
        X[i].append(exp_negativo_linearizado[i])

    print('X', X)
    # Calcula os coeficientes a0', a1', a2'
    coeficientes_log, desvio_padrao = minimos_quadrados_linear(num_pontos, X, y)

    # Converte a0' e a1' para a0 e a1
    a0 = math.exp(coeficientes_log[0])
    a1 = coeficientes_log[1]

    return [a0, a1], desvio_padrao



n, pontosXY = ler_dados_de_arquivo()

print("Pontos lidos:")
imprimir_array(pontosXY)


coeficientes, desvio_padrao = minimos_quadrados_linear(n, pontosXY)
imprimir_resultado(coeficientes, desvio_padrao)


coeficientes, desvio_padrao = calcular_regressao_quadratica(n, pontosXY)
imprimir_resultado(coeficientes, desvio_padrao, "quadratica")


coeficientes, desvio_padrao = minimos_quadrados_exponencial(n, pontosXY)
imprimir_resultado(coeficientes, desvio_padrao, "exponencial-simples")


coeficientes, desvio = minimos_quadrados_produto_exponencial(n, pontosXY)
imprimir_resultado(coeficientes, desvio, "exponencial-produto")


#coeficientes, desvio = minimos_quadrados_soma_exponencial(n, pontosXY)
#imprimir_resultado(coeficientes, desvio, "exponencial-soma")


#coeficientes, desvio = minimos_quadrados_exponencial_inversa(n, pontosXY)
#imprimir_resultado(coeficientes, desvio, "exponencial-inversa")

