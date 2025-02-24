import matplotlib.pyplot as plt
from sistemasLineares import resolver_sistema
from random import uniform

def derivada(fn, x, delta=0.0000001):
    return (fn(x + delta) - fn(x)) / delta

def minimo_quadrado(xData, yData, gn):
    sistema = []
    for i in range(len(gn)):
        linha = []
        for j in range(len(gn)):
            res = 0
            for k in range(len(xData)):
                res += gn[i](xData[k])*gn[j](xData[k])
            linha.append(res)

        res = 0
        for k in range(len(xData)):
            res += yData[k] * gn[i](xData[k])
        linha.append(res)
        sistema.append(linha)
    return sistema

def fit_linear(xData, yData, gn, limA, limB, pulo=0.1):
    sistema = minimo_quadrado(xData, yData, gn)
    # TODO: usar implementação própria
    alphas = resolver_sistema(sistema)
    newXData = []
    newYData = []
    x = limA
    while x <= limB:
        res = 0
        for j in range(len(gn)):
            res += gn[j](x) * alphas[j]
        newXData.append(x)
        newYData.append(res)
        x += pulo
    return newXData, newYData, alphas


def gerar_pontos(fn, limA, limB, num_pontos=10):
    pulo = abs(limA - limB) / num_pontos

    xData = []
    yData = []
    x = limA
    while x < limB:
        res = fn(x)
        noiseX = uniform(-1, 1)
        noiseY = uniform(-1, 1)
        xData.append(x)
        yData.append(res + noiseY)
        x = min(x + pulo + noiseX, limB)
    return xData, yData



def gerar_grafico(xData, yData, newXData, newYData):
    fig, ax = plt.subplots()
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)

    ax.scatter(xData, yData, color="red")
    ax.plot(newXData, newYData)

    ax.grid(True)
    plt.show()


# xData, yData = gerar_pontos(lambda x: x**5 - 12*x**2 - 13, 0, 10)
# gn = [lambda x: x**5, lambda x: x**4, lambda x: x**3, lambda x: x**2, lambda x: x, lambda x: 1]
#
# newXData, newYData, alphas = fit_linear(xData, yData, gn, 0, 10)
# gerar_grafico(xData, yData, newXData, newYData)

# fig, ax = plt.subplots()
# ax.scatter(xData, yData, color="red")
# plt.show()

# print(alphas)
