import numpy as np
import matplotlib.pyplot as plt
from resolver_sistema import resolver_sistema_LU

class MinimosQuadrados:
    def __init__(self, x, y, funcoes_base):
        """
        Inicializa o modelo de mínimos quadrados.

        Parâmetros:
        x : np.array
            Vetor de valores da variável independente.
        y : np.array
            Vetor de valores da variável dependente.
        funcoes_base : list
            Lista de funções base para ajuste.
        """
        self.x = x
        self.y = y
        self.funcoes_base = funcoes_base
        self.coeficientes = self.ajustar()

    def ajustar(self):
        """Realiza o ajuste pelo método dos mínimos quadrados."""
        n = len(self.x)
        m = len(self.funcoes_base)

        A = np.zeros((m, m))
        b = np.zeros(m)

        for i in range(m):
            for j in range(m):
                A[i, j] = sum(self.funcoes_base[i](x_k) * self.funcoes_base[j](x_k) for x_k in self.x)
            b[i] = sum(y_k * self.funcoes_base[i](x_k) for x_k, y_k in zip(self.x, self.y))

        coeficientes = resolver_sistema_LU(A, b)
        return coeficientes

    def predicao(self, x_val):
        """
        Faz a previsão para um dado x utilizando os coeficientes ajustados.

        Parâmetros:
        x_val : float ou np.array
            Valor ou vetor de valores de entrada.

        Retorno:
        float ou np.array
            Valor estimado de y correspondente a x_val.
        """
        return sum(c * f(x_val) for c, f in zip(self.coeficientes, self.funcoes_base))

    def plotar(self):
        """Plota os pontos experimentais e a curva ajustada."""
        x_fit = np.linspace(min(self.x), max(self.x), 100)
        y_fit = self.predicao(x_fit)

        plt.scatter(self.x, self.y, color='red', label='Pontos experimentais')
        plt.plot(x_fit, y_fit, color='blue', label='Curva ajustada')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Ajuste por Mínimos Quadrados')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Exemplo de uso
    x = np.array([-1, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1])
    y = np.array([2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05])
    funcoes_base = [lambda x: np.sin(x), lambda x: np.cos(x), lambda x: 1]

    modelo = MinimosQuadrados(x, y, funcoes_base)
    modelo.plotar()

    # Exemplo de predição
    novo_x = 0.3
    pred_y = modelo.predicao(novo_x)
    print(novo_x)
