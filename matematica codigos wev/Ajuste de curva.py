import numpy as np
import math
import matplotlib.pyplot as plt

class MQ:
    def __init__(self):
        self.alfas = []
    
    @staticmethod
    def gauss_jacobi(A, B, x0=None, tol=1e-10, max_iter=1000):
        n = len(B)
        x = np.zeros(n) if x0 is None else x0
        for _ in range(max_iter):
            x_new = np.copy(x)
            for i in range(n):
                s = sum(A[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (B[i] - s) / A[i][i]
            if np.linalg.norm(x_new - x, ord=np.inf) < tol:
                return x_new
            x = x_new
        return x
        
    @staticmethod
    def gauss_seidel(A, B, x0=None, tol=1e-10, max_iter=1000):
        n = len(B)
        x = np.zeros(n) if x0 is None else x0
        for _ in range(max_iter):
            x_new = np.copy(x)
            for i in range(n):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (B[i] - s1 - s2) / A[i][i]
            if np.linalg.norm(x_new - x, ord=np.inf) < tol:
                return x_new
            x = x_new
        return x
        
    @staticmethod
    def gauss_elimination_pivot(A, B):
        n = len(B)
        A = A.astype(float)
        B = B.astype(float)
        for i in range(n):
            max_row = np.argmax(abs(A[i:, i])) + i
            A[[i, max_row]] = A[[max_row, i]]
            B[[i, max_row]] = B[[max_row, i]]
            for j in range(i + 1, n):
                factor = A[j, i] / A[i, i]
                A[j, i:] -= factor * A[i, i:]
                B[j] -= factor * B[i]
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (B[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        return x
    
    def solve_system(self, A, B, method='gauss_jacobi'):
        if method == 'gauss_jacobi':
            return self.gauss_jacobi(A, B)
        elif method == 'gauss_seidel':
            return self.gauss_seidel(A, B)
        elif method == 'gauss_elimination':
            return self.gauss_elimination_pivot(A, B)
        else:
            raise ValueError("Método inválido. Escolha entre 'gauss_jacobi', 'gauss_seidel' ou 'gauss_elimination'.")
    
    def fit(self, x, y, G, method='gauss_jacobi', printValues=True):
        """Método que calcula os valores do vetor de alfas.\n
        Parâmetros:\n
        x= vetor de valores de xi tabelados\n
        y= vetor de valores de yi tabelados\n
        G= Vetor com as n funções g1(x),...gn(x), ex: [lambda x:1, lambda x:x,lambda x:x**2].\n\n 
        Retorno:\n
        calcula os valores de alfas
        printa os valores dos alfas calculados."""
        self.G = G
        A = []
        B = []
        
        """ montagem da matriz """
        for g_lin in G:
            b = sum(g_lin(x[i]) * y[i] for i in range(len(x)))
            B.append(b)
            A.append([sum(g_lin(x[i]) * g_col(x[i]) for i in range(len(x))) for g_col in G])
        
        A = np.array(A) #conversão explicita para um np array
        B = np.array(B)
        
        # Escolha do método para resolver o sistema linear
        self.alfas = self.solve_system(A, B, method)
        
        if printValues:
            print("Valores do sistema linear Criado:")
            print('A: ', A)
            print('B: ', B)
            print(f"Matriz:\n {np.column_stack((A, B))}")
            print(f"Alfas: {self.alfas}")
    
    def fit_exp(self, x, y, GExp=[lambda x: 1, lambda x: x], method='gauss_jacobi', printValues=True):
        self.Gexp = GExp
        z = np.log(y)  # calcula o vetor z ln(y)
        self.fit(x, z, self.Gexp, method)  # calcula os valores de alfa com vetor z g1=1 e g2=x
        
        self.alfas[0] = np.exp(self.alfas[0])  # calcula o a1
        self.alfas[1] = -self.alfas[1]  # calcula o a2

        if printValues:
            print("Valores do sistema linear Criado:")
            print(f"Alfas: {self.alfas}")

    def fit_seno(self, x, y, G=[lambda x: 1, lambda x: x], method='gauss_jacobi', printValues=False):
        z = [np.arcsin(yi) for yi in y]   # calcula o vetor z ln(y)
         # linearização
        self.fit(x, z, G, method, printValues)  # calcula os valores de alfa com vetor z g1=1 e g2=x

    def fit_geom(self, x, y, GGeom=[lambda x: 1, lambda x: x], method='gauss_jacobi', printValues=False):
        """O método realiza a linearização da curva geométrica, calculando o logaritmo natural dos valores y e,
        em seguida, chama o método fit para calcular os valores dos coeficientes alfa utilizando as funções g definidas em GGeom."""
        z = np.log(y) # calcula o vetor z ln(y)
        # linearização
        self.fit(x, z, GGeom, method)   # calcula os valores de alfa com vetor z g1=1 e g2=x
        self.alfas[0] = math.e ** self.alfas[0]   # calcula o a1
        self.alfas[1] = -self.alfas[1]   # calcula o a2

        if printValues:
            print("Valores do sistema linear criado:")
            print(f"Alfas: {self.alfas}")

    def calc(self, x):
        """Calcula o somatório do valor de x aplicado em cada função no vetor de funções g."""
        return sum(self.alfas[i] * self.G[i](x) for i in range(len(self.G)))

    def calc_hip(self, x):
        s = sum(self.alfas[i] * self.G[i](x) for i in range(len(self.G)))
        return 1 / s

    def calc_exp(self, x):
        """Retorna o valor da função phi no ponto x para casos não lineares."""
        return self.alfas[0] * (math.e ** (-self.alfas[1] * x))

    def calc_geom(self, x):
        """Calcula o valor da função geométrica no ponto x."""
        return sum(self.alfas[i] * self.Ggeom[i](x) for i in range(len(self.Ggeom)))

    def calc_seno(self, x):
        """Calcula o valor da função seno no ponto x."""
        return np.sin(sum(self.alfas[i] * self.G[i](x) for i in range(len(self.G))))

    def plotPontos(self, x, y):
        """Método que plota o gráfico dos pontos tabelados"""
        plt.plot(x, y, 'ro')
        plt.title('Gráfico dos pontos tabelados')
        plt.grid()
        plt.show()

    def PrintAjusteCurva(self, x, y, Linear=True, exp=False, hip=False, geom=False, seno=False, method='gauss_jacobi'):
        """Método que mostra o gráfico do ajuste de curva. Os alfas já devem ter sido calculados com o método fit."""
        x_line = np.linspace(min(x) - 0.0001, max(x) + 0.0001, 100)

        if Linear: 
            self.fit(x, y, self.G, method)
            y_line = list(map(self.calc, x_line))
            plt.plot(x_line, y_line, 'g-', label='Função linear')
        
        if exp:
            self.fit_exp(x, y, self.Gexp, method)
            y_nlinear = list(map(self.calc_exp, x_line))
            plt.plot(x_line, y_nlinear, 'b-', label='Função Não linear - exp')
        
        if hip:
            y_nlinear = list(map(self.calc_hip, x_line))
            plt.plot(x_line, y_nlinear, 'b-', label='Função Não linear - hip')
        
        if geom:
            y_nlinear = list(map(self.calc_geom, x_line))
            plt.plot(x_line, y_nlinear, 'b-', label='Função Não linear - geo')
        
        if seno:
            y_nlinear = list(map(self.calc_seno, x_line))
            plt.plot(x_line, y_nlinear, 'b-', label='Função Não linear - seno')

        plt.plot(x, y, 'ro')  
        plt.legend()
        plt.grid()
        plt.show()

def MinimoQuadrado(xi, yi):
    """Função que Calcula os valores do vetor de alfas com o mínimo Quadrado.\n
    Parâmetros:\n
    xi= vetor de valores de xi tabelados\n
    yi= vetor de valores de yi tabelados\n\n
    
    Retorno:\n
    Vetor a com os valores calculados 'alfas' por meio da resolução do sistema linear."""
    
    V = np.array([xi**2, xi**1, xi**0]).transpose()
    a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi)
    return a


####################################################################
#exemplo de uso minimo quadradao:     
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2.7, 7.4, 20.1, 54.6, 148.4])
   
# vetR = MinimoQuadrado(x, y)
# print(vetR)

##########################################################################

#Uso do MQ

def exemplo_ajuste_curva():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 7, 11])
    
    mq = MQ()
    mq.fit(x, y, [lambda x: 1, lambda x: x], method='gauss_elimination')    #escolher entre 'gauss_jacobi', 'gauss_seidel' ou 'gauss_elimination'
    mq.PrintAjusteCurva(x, y)
    

exemplo_ajuste_curva()
