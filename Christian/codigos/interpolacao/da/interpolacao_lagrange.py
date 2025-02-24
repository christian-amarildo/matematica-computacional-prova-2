# Importação das bibliotecas necessárias
import numpy as np  # Biblioteca NumPy para manipulações numéricas (especialmente arrays e funções matemáticas)
import matplotlib.pyplot as plt  # Biblioteca Matplotlib para criar gráficos e visualizações

# Função para calcular o valor interpolado usando o polinômio de Lagrange
def interpLagrange(xp, x, y):
    """
    Calcula a interpolação polinomial de Lagrange em um ponto específico xp.

    O polinômio de Lagrange é usado para encontrar uma função polinomial que passe
    por todos os pontos dados (x, y) e que possa ser avaliada em outros pontos.

    Parâmetros:
    xp (float): Ponto específico onde a interpolação será avaliada.
    x (list ou array): Lista de valores da variável independente (os x conhecidos).
    y (list ou array): Lista de valores da variável dependente (os f(x) conhecidos).

    Retorna:
    float: Valor interpolado em xp, que é a avaliação do polinômio em xp.
    """
    yp = 0  # Inicializa a variável para armazenar o valor interpolado
    n = len(x)  # Obtém o número de pontos conhecidos (quantidade de elementos em x)

    # Loop sobre cada termo do polinômio de Lagrange
    for k in range(n):
        p = 1  # Inicializa o termo do polinômio de Lagrange para o índice k
        for j in range(n):
            if k != j:
                # Calcula o termo de Lagrange, que é um fator multiplicativo para cada k
                p *= (xp - x[j]) / (x[k] - x[j])  # (xp - x_j) / (x_k - x_j)
        
        # Soma o termo ponderado pelo valor correspondente de y[k]
        yp += p * y[k]  # Pondera o valor y[k] com o termo de Lagrange calculado para k

    return yp  # Retorna o valor interpolado

# Função para construir a forma simbólica do polinômio de Lagrange
def calcular_polinomio_lagrange(x, y):
    """
    Constrói o polinômio interpolador de Lagrange em forma simbólica.

    Essa função cria uma representação simbólica do polinômio interpolador, o qual
    passa por todos os pontos fornecidos (x, y). O polinômio é uma soma de termos
    de Lagrange ponderados pelos valores de y.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente (os x conhecidos).
    y (list ou array): Lista de valores da variável dependente (os f(x) conhecidos).

    Retorna:
    str: Representação formatada do polinômio de Lagrange em formato string.
    """
    n = len(x)  # Obtém o número de pontos (tamanho de x)
    termos = []  # Lista para armazenar cada termo do polinômio

    # Loop sobre cada ponto k para calcular o termo correspondente do polinômio de Lagrange
    for k in range(n):
        numerador = []  # Lista para armazenar os termos (x - x_j)
        denominador = 1  # Inicializa o denominador do termo de Lagrange

        # Loop para calcular os fatores (x - x_j) para o termo de Lagrange
        for j in range(n):
            if k != j:
                numerador.append(f"(x - {x[j]})")  # Adiciona o fator (x - x_j) ao numerador
                denominador *= (x[k] - x[j])  # Multiplica o denominador pela diferença (x_k - x_j)

        # Cria o termo simbólico completo para o ponto k
        termo = f"{y[k]:.6f} * ({' * '.join(numerador)}) / {denominador:.6f}"
        termos.append(termo)  # Adiciona o termo à lista

    # Retorna o polinômio como uma string formatada com todos os termos
    return " + ".join(termos)

# Função para gerar e plotar o gráfico da interpolação polinomial de Lagrange
def plotar_interpolacao(x, y, xp, yp):
    """
    Plota a interpolação polinomial de Lagrange junto com os pontos fornecidos.

    A função gera um gráfico da função interpoladora de Lagrange e destaca os pontos
    originais, bem como o ponto no qual a interpolação foi realizada.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente (os x conhecidos).
    y (list ou array): Lista de valores da variável dependente (os f(x) conhecidos).
    xp (float): Ponto específico onde foi realizada a interpolação (o ponto x no qual a interpolação foi realizada).
    yp (float): Valor interpolado em xp, ou seja, f(xp), que foi calculado pela interpolação.
    """
    # Gerando valores para a curva interpoladora, criando uma linha com mais pontos para visualização suave
    t = np.linspace(min(x), max(x), len(x) + (len(x)-1)*3000)  # Gera uma sequência de pontos entre o valor mínimo e máximo de x
    yt = [interpLagrange(i, x, y) for i in t]  # Calcula os valores interpolados para cada ponto de t usando interpLagrange

    # Criando o gráfico
    plt.figure(figsize=(8, 6))  # Configura o tamanho da figura
    plt.plot(t, yt, 'b-', label="Polinômio de Lagrange")  # Plota a linha do polinômio interpolador (em azul)
    plt.scatter(x, y, color='red', marker='o', s=100, label="Pontos Originais")  # Plota os pontos reais (em vermelho)
    plt.scatter(xp, yp, color='green', marker='x', s=150, label=f"Interpolado em x={xp}")  # Plota o ponto interpolado (em verde)

    plt.xlabel("x")  # Rótulo do eixo x
    plt.ylabel("f(x)")  # Rótulo do eixo y
    plt.title("Interpolação Polinomial de Lagrange")  # Título do gráfico
    plt.legend()  # Exibe a legenda
    plt.grid(True)  # Exibe a grade no gráfico
    plt.show()  # Exibe o gráfico gerado

