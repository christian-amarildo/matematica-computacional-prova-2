import numpy as np  # Importando o pacote numpy, utilizado para manipulação de arrays e operações matemáticas
from met_min_quad_linear import MinimosQuadrados  # Importando a classe MinimosQuadrados de um arquivo externo
import matplotlib.pyplot as plt  # Importando a biblioteca matplotlib para plotagem de gráficos

# Dados extraídos de uma tabela, representando pares (x, y) que correspondem a alguma variável.
# Esses são os dados experimentais para os quais queremos ajustar uma função.
x = np.array([-1.0, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1.0])  # Valores da variável independente (x)
y = np.array([36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246])  # Valores da variável dependente (y)

# --------------------------------------------------------
# Etapa de Linearização:
# O modelo original é da forma y = a1 * exp(-a2 * x), que é uma exponencial decrescente.
# Para facilitar o ajuste, aplicamos o logaritmo natural nos valores de y para linearizar o modelo.
# A transformação será: ln(y) = ln(a1) - a2 * x
# --------------------------------------------------------

y_transformed = np.log(y)  # Aplica o logaritmo natural nos valores de y para linearizar a equação

# Definindo as funções base para o ajuste linear. As funções base serão usadas no método dos mínimos quadrados.
# Para o modelo linear ln(y) = ln(a1) - a2 * x, as funções base são:
# 1. A função constante 1, que corresponde ao termo ln(a1).
# 2. A função x, que corresponde ao termo -a2 * x.
funcoes_base = [lambda x: 1, lambda x: x]

# Criando o modelo de mínimos quadrados utilizando os dados x e os valores transformados de y (y_transformed)
# A função MinimosQuadrados recebe os dados x, y_transformados e as funções base.
# Ela calcula os coeficientes que melhor ajustam os dados aos termos fornecidos pelas funções base.
# O retorno será um objeto que contém os coeficientes ajustados.
coef = MinimosQuadrados(x, y_transformed, funcoes_base).coeficientes

# Após o ajuste linear, os coeficientes encontrados correspondem a:
# coef[0] é o ln(a1), e coef[1] é o -a2.
# Para retornar aos valores originais do modelo não linear, devemos inverter a transformação.
a1 = np.exp(coef[0])  # Para obter a1, aplicamos a exponencial no coeficiente ln(a1)
a2 = -coef[1]  # O coeficiente a2 já foi negado, então apenas o usamos diretamente

# Definindo a função ajustada para o modelo original y = a1 * exp(-a2 * x)
# Agora, a função ajustada pode ser utilizada para prever os valores de y para qualquer x.
funcao_ajustada = lambda x: a1 * np.exp(-a2 * x)

# --------------------------------------------------------
# Função para plotar os dados experimentais e a curva ajustada:
# Esta função irá gerar um gráfico mostrando os pontos reais (em vermelho) e a curva ajustada (em azul).
# --------------------------------------------------------

def plotar(x, y):
    """
    Plota os pontos experimentais e a curva ajustada.
    """
    # Gerando um conjunto de pontos x para a curva ajustada
    # Usamos np.linspace para gerar 1000 pontos igualmente distribuídos entre o mínimo e o máximo de x
    x_fit = np.linspace(min(x), max(x), 1000)
    
    # Calculando os valores de y correspondentes aos pontos x_fit usando a função ajustada
    y_fit = funcao_ajustada(x_fit)
    
    # Plotando os pontos experimentais como um gráfico de dispersão (scatter plot)
    plt.scatter(x, y, color='red', label='Pontos experimentais')  # 'red' define a cor dos pontos experimentais
    
    # Plotando a curva ajustada. Aqui, usamos x_fit e y_fit, que são os valores ajustados pela função.
    plt.plot(x_fit, y_fit, color='blue', label='Curva ajustada')  # 'blue' define a cor da curva ajustada
    
    # Definindo o título e rótulos dos eixos do gráfico
    plt.xlabel('X')  # Rótulo para o eixo X
    plt.ylabel('Y')  # Rótulo para o eixo Y
    plt.title('Ajuste por Mínimos Quadrados')  # Título do gráfico
    
    # Adicionando uma legenda para indicar as diferentes partes do gráfico (pontos experimentais e curva ajustada)
    plt.legend()
    
    # Adicionando uma grade ao gráfico para facilitar a visualização
    plt.grid()
    
    # Exibindo o gráfico gerado
    plt.show()

# Chamando a função de plotagem para mostrar o gráfico
# Passamos x e y originais para mostrar os pontos reais e a curva ajustada.
plotar(x, y)

# Explicações detalhadas do código:
# Leitura dos Dados:

# x e y são os dados experimentais que estamos ajustando. x representa a variável independente (por exemplo, o tempo, a distância, etc.), enquanto y representa a variável dependente (o que queremos prever ou modelar).
# Linearização:

# A equação original do modelo é y = a1 * exp(-a2 * x), uma função exponencial decrescente.
# Para facilitar a aplicação do método dos mínimos quadrados, transformamos a equação para a forma linear: ln(y) = ln(a1) - a2 * x.
# O logaritmo natural (np.log(y)) é aplicado nos valores de y para obter a versão transformada, y_transformed.
# Funções Base:

# As funções base são aquelas que representaram a forma linearizada do modelo. Aqui, escolhemos 1 (função constante) e x (função linear), pois estamos ajustando um modelo do tipo ln(y) = ln(a1) - a2 * x.
# A função lambda x: 1 cria um vetor de 1s, necessário para modelar o termo ln(a1), e lambda x: x modela o termo -a2 * x.
# Ajuste dos Coeficientes:

# O método dos mínimos quadrados é utilizado para ajustar os coeficientes ln(a1) e -a2.
# A classe MinimosQuadrados recebe os dados x, y_transformed e as funções base, e calcula os coeficientes ajustados.
# Após o ajuste, os coeficientes coef[0] e coef[1] são usados para calcular a1 e a2 na equação original, usando np.exp() para reverter o logaritmo e negando coef[1].
# Função Ajustada:

# Agora, temos a função ajustada no formato original: y = a1 * exp(-a2 * x). Essa função pode ser usada para prever os valores de y para qualquer entrada x.
# Plotagem:

# A função plotar é responsável por exibir o gráfico.
# Ela gera uma linha de x_fit (um intervalo de valores x de 1000 pontos igualmente distribuídos) e calcula os valores correspondentes de y_fit usando a função ajustada.
# Em seguida, plota os pontos experimentais em vermelho e a curva ajustada em azul.
# A legenda, título, rótulos dos eixos e grade são adicionados para tornar o gráfico mais legível.
# Como Modificar o Código:
# Alterar os dados de entrada: Se você tiver outros dados, basta substituir os valores dos arrays x e y pelos seus próprios dados experimentais.
# Alterar a função de modelo: Se o seu modelo for diferente de uma função exponencial (por exemplo, um polinômio), você precisará ajustar a transformação e as funções base. Para um modelo polinomial, as funções base poderiam ser algo como lambda x: x**2, lambda x: x**3, etc.
# Alterar o número de pontos de ajuste: Você pode aumentar ou diminuir o número de pontos para o gráfico ajustado alterando o número 1000 no np.linspace.
# Esse código serve como um excelente exemplo de como usar o método dos Mínimos Quadrados para ajustar dados experimentais a um modelo não linear transformado para um modelo linear.







