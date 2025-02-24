# Importação das bibliotecas necessárias
import pandas as pd  # Pandas para criar e manipular tabelas, especialmente a tabela de diferenças divididas.
import numpy as np  # NumPy para manipulações matemáticas e geração de valores contínuos (como o intervalo para o gráfico).
import matplotlib.pyplot as plt  # Matplotlib para plotar gráficos e visualizar a interpolação.

def interpolacao_newton(x, y, x_interpolado):
    """
    Função para calcular a interpolação polinomial de Newton.

    O método de interpolação de Newton é uma forma de obter um polinômio de grau 
    n-1 que passa por todos os pontos (x_i, y_i) fornecidos. A principal vantagem 
    deste método é que o polinômio pode ser facilmente atualizado se novos pontos 
    forem adicionados.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente, os pontos de x nos quais a função f(x) é conhecida.
    y (list ou array): Lista de valores da variável dependente, os valores de f(x) para cada ponto de x.
    x_interpolado (float): O valor de x no qual a interpolação será realizada, ou seja, o ponto onde queremos estimar f(x).

    Retorna:
    float: O valor interpolado f(x_interpolado), ou seja, a avaliação do polinômio em x_interpolado.
    list: A tabela de diferenças divididas, que mostra como o polinômio de Newton é calculado passo a passo.
    list: Os coeficientes do polinômio de Newton, ou seja, os valores Δ^i f (diferenças divididas).
    """
    n = len(x)  # Número de pontos fornecidos (quantidade de elementos em x e y)
    
    # Inicializa a tabela de diferenças divididas com None. Cada célula tabela[i][j] 
    # irá armazenar a j-ésima diferença dividida dos primeiros i pontos.
    tabela_diferencas = [[None for _ in range(n)] for _ in range(n)]  

    # Preenche a primeira coluna da tabela de diferenças com os valores de y,
    # já que a primeira diferença dividida é apenas f(x_i) (os valores originais de y).
    for i in range(n):
        tabela_diferencas[i][0] = y[i]

    # Calcula as diferenças divididas. Cada célula tabela[i][j] é calculada pela fórmula:
    # Δ^j f(x_i) = (Δ^(j-1) f(x_{i+1}) - Δ^(j-1) f(x_i)) / (x_{i+j} - x_i)
    for j in range(1, n):  # Começando a calcular as diferenças divididas a partir da segunda coluna
        for i in range(n - j):  # Calcula para cada linha i até o final
            tabela_diferencas[i][j] = (tabela_diferencas[i + 1][j - 1] - tabela_diferencas[i][j - 1]) / (x[i + j] - x[i])

    # Extraindo os coeficientes do polinômio de Newton, que são as diferenças divididas da primeira linha
    coeficientes = [tabela_diferencas[0][j] for j in range(n)]  # Extraímos os coeficientes Δ^i f

    # Avaliação do polinômio de Newton em x_interpolado
    # O polinômio de Newton é avaliado como:
    # P(x) = Σ(Δ^i f(x_0) * Π(x - x_j)), para i = 0 até n-1
    termo_x = 1  # Termo que irá armazenar o produto (x - x_j) à medida que percorremos o polinômio
    resultado_interpolado = coeficientes[0]  # Começamos com o primeiro coeficiente (Δ^0 f)

    # A fórmula recursiva do polinômio de Newton para cada grau do polinômio
    for ordem in range(1, n):  # Iterando pelos termos do polinômio de grau 1 até n-1
        termo_x *= (x_interpolado - x[ordem - 1])  # Multiplica o termo (x - x_j)
        resultado_interpolado += coeficientes[ordem] * termo_x  # Adiciona o termo ao resultado

    # Retorna o valor interpolado, a tabela de diferenças divididas e os coeficientes
    return resultado_interpolado, tabela_diferencas, coeficientes

def exibir_tabela_diferencas(x, tabela_diferencas):
    """
    Exibe a tabela de diferenças divididas em formato tabular utilizando o Pandas.

    Esta tabela é útil para entender como o polinômio de Newton foi construído,
    e como as diferenças divididas são calculadas.

    Parâmetros:
    x (list ou array): Lista de valores de x (pontos conhecidos).
    tabela_diferencas (list): A tabela de diferenças divididas gerada pela interpolação de Newton.
    """
    # Cria um DataFrame (tabela) do Pandas, onde cada coluna corresponde a uma diferença dividida (Δ^i f).
    df = pd.DataFrame(tabela_diferencas, columns=[f"Δ^{i}f" for i in range(len(x))])
    
    # Adiciona uma coluna "x" na tabela para mostrar os valores de x associados a cada linha
    df.insert(0, "x", x + ["" for _ in range(len(x) - len(df))])  # Preenche com "" quando os tamanhos não coincidem

    # Exibe a tabela de diferenças divididas de forma legível
    print("\n=== Tabela de Diferenças Divididas ===")
    print(df.fillna(''))  # Preenche valores faltantes com strings vazias para melhor leitura

