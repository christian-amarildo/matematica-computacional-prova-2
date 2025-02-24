import numpy as np  # Importando o pacote numpy, utilizado para manipulação de arrays e operações matemáticas
import matplotlib.pyplot as plt  # Importando a biblioteca para plotar gráficos
from resolver_sistema import resolver_sistema_LU  # Importando uma função externa para resolver sistemas lineares

# Definindo a classe MinimosQuadrados
class MinimosQuadrados:
    def __init__(self, x, y, funcoes_base):
        """
        Inicializa o modelo de mínimos quadrados.

        Parâmetros:
        x : np.array
            Vetor de valores da variável independente (os valores para os quais queremos estimar y).
        y : np.array
            Vetor de valores da variável dependente (valores observados para y, que queremos ajustar).
        funcoes_base : list
            Lista de funções base para ajuste. Essas funções representam os termos que serão usados para aproximar o modelo.
            Cada função base será uma função do tipo lambda, que recebe um valor de x e retorna um valor relacionado.

        A classe irá ajustar um modelo polinomial (ou outro tipo de modelo) que melhor se encaixa aos dados dados por x e y
        usando o método dos Mínimos Quadrados. O modelo será construído a partir das funções base fornecidas.
        """
        self.x = x  # Armazena os valores da variável independente (x)
        self.y = y  # Armazena os valores da variável dependente (y)
        self.funcoes_base = funcoes_base  # Armazena as funções base para o ajuste
        self.coeficientes = self.ajustar()  # Chama a função de ajuste para calcular os coeficientes

    def ajustar(self):
        """
        Realiza o ajuste pelo método dos mínimos quadrados.
        
        O método dos mínimos quadrados resolve um sistema linear para encontrar os coeficientes
        que minimizam a soma dos quadrados dos erros entre a predição do modelo e os dados reais.

        Retorna:
        coeficientes : np.array
            Os coeficientes ajustados que melhor se adaptam aos dados fornecidos.
        """
        n = len(self.x)  # Número de pontos de dados (tamanho do vetor x)
        m = len(self.funcoes_base)  # Número de funções base fornecidas

        # Matriz A que armazena os produtos das funções base para cada par (i,j)
        A = np.zeros((m, m))  # Inicializa uma matriz quadrada de tamanho m x m com zeros
        b = np.zeros(m)  # Inicializa um vetor coluna b de tamanho m com zeros

        # Preenchendo a matriz A e o vetor b, de acordo com a formulação do método dos mínimos quadrados
        for i in range(m):  # Para cada função base i
            for j in range(m):  # Para cada função base j
                # Calcula o somatório da multiplicação das funções base i e j nos dados x
                A[i, j] = sum(self.funcoes_base[i](x_k) * self.funcoes_base[j](x_k) for x_k in self.x)
            # Preenche o vetor b com o somatório do produto entre y_k e a função base i para cada valor de x_k
            b[i] = sum(y_k * self.funcoes_base[i](x_k) for x_k, y_k in zip(self.x, self.y))

        # Chama a função resolver_sistema_LU (que provavelmente resolve um sistema linear usando decomposição LU)
        coeficientes = resolver_sistema_LU(A, b)
        return coeficientes  # Retorna os coeficientes ajustados

    def predicao(self, x_val):
        """
        Faz a previsão para um dado valor de x utilizando os coeficientes ajustados.

        Parâmetros:
        x_val : float ou np.array
            Valor ou vetor de valores de entrada, para os quais queremos prever os valores de y.

        Retorno:
        float ou np.array
            Valor estimado de y correspondente a x_val.
        """
        # A predição é dada pela soma ponderada das funções base avaliadas em x_val,
        # multiplicada pelos coeficientes ajustados
        return sum(c * f(x_val) for c, f in zip(self.coeficientes, self.funcoes_base))

    def plotar(self):
        """
        Plota os pontos experimentais e a curva ajustada pelo modelo de mínimos quadrados.
        """
        # Gera um vetor de valores de x (x_fit) para plotar a curva ajustada
        x_fit = np.linspace(min(self.x), max(self.x), 100)  # Gera 100 pontos igualmente distribuídos no intervalo de x
        # Calcula os valores de y correspondentes aos valores de x_fit usando a predição
        y_fit = self.predicao(x_fit)

        # Plota os pontos experimentais em vermelho
        plt.scatter(self.x, self.y, color='red', label='Pontos experimentais')
        # Plota a curva ajustada em azul
        plt.plot(x_fit, y_fit, color='blue', label='Curva ajustada')
        
        # Define rótulos e título do gráfico
        plt.xlabel('X')  # Rótulo para o eixo X
        plt.ylabel('Y')  # Rótulo para o eixo Y
        plt.title('Ajuste por Mínimos Quadrados')  # Título do gráfico
        plt.legend()  # Adiciona uma legenda ao gráfico
        plt.grid()  # Adiciona uma grade ao gráfico
        plt.show()  # Exibe o gráfico gerado