# Função para calcular o erro absoluto da interpolação
def calcular_erro(x, y):
    """
    Calcula o erro absoluto entre os valores reais e os valores estimados pela interpolação.

    A função calcula a diferença absoluta entre o valor real f(x) e o valor estimado
    pela interpolação de Lagrange em cada um dos pontos fornecidos.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente (os x conhecidos).
    y (list ou array): Lista de valores da variável dependente (os f(x) conhecidos).

    Retorna:
    list: Lista de erros absolutos para cada ponto, ou seja, |f(x) real - f(x) estimado|
    """
    erros = []  # Lista para armazenar os erros
    estimados = []  # Lista para armazenar os valores estimados

    # Loop sobre cada ponto
    for i in range(len(x)):
        estimado = interpLagrange(x[i], x, y)  # Calcula o valor estimado de f(x) usando a interpolação
        erro = abs(estimado - y[i])  # Calcula o erro absoluto entre o valor real e o estimado
        erros.append(erro)  # Adiciona o erro à lista
        estimados.append(estimado)  # Adiciona o valor estimado à lista

    return erros, estimados  # Retorna as listas de erros e estimados

# Função para exibir os detalhes da interpolação
def mostrar_detalhes(x, y, xp, yp, exibir_polinomio=False):
    """
    Exibe detalhes da interpolação, mostrando os valores de x, y, erros e o polinômio interpolador.

    A função imprime uma tabela com os pontos reais, seus valores, os valores estimados
    pela interpolação e os erros absolutos. Também exibe o valor interpolado em xp.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente (os x conhecidos).
    y (list ou array): Lista de valores da variável dependente (os f(x) conhecidos).
    xp (float): Ponto onde foi realizada a interpolação (o ponto x no qual a interpolação foi realizada).
    yp (float): Valor interpolado em xp, ou seja, f(xp), que foi calculado pela interpolação.
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
        polinomio = calcular_polinomio_lagrange(x, y)  # Gera a representação simbólica do polinômio de Lagrange
        print("\n=== Polinômio Interpolador de Lagrange ===")
        print(f"P(x) = {polinomio}")  # Exibe o polinômio

# === TESTE RÁPIDO: BASTA ALTERAR ESTES VALORES ===
# Aqui você pode modificar os pontos conhecidos e o ponto a ser interpolado

x_pontos = [-1, 0, 1, 2, 3]  # Modifique aqui os valores de x (os pontos conhecidos)
y_pontos = [0, 1, -1, 2, 7]  # Modifique aqui os valores de f(x) (os valores correspondentes de y)
xp_teste = 1.5  # Modifique aqui o ponto em que deseja interpolar (xp)
exibir_grafico = True  # Escolha se deseja ver o gráfico (True ou False)
exibir_polinomio = True  # Escolha se deseja ver o polinômio (True ou False)

# Testando a interpolação em xp_teste
yp_teste = interpLagrange(xp_teste, x_pontos, y_pontos)

# Exibindo detalhes da interpolação, erros e valor interpolado
mostrar_detalhes(x_pontos, y_pontos, xp_teste, yp_teste, exibir_polinomio)

# Gerando o gráfico (se o usuário quiser)
if exibir_grafico:
    plotar_interpolacao(x_pontos, y_pontos, xp_teste, yp_teste)








  
# Explicação:
# Interpolação de Lagrange: O código implementa a técnica de interpolação polinomial de Lagrange. Esta técnica constrói um polinômio de grau 
# 𝑛
# −
# 1
# n−1 que passa por todos os pontos fornecidos 
# (
# 𝑥
# 1
# ,
# 𝑦
# 1
# )
# ,
# (
# 𝑥
# 2
# ,
# 𝑦
# 2
# )
# ,
# …
# (x 
# 1
# ​
#  ,y 
# 1
# ​
#  ),(x 
# 2
# ​
#  ,y 
# 2
# ​
#  ),…. O polinômio resultante é usado para estimar valores de 
# 𝑓
# (
# 𝑥
# )
# f(x) em pontos intermediários.

# Funções:

# interpLagrange: Calcula o valor do polinômio interpolador de Lagrange em um ponto 
# 𝑥
# 𝑝
# x 
# p
# ​
#  .
# calcular_polinomio_lagrange: Gera uma representação simbólica do polinômio interpolador.
# plotar_interpolacao: Gera um gráfico que mostra os pontos originais e o polinômio interpolador.
# calcular_erro: Calcula o erro absoluto entre os valores reais e os valores estimados pela interpolação.
# mostrar_detalhes: Exibe detalhes sobre a interpolação, incluindo erros, valores estimados e o polinômio simbólico (se solicitado).
# Uso:

# Você pode modificar a lista x_pontos para os pontos 
# 𝑥
# x conhecidos, e a lista y_pontos para os valores de 
# 𝑓
# (
# 𝑥
# )
# f(x) correspondentes.
# Defina xp_teste para o ponto onde você quer avaliar o polinômio.
# Controle se deseja gerar o gráfico e ver o polinômio definindo exibir_grafico e exibir_polinomio.