def exibir_polinomio(coeficientes, x):
    """
    Exibe o polinômio interpolador de Newton de forma formatada.

    Esta função gera uma string que representa o polinômio de Newton em termos de seus coeficientes 
    e as variáveis x. Essa forma é útil para ver como o polinômio é estruturado.

    Parâmetros:
    coeficientes (list): Lista de coeficientes do polinômio de Newton (Δ^i f).
    x (list): Lista de valores de x usados na interpolação.
    """
    termos = [f"{coeficientes[0]:.6f}"]  # Adiciona o primeiro coeficiente (Δ^0 f)

    # Para cada coeficiente adicional, adicionamos um termo ao polinômio
    for i in range(1, len(coeficientes)):
        termo = f"{coeficientes[i]:.6f}"  # Coeficiente atual
        for j in range(i):  # Multiplica por (x - x_j) para cada j
            termo += f"*(x - {x[j]})"
        termos.append(termo)  # Adiciona o termo completo ao polinômio

    # Exibe o polinômio completo
    print("\n=== Polinômio Interpolador ===")
    print("P(x) =", " + ".join(termos))  # Exibe o polinômio formatado

def plotar_interpolacao(x, y, x_interpolado, y_interpolado):
    """
    Plota a interpolação polinomial de Newton juntamente com os pontos fornecidos.

    Parâmetros:
    x (list ou array): Lista de valores de x (pontos conhecidos).
    y (list ou array): Lista de valores de f(x) para os pontos conhecidos.
    x_interpolado (float): Ponto onde o valor da interpolação foi calculado.
    y_interpolado (float): O valor da interpolação em x_interpolado.
    """
    # Gera valores contínuos para o intervalo de x, que são usados para desenhar o gráfico da curva
    intervalo_x = np.linspace(min(x) - 1, max(x) + 1, 100)  # Gera 100 pontos entre o mínimo e máximo de x
    intervalo_y = [interpolacao_newton(x, y, i)[0] for i in intervalo_x]  # Calcula os valores de y para cada ponto

    # Cria o gráfico
    plt.figure(figsize=(8, 6))  # Configura o tamanho do gráfico
    plt.plot(intervalo_x, intervalo_y, 'b-', label="Polinômio de Newton")  # Plota a linha do polinômio interpolador
    plt.scatter(x, y, color='red', marker='o', s=100, label="Pontos Originais")  # Plota os pontos originais (em vermelho)
    plt.scatter(x_interpolado, y_interpolado, color='green', marker='x', s=150, label=f"Interpolado em x={x_interpolado}")  # Plota o ponto interpolado (em verde)

    # Adiciona rótulos e título ao gráfico
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Interpolação Polinomial de Newton")
    plt.legend()  # Exibe a legenda
    plt.grid(True)  # Adiciona a grade ao gráfico
    plt.show()  # Exibe o gráfico gerado

# === TESTE RÁPIDO: BASTA ALTERAR ESTES VALORES ===
x_pontos = [-1, 0, 2, 3]  # Modifique os valores de x aqui para os pontos conhecidos
y_pontos = [4, 1, -1, 2]  # Modifique os valores de f(x) para cada ponto de x
x_interpolacao = 1.5  # Modifique o valor de x para o ponto em que deseja interpolar

# Flags para controlar o que será exibido
exibir_grafico = True  # Se True, o gráfico da interpolação será exibido
exibir_tabela = True   # Se True, a tabela de diferenças divididas será exibida
exibir_coeficientes = True  # Se True, os coeficientes do polinômio de Newton serão exibidos
exibir_polinomio_completo = True  # Se True, o polinômio completo será exibido

# Testando a interpolação de Newton com os valores fornecidos
y_interpolacao, tabela_diferencas, coeficientes = interpolacao_newton(x_pontos, y_pontos, x_interpolacao)

# Exibindo o resultado da interpolação
print(f"\nInterpolação realizada em x = {x_interpolacao:.6f}")
print(f"Valor interpolado: f({x_interpolacao:.6f}) = {y_interpolacao:.6f}")

# Exibir tabela de diferenças divididas, coeficientes e o polinômio, se solicitado
if exibir_tabela:
    exibir_tabela_diferencas(x_pontos, tabela_diferencas)

if exibir_coeficientes:
    print("\n=== Coeficientes do Polinômio ===")
    for i, coef in enumerate(coeficientes):
        print(f"Coeficiente Δ^{i}f: {coef:.6f}")

if exibir_polinomio_completo:
    exibir_polinomio(coeficientes, x_pontos)

# Gerar o gráfico da interpolação, se solicitado
if exibir_grafico:
    plotar_interpolacao(x_pontos, y_pontos, x_interpolacao, y_interpolacao)
O que este código faz:
Interpolação de Newton: Cria um polinômio de grau 
𝑛
−
1
n−1 (onde 
𝑛
n é o número de pontos dados) que passa por todos os pontos fornecidos. O polinômio de Newton é gerado através das diferenças divididas, uma técnica iterativa que facilita o cálculo e a atualização do polinômio quando novos pontos são adicionados.
Funções:
interpolacao_newton: Calcula o valor interpolado no ponto desejado, calcula as diferenças divididas e os coeficientes do polinômio.
exibir_tabela_diferencas: Exibe a tabela de diferenças divididas para entender como o polinômio foi calculado.
exibir_polinomio: Exibe o polinômio interpolador completo de forma legível.
plotar_interpolacao: Gera um gráfico que mostra os pontos fornecidos, a curva interpoladora e o ponto interpolado.
Modificações:
Alterar os pontos de 
𝑥
x e 
𝑦
y: Modifique as listas x_pontos e y_pontos para os dados de entrada do seu problema.
Alterar o ponto de interpolação: Modifique a variável x_interpolacao para o ponto onde deseja estimar o valor da função.
Exibir gráficos/tabelas/polinômios: As variáveis exibir_grafico, exibir_tabela, exibir_coeficientes e exibir_polinomio_completo controlam o que será exibido ao usuário.
