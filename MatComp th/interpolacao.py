from sistemasLineares import resolver_sistema
from ajusteCurva import gerar_grafico
from math import sin, asin, log, e

import matplotlib.pyplot as plt

def matriz_vandermonde(xData, yData):
    matriz = []
    for i in range(len(xData)):
        linha = [xData[i]**n for n in range(len(xData))]
        linha.append(yData[i])
        matriz.append(linha)
    return matriz

def lagrange(x, xData, yData):
    res = 0
    for i in range(len(xData)):
        lagrange = yData[i]
        for j in range(len(xData)):
            if i != j:
                lagrange *= (x - xData[j]) / (xData[i] - xData[j])
        res += lagrange
    return res

def newton(x, xData, yData):
    tam = len(xData)
    F = [[0] * tam for _ in range(tam)]
    for i in range(tam):
        F[i][0] = yData[i]

    for j in range(1, tam):
        for i in range(tam - j):
            F[i][j] = (F[i+1][j-1] - F[i][j-1]) / (xData[i+j] - xData[i])

    res = F[0][0]
    for j in range(1, tam):
        termo = F[0][j]
        for k in range(j):
            termo *= (x - xData[k])
        res += termo
    return res


def gerar_pontos(limA, limB, fn, pulo=0.1):
    newXData = []
    newYData = []
    x = limA
    while x < limB:
        newXData.append(x)
        y = 0
        for n in range(len(fn)):
            y += fn[n](x)
        newYData.append(y)
        x += pulo
    return newXData, newYData


def interpolar(xData, yData, limA, limB, pulo=0.1, metodo=0):
    newXData = []
    newYData = []
    alphas = []

    if metodo == 0:
        matriz = matriz_vandermonde(xData, yData)
        alphas = resolver_sistema(matriz)

    x = limA
    while x < limB:
        newXData.append(x)
        y = 0
        if metodo == 0:
            for n in range(len(alphas)):
                y += alphas[n] * (x ** n)
        elif metodo == 1:
            y = lagrange(x, xData, yData)
        else:
            y = newton(x, xData, yData)
        newYData.append(y)
        x += pulo
    return newXData, newYData


def interpolacao_reversa(y, xData, yData, metodo=0):
    if metodo == 0:
        x = lagrange(y, yData, xData)
    else:
        x = newton(y, yData, xData)
    return x



xData = [-1, 0, 2, 4, 7]
yData = [4, 1, -1, 2.333, 17.331]

matriz = matriz_vandermonde(xData, yData)
alphas = resolver_sistema(matriz)
print(alphas)

newXData, newYData = interpolar(xData, yData, -1, 7, metodo=2, pulo=0.1)
print(newYData)

gerar_grafico(xData, yData, newXData, newYData)

def f(x):
    return sin(x)

x_data = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
y_data = [f(x) for x in x_data]

y = 0.5
x = interpolacao_reversa(y, y_data, x_data, metodo=0)
print(x, asin(y))