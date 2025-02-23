# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def interpolacao_newton(x, y, x_interpolado):
    """
    Calcula a interpolação polinomial de Newton para um conjunto de pontos.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    y (list ou array): Lista de valores da variável dependente.
    x_interpolado (float): Ponto no qual a interpolação será avaliada.

    Retorna:
    float: Valor interpolado em x_interpolado.
    list: Tabela de diferenças divididas.
    list: Coeficientes do polinômio de Newton.
    """
    n = len(x)  # Número de pontos
    tabela_diferencas = [[None for _ in range(n)] for _ in range(n)]  # Inicializa a tabela de diferenças divididas

    # Preenche a primeira coluna com os valores de y
    for i in range(n):
        tabela_diferencas[i][0] = y[i]

    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            tabela_diferencas[i][j] = (tabela_diferencas[i + 1][j - 1] - tabela_diferencas[i][j - 1]) / (x[i + j] - x[i])

    # Extraindo os coeficientes do polinômio de Newton
    coeficientes = [tabela_diferencas[0][j] for j in range(n)]

    # Avaliação do polinômio interpolador de Newton
    termo_x = 1
    resultado_interpolado = coeficientes[0]

    for ordem in range(1, n):
        termo_x *= (x_interpolado - x[ordem - 1])
        resultado_interpolado += coeficientes[ordem] * termo_x

    return resultado_interpolado, tabela_diferencas, coeficientes

def exibir_tabela_diferencas(x, tabela_diferencas):
    """
    Exibe a tabela de diferenças divididas com mais informações.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    tabela_diferencas (list): Tabela de diferenças divididas gerada pela interpolação de Newton.
    """
    df = pd.DataFrame(tabela_diferencas, columns=[f"Δ^{i}f" for i in range(len(x))])
    df.insert(0, "x", x + ["" for _ in range(len(x) - len(df))])  # Adiciona a coluna x

    print("\n=== Tabela de Diferenças Divididas ===")
    print(df.fillna(''))  # Preenchendo valores vazios para melhor leitura

def exibir_polinomio(coeficientes, x):
    """
    Exibe o polinômio interpolador de forma formatada.

    Parâmetros:
    coeficientes (list): Lista de coeficientes do polinômio.
    x (list): Lista de valores x usados na interpolação.
    """
    termos = [f"{coeficientes[0]:.6f}"]
    
    for i in range(1, len(coeficientes)):
        termo = f"{coeficientes[i]:.6f}"
        for j in range(i):
            termo += f"*(x - {x[j]})"
        termos.append(termo)
    
    print("\n=== Polinômio Interpolador ===")
    print("P(x) =", " + ".join(termos))

def plotar_interpolacao(x, y, x_interpolado, y_interpolado):
    """
    Plota a interpolação polinomial de Newton junto com os pontos fornecidos.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    y (list ou array): Lista de valores da variável dependente.
    x_interpolado (float): Ponto específico onde foi realizada a interpolação.
    y_interpolado (float): Valor interpolado em x_interpolado.
    """
    # Gerando valores para a curva interpoladora
    intervalo_x = np.linspace(min(x) - 1, max(x) + 1, 100)
    intervalo_y = [interpolacao_newton(x, y, i)[0] for i in intervalo_x]

    # Criando o gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(intervalo_x, intervalo_y, 'b-', label="Polinômio de Newton")  # Linha do polinômio
    plt.scatter(x, y, color='red', marker='o', s=100, label="Pontos Originais")  # Pontos reais (maiores)
    plt.scatter(x_interpolado, y_interpolado, color='green', marker='x', s=150, label=f"Interpolado em x={x_interpolado}")  # Ponto interpolado
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Interpolação Polinomial de Newton")
    plt.legend()
    plt.grid(True)
    plt.show()

# === TESTE RÁPIDO: BASTA ALTERAR ESTES VALORES ===
x_pontos = [-1, 0, 2, 3]  # Modifique aqui os valores de x
y_pontos = [4, 1, -1, 2]  # Modifique aqui os valores de f(x)
x_interpolacao = 1.5  # Modifique aqui o ponto a ser interpolado
exibir_grafico = True  # Escolha se deseja ver o gráfico (True ou False)
exibir_tabela = True   # Escolha se deseja ver a tabela de diferenças divididas (True ou False)
exibir_coeficientes = True  # Escolha se deseja ver os coeficientes (True ou False)
exibir_polinomio_completo = True  # Escolha se deseja ver o polinômio completo (True ou False)

# Testando a interpolação
y_interpolacao, tabela_diferencas, coeficientes = interpolacao_newton(x_pontos, y_pontos, x_interpolacao)

# Exibindo os resultados
print(f"\nInterpolação realizada em x = {x_interpolacao:.6f}")
print(f"Valor interpolado: f({x_interpolacao:.6f}) = {y_interpolacao:.6f}")

# Exibir tabela de diferenças divididas (se o usuário quiser)
if exibir_tabela:
    exibir_tabela_diferencas(x_pontos, tabela_diferencas)

# Exibir coeficientes do polinômio (se o usuário quiser)
if exibir_coeficientes:
    print("\n=== Coeficientes do Polinômio ===")
    for i, coef in enumerate(coeficientes):
        print(f"Coeficiente Δ^{i}f: {coef:.6f}")

# Exibir o polinômio completo de forma formatada (se o usuário quiser)
if exibir_polinomio_completo:
    exibir_polinomio(coeficientes, x_pontos)

# Gerar o gráfico (se o usuário quiser)
if exibir_grafico:
    plotar_interpolacao(x_pontos, y_pontos, x_interpolacao, y_interpolacao)
