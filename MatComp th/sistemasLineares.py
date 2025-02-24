import random as rd

def gerar_matriz_identidade(tam_matriz):
    matriz = []
    for i in range(tam_matriz):
        linha = []
        for j in range(tam_matriz):
            if i != j:
                linha.append(0)
            else:
                linha.append(1)
        matriz.append(linha)
    return matriz


def resolver_matriz_triangular(matriz):
    tam_matriz = len(matriz)

    variaveis = [0] * tam_matriz
    num_variaveis = 0
    for i in range(tam_matriz - 1, -1, -1):
        var = matriz[i][tam_matriz]
        for j in range(num_variaveis):
            var -= matriz[i][tam_matriz - 1 - j] * variaveis[tam_matriz - 1 - j]
        variaveis[i] = var / matriz[i][tam_matriz - 1 - num_variaveis]
        num_variaveis += 1
    return variaveis

def eliminacao_gauss(matriz):
    tam_matriz = len(matriz)

    for i in range(tam_matriz - 1):
        # Coeficiente da variavel
        for j in range(i + 1, tam_matriz):
            const = matriz[j][i] / matriz[i][i]
            for k in range(tam_matriz + 1):
                # Multiplicar a linha pelo termo que zere o coeficiente
                matriz[j][k] -= const * matriz[i][k]
    return matriz

def fatoracao_lu(matriz):
    tam_matriz = len(matriz)

    matriz_u = matriz.copy()
    matriz_l = gerar_matriz_identidade(tam_matriz)
    matriz_p = matriz_l.copy()

    for i in range(tam_matriz - 1):
        max = i
        for j in range(i + 1, tam_matriz):
            if abs(matriz_u[j][i]) > abs(matriz_u[max][i]):
                max = j

        if max != i:
            matriz_u[[i, max]] = matriz_u[[max, i]]
            for j in range(tam_matriz):
                matriz_u[i][j], matriz_u[max][j] = matriz_u[max][j], matriz_u[i][j]
            for j in range(tam_matriz):
                matriz_p[i][j], matriz_p[max][j] = matriz_p[max][j], matriz_p[i][j]

            for j in range(i):
                matriz_l[i][j] , matriz_l[max][j] = matriz_l[max][j], matriz_l[i][j]

        for j in range(i + 1, tam_matriz):
            matriz_l[j][i] = matriz_u[j][i] / matriz_u[i][i]
            for k in range(i, tam_matriz):
                matriz_u[j][k] -= matriz_l[j][i] * matriz_u[i][k]
    return matriz_l, matriz_u, matriz_p

def resolver_lu(matriz):
    tam_matriz = len(matriz)
    matriz_l, matriz_u, matriz_p = fatoracao_lu(matriz)

    res_permutado = []
    for i in range(tam_matriz):
        sum = 0
        for j in range(tam_matriz):
            sum += matriz[i][tam_matriz] * matriz_p[j][i]
        res_permutado.append(sum)


    vars = [0] * tam_matriz
    for i in range(tam_matriz):
        vars[i] = res_permutado[i]
        for j in range(i):
            vars[i] -= matriz_l[i][j] * vars[j]

    variaveis = [0] * tam_matriz
    for i in range(tam_matriz - 1, -1, -1):
        variaveis[i] = vars[i]
        for j in range(i + 1, tam_matriz):
            variaveis[i] -= matriz_u[i][j] * variaveis[j]
        variaveis[i] /= matriz_u[i][i]
    return variaveis


def gauss_jacobi(matriz, aprox):
    tam_matriz = len(matriz)

    alpha = 0
    for i in range(tam_matriz):
        soma = 0
        for j in range(tam_matriz):
            if i != j:
                soma += matriz[i][j]
        if (soma / matriz[i][i]) > alpha:
            alpha = soma / matriz[i][i]
    if alpha >= 1:
        return []

    if not aprox:
        aprox = [0] * tam_matriz
    for n in range(1000000):
        teste = aprox[0]
        for i in range(tam_matriz):
            aprox[i] = (matriz[i][tam_matriz] / matriz[i][i])
            for j in range(tam_matriz):
                if i != j:
                    aprox[i] -= (matriz[i][j] / matriz[i][i]) * aprox[j]
        if abs(aprox[0] - teste) < 0.01:
            break
    return aprox

def resolver_sistema(matriz, aprox=[], metodo=0):
    # Resolve um sistema linear
    # Retorna vazio caso a matriz não seja quadrada
    tam_matriz = len(matriz)
    for i in range(tam_matriz):
        if tam_matriz != (len(matriz[i]) - 1):
            return []

    # Seleciona o método de escalonamento da matriz
    match metodo:
        case 0:
            matriz = eliminacao_gauss(matriz)
            resultados = resolver_matriz_triangular(matriz)
        case 1:
            resultados = resolver_lu(matriz)
        case 2:
            resultados = gauss_jacobi(matriz, aprox)

    return resultados


def print_resultado(variaveis):
    for i in range(len(variaveis)):
        print(f'V{i + 1}: {variaveis[i]:.2f}')


def non_zero_random(a, b):
    num = rd.uniform(a, b)
    rd.uniform(a, b)
    while num == 0:
        num = rd.uniform(a, b)
    return num

def gerar_matriz_aleatoria(max_matriz=10, range_num=100):
    tam_matriz = rd.randint(2, max_matriz)
    variaveis = [non_zero_random(-range_num, range_num) for _ in range(tam_matriz)]

    matriz = []
    for i in range(tam_matriz):
        linha = []
        for j in range(tam_matriz):
            coef = non_zero_random(-range_num, range_num)
            linha.append(coef)
        matriz.append(linha)

    for i in range(tam_matriz):
        soma = 0
        for j in range(tam_matriz):
            if i != j:
                soma += abs(matriz[i][j])
        matriz[i][i] = soma + rd.uniform(1, 5)

        res = 0
        for j in range(tam_matriz):
            res += matriz[i][j] * variaveis[j]
        matriz[i].append(res)

    return variaveis, matriz
