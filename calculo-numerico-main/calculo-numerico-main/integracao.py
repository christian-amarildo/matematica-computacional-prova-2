
import math
import numpy as np
import matplotlib.pyplot as plt


def ler_dados_de_arquivo():
    with open("entrada-pontos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    n = int(linhas[0])
    pontosXY = []

    for i in range(1, n + 1):
        pontos = list(map(float, linhas[i].split()))
        pontosXY.append(pontos)
    
    return n, pontosXY


def calcula_por_lagrange(pontos, pontoACalcular):
    nn = len(pontos)
    yp = 0
    for k in range(0, nn):
        p = 1
        for j in range(0, nn):
            if (k != j):
                p = p * (pontoACalcular - pontos[j][0]) / (pontos[k][0] - pontos[j][0])
        yp = yp + p * pontos[k][1]

    return yp



def calcular_regra_retangulo_simples(pontos):
    a = pontos[0][0]
    b = pontos[-1][0]
    x_medio = (a+b)/2

    h = b - a
    fx_medio = calcula_por_lagrange(pontos, x_medio)
    integral = h * fx_medio

    
    #plt.plot([a, x_medio], [a, fx_medio], 'b*')

    return integral

def calcular_regra_trapezio_simples(pontos):
    a = pontos[0][0]
    b = pontos[-1][0]
    h = b - a

    fx_a = calcula_por_lagrange(pontos, a)
    fx_b = calcula_por_lagrange(pontos, b)

    integral = h * (fx_a + fx_b) / 2
    return integral


def calcular_regra_1_3_simpson_simples(pontos):
    a = pontos[0][0]
    b = pontos[-1][0]
    h = (b - a) / 2

    fx_a = calcula_por_lagrange(pontos, a)
    fx_b = calcula_por_lagrange(pontos, b)
    fx_medio = calcula_por_lagrange(pontos, (a+b)/2)

    integral = (h / 3) * (fx_a + 4 * fx_medio + fx_b)
    return integral

def calcular_regra_3_8_simpson_simples(pontos):
    a = pontos[0][0]
    b = pontos[-1][0]
    h = (b - a) / 3

    fx_a = calcula_por_lagrange(pontos, a)
    fx_b = calcula_por_lagrange(pontos, b)
    fx_parte_1 = calcula_por_lagrange(pontos, (a+b)/3)
    fx_parte_2 = calcula_por_lagrange(pontos, (a+b)/3 * 2)

    integral = (3 * h / 8) * (fx_a + 3 * fx_parte_1 + 3 * fx_parte_2 + fx_b)
    return integral


def calcular_regra_retangulo_composta(pontos, n):
    a = pontos[0][0]
    b = pontos[-1][0]

    h = (b - a) / n
    integral = 0

    for i in range(n):
        x_i = a + h*i
        x_i2 = a + h*(i + 1)

        fx_i = calcula_por_lagrange(pontos, (x_i + x_i2)/2)

        integral += h * fx_i

    return integral




def calcular_regra_gaussiana_n2(pontos):
    a = pontos[0][0]
    b = pontos[-1][0]
    c1 = 1
    c2 = 1
    x1 = -math.sqrt(3) / 3 
    x2 = math.sqrt(3) / 3 

    fx_x1 = calcula_por_lagrange(pontos, x1)
    fx_x2 = calcula_por_lagrange(pontos, x2)

    h = (b - a) / 2

    integral = h * (
        c1 * fx_x1 + c2 * fx_x2
    )

    return integral

def calcular_regra_gaussiana_n3(pontos):
    a = pontos[0][0]
    b = pontos[-1][0]
    c1 = 5 / 9
    c2 = 8 / 9
    c3 = 5 / 9
    x1 = - math.sqrt(3 / 5)
    x2 = 1
    x3 = math.sqrt(3 / 5)

    fx_x1 = calcula_por_lagrange(pontos, x1)
    fx_x2 = calcula_por_lagrange(pontos, x2)
    fx_x3 = calcula_por_lagrange(pontos, x3)

    h = (b - a) / 2

    integral = h * (
        c1 * fx_x1 + c2 * fx_x2 + c3 * fx_x3
    )

    return integral

def calcular_regra_gaussiana_n4(pontos):
    a = pontos[0][0]
    b = pontos[-1][0]
    c1 = (18 + math.sqrt(30)) / 36
    c2 = (18 - math.sqrt(30)) / 36
    c3 = (18 - math.sqrt(30)) / 36

    x1 = - math.sqrt((3 + 2 * math.sqrt(6 / 5)) / 7)
    x2 = - math.sqrt((3 - 2 * math.sqrt(6 / 5)) / 7)
    x3 = math.sqrt((3 - 2 * math.sqrt(6 / 5)) / 7)
    x4 = math.sqrt((3 + 2 * math.sqrt(6 / 5)) / 7)

    fx_x1 = calcula_por_lagrange(pontos, x1)
    fx_x2 = calcula_por_lagrange(pontos, x2)
    fx_x3 = calcula_por_lagrange(pontos, x3)
    fx_x4 = calcula_por_lagrange(pontos, x4)

    h = (b - a) / 2

    integral = h * (
        c1 * fx_x1 + c2 * fx_x2 + c3 * fx_x3
    )

    return integral



num_pontos, pontos = ler_dados_de_arquivo()

print("Pontos lidos:")
for ponto in pontos:
    print(ponto)


###### GERANDO GRÁfico
ponto_x_inicial = pontos[0][0]
ponto_x_final = pontos[-1][0]

dominio = np.arange(ponto_x_inicial, ponto_x_final + 0.05, 0.05)

y_calculado = []
for i in dominio:
    y_calculado.append(calcula_por_lagrange(pontos, i))
plt.plot(dominio, y_calculado, 'b-')

x = [ponto[0] for ponto in pontos]
y = [ponto[1] for ponto in pontos]

plt.plot(x, y, 'ro')



print("O valor da integral é:")

integral = calcular_regra_retangulo_simples(pontos)
print(f"Pela regra do retangulo simples: {integral}")

integral = calcular_regra_trapezio_simples(pontos)
print(f"Pela regra do trapezio simples: {integral}")


integral = calcular_regra_1_3_simpson_simples(pontos)
print(f"Pela regra de Simpson 1/3: {integral}")

integral = calcular_regra_3_8_simpson_simples(pontos)
print(f"Pela regra de Simpson 3/8: {integral}")


integral = calcular_regra_trapezio_simples(pontos)
print(f"Pela regra do trapezio simples: {integral}")

integral = calcular_regra_retangulo_composta(pontos, 10)
print(f"Pela regra do retangulo composto com n=10: {integral}")

integral = calcular_regra_retangulo_composta(pontos, 100)
print(f"Pela regra do retangulo composto com n=100: {integral}")

integral = calcular_regra_retangulo_composta(pontos, 1000)
print(f"Pela regra do retangulo composto com n=1000: {integral}")


integral = calcular_regra_gaussiana_n2(pontos)
print(f"Por Gaussiana com n=2: {integral}")

integral = calcular_regra_gaussiana_n3(pontos)
print(f"Por Gaussiana com n=3: {integral}")

integral = calcular_regra_gaussiana_n4(pontos)
print(f"Por Gaussiana com n=4: {integral}")
print('\n\n\n')
plt.show()

