from interpolacao import gerar_pontos

def integral_pontos(xData, yData):
    res = 0
    for i in range(1, len(xData)):
        h = xData[i] - xData[i - 1]
        res += ((yData[i] + yData[i - 1]) * h) / 2
    return res

def integral_funcao(fn, limA, limB, n):
    h = (limB - limA) / n
    res = (fn(limA) + fn(limB)) / 2

    for i in range(1, n):
        res += fn(limA + i * h)
    res *= h
    return res


xData, yData = gerar_pontos(0, 5, [lambda x: x**2], pulo=0.00001)

res = integral_pontos(xData, yData)

print(res)
print((5**3 / 3) - (0**3 / 3))