# Bloco principal para testar a classe e o método de ajuste
if __name__ == "__main__":
    # Exemplo de uso do código:
    
    # Definindo os dados experimentais (x e y)
    x = np.array([-1, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1])  # Valores de x (variável independente)
    y = np.array([2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05])  # Valores de y (variável dependente)
    
    # Definindo as funções base para o ajuste (aqui estamos usando seno, cosseno e um termo constante)
    funcoes_base = [
        lambda x: np.sin(x),  # Função base 1: seno de x
        lambda x: np.cos(x),  # Função base 2: cosseno de x
        lambda x: 1           # Função base 3: termo constante (1)
    ]

    # Criação do modelo de mínimos quadrados, passando os dados e as funções base
    modelo = MinimosQuadrados(x, y, funcoes_base)
    
    # Plotando os pontos experimentais e a curva ajustada
    modelo.plotar()

    # Exemplo de predição: prever o valor de y para um novo valor de x (por exemplo, x = 0.3)
    novo_x = 0.3  # Novo valor de x para o qual queremos fazer a predição
    pred_y = modelo.predicao(novo_x)  # Prediz o valor de y correspondente a novo_x
    print(f'Para x = {novo_x}, a predição de y é {pred_y}')  # Exibe o valor de y estimado





    
# Comentários detalhados sobre o código:
# Importações e dependências:

# numpy é usado para manipulação de arrays e operações numéricas.
# matplotlib.pyplot é utilizado para plotar gráficos.
# resolver_sistema_LU é uma função externa que resolve sistemas lineares utilizando o método de decomposição LU.
# Classe MinimosQuadrados:

# Construtor __init__: Recebe os dados x, y e as funções base para o ajuste, e chama o método ajustar para calcular os coeficientes que melhor ajustam os dados.
# Método ajustar: Constrói a matriz 
# 𝐴
# A e o vetor 
# 𝑏
# b necessários para resolver o sistema linear, onde as soluções são os coeficientes que minimizam o erro quadrático.
# Método predicao: Recebe um valor de x_val e calcula o valor correspondente de y, utilizando os coeficientes ajustados e as funções base.
# Método plotar: Plota os pontos experimentais e a curva ajustada.
# Como modificar o código:

# Alterar funções base: Você pode alterar as funções que estão sendo usadas no ajuste (seno, cosseno e constante). Por exemplo, se quiser ajustar um polinômio de segundo grau, pode adicionar funções como lambda x: x**2 ou outras funções conforme necessário.
# Alterar os dados de entrada: Basta modificar os vetores x e y para outros valores experimentais ou funções.
# Alterar a técnica de resolução do sistema: Se preferir outro método de solução para o sistema linear, basta alterar a chamada à função resolver_sistema_LU.
# Esse código aplica o método de mínimos quadrados para ajustar uma curva aos dados fornecidos. A principal vantagem dessa abordagem é que ela encontra o melhor modelo linear (ou em termos das funções base fornecidas) que minimiza a soma dos quadrados dos erros.
