import numpy as np

from sistemasLineares import resolver_sistema

def metodo_newton(funcao, derivada, tam):
    variaveis = [1] * tam
    for _ in range(100000):
        coefs = derivada(variaveis)
        res = funcao(variaveis)

        matriz = []
        for i in range(tam):
            linha = coefs[i]
            linha.append(-res[i])
            matriz.append(linha)

        vars = resolver_sistema(matriz)
        variaveis = [variaveis[i] + vars[i] for i in range(tam)]
    return variaveis

def funcoes(x):
    return [x[0]**2 + x[1]**2 - 4,
            x[0]**2 - x[1] - 1]

def jacob(x):
    return [[2*x[0], 2*x[1]],
            [2*x[1], 1]]

print(metodo_newton(funcoes, jacob, 2))