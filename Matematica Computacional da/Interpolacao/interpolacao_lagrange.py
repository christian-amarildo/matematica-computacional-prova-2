# Importação das bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

def interpLagrange(xp, x, y):
    """
    Calcula a interpolação polinomial de Lagrange em um ponto específico xp.

    Parâmetros:
    xp (float): Ponto no qual a interpolação será avaliada.
    x (list ou array): Lista de valores da variável independente.
    y (list ou array): Lista de valores da variável dependente.

    Retorna:
    float: Valor interpolado em xp.
    """
    yp = 0
    n = len(x)  # Determina o grau do polinômio baseado no número de pontos
    
    for k in range(n):
        p = 1  # Inicializa o termo do polinômio de Lagrange
        for j in range(n):
            if k != j:
                p *= (xp - x[j]) / (x[k] - x[j])  # Calcula o termo de Lagrange
        
        yp += p * y[k]  # Soma os termos ponderados pelos valores de y

    return yp

def calcular_polinomio_lagrange(x, y):
    """
    Constrói o polinômio interpolador de Lagrange em forma simbólica.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    y (list ou array): Lista de valores da variável dependente.

    Retorna:
    str: Representação formatada do polinômio de Lagrange.
    """
    n = len(x)
    termos = []

    for k in range(n):
        numerador = []
        denominador = 1
        for j in range(n):
            if k != j:
                numerador.append(f"(x - {x[j]})")
                denominador *= (x[k] - x[j])

        termo = f"{y[k]:.6f} * ({' * '.join(numerador)}) / {denominador:.6f}"
        termos.append(termo)

    return " + ".join(termos)

def plotar_interpolacao(x, y, xp, yp):
    """
    Plota a interpolação polinomial de Lagrange junto com os pontos fornecidos.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    y (list ou array): Lista de valores da variável dependente.
    xp (float): Ponto específico onde foi realizada a interpolação.
    yp (float): Valor interpolado em xp.
    """
    # Gerando valores para a curva interpoladora
    t = np.linspace(min(x), max(x), len(x) + (len(x)-1)*3000)
    yt = [interpLagrange(i, x, y) for i in t]

    # Criando o gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(t, yt, 'b-', label="Polinômio de Lagrange")  # Linha do polinômio
    plt.scatter(x, y, color='red', marker='o', s=100, label="Pontos Originais")  # Pontos reais (maiores)
    plt.scatter(xp, yp, color='green', marker='x', s=150, label=f"Interpolado em x={xp}")  # Ponto interpolado
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Interpolação Polinomial de Lagrange")
    plt.legend()
    plt.grid(True)
    plt.show()

    

def calcular_erro(x, y):
    """
    Calcula o erro absoluto entre os valores reais e os valores estimados.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    y (list ou array): Lista de valores da variável dependente.

    Retorna:
    list: Lista de erros absolutos para cada ponto.
    """
    erros = []
    estimados = []

    for i in range(len(x)):
        estimado = interpLagrange(x[i], x, y)  # Calcula o valor estimado no ponto original
        erro = abs(estimado - y[i])  # Calcula o erro absoluto
        erros.append(erro)
        estimados.append(estimado)

    return erros, estimados

def mostrar_detalhes(x, y, xp, yp, exibir_polinomio=False):
    """
    Exibe detalhes da interpolação, mostrando os valores de x, y, erros e o polinômio interpolador.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    y (list ou array): Lista de valores da variável dependente.
    xp (float): Ponto onde foi realizada a interpolação.
    yp (float): Valor interpolado.
    exibir_polinomio (bool): Se True, exibe a representação simbólica do polinômio de Lagrange.
    """
    erros, estimados = calcular_erro(x, y)  # Calcula os erros

    print("\n=== Detalhes da Interpolação ===")
    print("Pontos conhecidos:")
    for i in range(len(x)):
        print(f"x = {x[i]:.6f} | f(x) real = {y[i]:.6f} | f(x) estimado = {estimados[i]:.6f} | Erro = {erros[i]:.6e}")
    
    print(f"\nInterpolação realizada em x = {xp:.6f}")
    print(f"Valor interpolado: f({xp:.6f}) = {yp:.6f}")

    if exibir_polinomio:
        polinomio = calcular_polinomio_lagrange(x, y)
        print("\n=== Polinômio Interpolador de Lagrange ===")
        print(f"P(x) = {polinomio}")

# === TESTE RÁPIDO: BASTA ALTERAR ESTES VALORES ===
x_pontos = [-1, 0, 1,2, 3]  # Modifique aqui os valores de x
y_pontos = [0, 1, -1, 2,7]  # Modifique aqui os valores de f(x)
xp_teste = 1.5  # Modifique aqui o ponto a ser interpolado
exibir_grafico = True  # Escolha se deseja ver o gráfico (True ou False)
exibir_polinomio = True  # Escolha se deseja ver o polinômio (True ou False)

# Testando a interpolação
yp_teste = interpLagrange(xp_teste, x_pontos, y_pontos)

# Exibindo detalhes e erro
mostrar_detalhes(x_pontos, y_pontos, xp_teste, yp_teste, exibir_polinomio)

# Gerando o gráfico (se o usuário quiser)
if exibir_grafico:
    plotar_interpolacao(x_pontos, y_pontos, xp_teste, yp_teste)
