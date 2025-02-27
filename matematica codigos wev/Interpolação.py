import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt


def sistemaVandermonde(x,y):
  """Função que resolve um sistema Vandermonde pra obter a função polinomial interpoladora.
  Parâmetros de Entrada:\n
  x = valores de x tabelados em f(x)\n
  y = valores de f(x)\n (x,y) formam os pontos pra gerar a função interpoladora.\n
  Retorno:\n
  Mostra a matriz de Vandermonde.\n
  Mostra o polinômio Interpolador.\n
  Retorna array com os coeficientes da função interpoladora, que é a resolução do sistema linear.\n"""

  #inicializa as variáveis pra guardar os resultados,todas vazias
  n = len(x)
  A = np.empty((n,n))
  b = np.empty((n))

  # popula a matriz de vandermonde
  for i in range(0,n):
    A[i,0] = 1
    for j in range(1,n):
      A[i,j] = A[i,j-1]*x[i] #valor da comula anterior * o x referente a linha
    b[i] = y[i]
  
  print("Matriz de Vandermonde:\n")
  print(A)

  x = np.linalg.solve(A,b)


  print("Polinômio interporlador obtido:")
  p = np.poly1d(np.flip(x))
  print(p)
  return x
"""
Ex :

# Exemplo

# x e y tabelados
x  = [-1, 0, 2]
fx = [4, 1, -1]
#Resolução

print(sistemaVandermonde(x,fx))
"""


def interpLagrange(xp, x, y, grau=None):
    """Função que calcula o valor y da função interpoladora de Lagrange.
    
    Parâmetros:
    xp = Ponto onde deseja interpolar.
    x = Lista com os valores de x tabelados.
    y = Lista com os valores de y tabelados.
    grau = Grau do polinômio interpolador (opcional).
    
    Retorno:
    yp = Valor de y correspondente a xp pela interpolação.
    """
    n = grau if grau is not None else len(x) - 1  # Define o grau do polinômio caso não seja definido
    
    yp = 0  # Inicializa yp como zero
    
    for k in range(n + 1):  # Loop pelos pontos da tabela
        Lk = 1  # Inicializa o polinômio base de Lagrange
        
        for j in range(n + 1):  # Construção de Lk(x)
            if k != j:
                Lk *= (xp - x[j]) / (x[k] - x[j])
        
        yp += Lk * y[k]  # Soma ponderada dos valores de y
    
    return yp



def interpLagrangeGrafico(x,y,grau=None):
  """Função que encontra o polinômio Interpolador pela forma de Lagrange.\n
  Parâmetros:\n
  x = vetor com valores x pra formação do polinômio Interpolador\n
  y = vetor com os valores de y pra formação da cunção interpoladora\n
  Intervalo = intervalo que será gerada a função Interpoladora. Por padrão recebe o valor de -1 até 2

  A função gera o gráfico da função interpoladora e retorna os valores da função interpoladora nesse intervalo passado por parâmetro
  """
  Intervalo=np.arange(min(x),max(x)+0.0001,0.01)

  n=grau if grau != None else len(x)-1

  yt = []
  # Valor inicial de g(xp).
  
  for i in Intervalo:
    yp = 0
    # Interpolação de Lagrange
    for k in range(0,n+1):  
      p = 1
      for j in range(0,n+1):
        if k != j:
          p = p*(i - x[j])/(x[k] - x[j])
      
      yp = yp + p * y[k]  
    yt.append(yp)
    
  plt.title(f'Polinomio Interpolador pela Forma de Lagrange')
  plt.plot(Intervalo,yt,'b-')
  plt.plot(x,y,'ro')
  plt.grid()
  plt.show()

  return yt

################# método de newton ###################


def TabelaDD(x, y):
  """Função que recebe pontos tabelados e imprime a tabela de diferençsa divididas"""
  
  n = len(x)
  fdd = [[None for x in range(n)] for x in range(n)]

  for i in range(n):
    fdd[i][0] = y[i] 

  for j in range(1,n):
    for i in range(n-j):
      fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])
  
  
  print(" < Tabela de diferenças divididas >\n Colunas : Ordem\nLinhas: índice do x")
  fdd_table = pd.DataFrame(fdd)
  print(fdd_table)
 
 
def interpNewton(x, y, xi):
  """Função calcula a interpolação pela forma de newton.\n
  Parâmetros:\n
  x = ponto x tabelado.\n
  y = ponto y tabelado\n
  xi= Ponto da Interpolação.\n
  Retorno:\n
  yp = valor interpolado de xi."""

  #Número de dados
  n = len(x)
  #Inicialização da diferença dividida: n x n
  fdd = [[None for x in range(n)] for x in range(n)]
  #Valores da função f(X) em vários pontos
  yint = [None for x in range(n)]
    
  #Encontrando diferenças divididas.
  for i in range(n):
    fdd[i][0] = y[i]
  for j in range(1,n):
    for i in range(n-j):
      fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i]) #formula do polinomio interpolador
    
    
  #Interpolação para xi.
  xterm = 1
  yint = fdd[0][0]
  for order in range(1, n):
    xterm = xterm * (xi - x[order-1])
    yint = yint + fdd[0][order]*xterm
    
  #Retornando g(xi).
  return yint

def interpNewtonGrafico(x,y,ShowGraph=True, MostrartabelaDD=False):
  """Função que Encontra o polinômio interpolador pela forma de newton.\n
  Parâmetros:\n
  x = vetor com valores x pra formação do polinômio Interpolador\n
  y = vetor com os valores de y pra formação da cunção interpoladora\n
  ShowGraph - Valor booleano pra gerar o gráfico da função interpoladora\n

  A função gera o gráfico da função interpoladora e retorna os valores da função interpoladora nesse intervalo passado por parâmetro.
  """
  Intervalo=np.arange(min(x),max(x)+0.0001,0.01)
  n = len(x)
  fdd = [[None for x in range(n)] for x in range(n)]

  for i in range(n):
    fdd[i][0] = y[i] 

  for j in range(1,n):
    for i in range(n-j):
      fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])
  
  if MostrartabelaDD:
    print(" < Tabela de diferenças divididas >\n Colunas : Ordem\nLinhas: índice do x")
    fdd_table = pd.DataFrame(fdd)
    print(fdd_table)
  
  yt = []

  for xi in Intervalo:
    xterm = 1
    yint  = fdd[0][0]
    for order in range(1,n):
      xterm = xterm*(xi - x[order-1])
      yint  = yint + fdd[0][order]*xterm
    yt.append(yint)
    
  if ShowGraph:
    plt.title(f'Polinomio Interpolador pela Forma de Newton')
    plt.plot(Intervalo,yt,'b-')
    plt.plot(x,y,'ro')
    plt.grid()
    plt.show()

  return yt

def Results(f,pontosx,pontosy):
    """Função que plota os valores de f em pontos tabelados juntamente com a função interpoladora calculada pelo método de newton.\n"""
    x=np.arange(min(pontosx),max(pontosx)+0.0001,0.01)
    y= f(x)
    yt = []
    for i in x:
        yt.append(interpNewton(pontosx, pontosy, i))

    plt.plot(x,yt,marker = '', label= 'Função Interpoladora',color = 'green')
    plt.plot(pontosx,pontosy,'ro')
    plt.plot(x, y,'b--', label= 'Função f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Results()\nGráfico da função f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def Results_spline(f,pontosx,pontosy,spline=True):
    """ Função que plota os valores de f em pontos tabelados juntamente com a função interpoladora calculada pelo método de newton com parâmetro spline.\n"""
    x=np.arange(min(pontosx),max(pontosx)+0.0001,0.01)
    y= f(x)
    t  = x
    yt = []
    yt2 =[]

    for i in t:
        yt.append(interpNewton(pontosx, pontosy, i))
    if spline:
        # f2 = interp1d(pontosx,pontosy,kind='linear',fill_value="extrapolate")
        # f3 = interp1d(pontosx,pontosy, kind='cubic',fill_value="extrapolate")
        f4 = interp1d(pontosx,pontosy,kind='quadratic',fill_value="extrapolate")


        # plt.plot(t,f2(t),'y-',label = 'spline linear')
        # plt.plot(t,f3(t),'m-',label = 'spline cúbica')
        plt.plot(t,f4(t),'r-',label = 'spline quadrática')

    plt.plot(t,yt,marker = '', label= 'Função Interpoladora',color = 'green')
    plt.plot(pontosx,pontosy,'ro')
    plt.plot(x, y,'b-.', label= 'Função f(x)')


    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico da função f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def gerar_pontos_aleatorios(n):
    pontos = []
    for _ in range(n):
        ponto = random.uniform(-1, 1)
        pontos.append(ponto)
    return pontos 
  


#################################################################################
# x = [1,1.01,1.02,1.03,1.04,1.05] # valores de x
# y = [1,1.005,1.01,1.0149,1.0198,1.0247] # valores f(x)
# sistemaVandermonde(x,y) ## exibe a matriz de vondermonde e calcula o polinomio interpolador

#################################################################################

# #metodo larange entradas:
# x = [1,1.01,1.02,1.03,1.04,1.05] # valores de x
# y = [1,1.005,1.01,1.0149,1.0198,1.0247] # valores f(x)
# xp = 0.75 # posição x da interpolação
# p = interpLagrange(xp,x,y,grau=None) # função que calcula o y no ponto x da interpolação
# interpLagrangeGrafico(x,y,grau=None) #função que plota o grafico do polinomio interpolador de larange 

# print("Resultado pelo metodo de larange")
# print(f"O valor interpolado de y para x = {xp} é : {p:.2f} ")

#################################################################################
#metodo newton entradas:

x = [1,1.01,1.02,1.03,1.04,1.05] # valores de x
y = [1,1.005,1.01,1.0149,1.0198,1.0247] # valores f(x)
# intervalo = np.arange(0.6,0.7,0.01)
xi = 1.025 # posição x da interpolação
TabelaDD(x, y) # função que exibe a tabela 
p = interpNewton(x, y, xi) # função que calcula o y no ponto x da interpolação

# interpNewtonGrafico(x,y) # função que plota o grafico de interpolação

# Results(f_cubica,x,y) ## esperando uma função f ser passada como argumento para plotar a função 
# Results_spline(f,x,y) ## esperando uma função f ser passada como argumento para plotar a função 

print("Resultado pelo metodo de newton")
print(f"O valor interpolado de y para x = {xi} é : {p:.2f} ")



