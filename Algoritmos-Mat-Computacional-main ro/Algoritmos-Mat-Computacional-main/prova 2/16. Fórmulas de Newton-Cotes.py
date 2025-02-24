import numpy as np

# Achar os coeficientes
def FormaDeNewton(x_tab, y_tab):
    """
    Calcula o polinômio interpolador usando a forma de Newton
    
    Parâmetros:
    x_tab -- array numpy com os pontos x de interpolação
    y_tab -- array numpy com os valores correspondentes y
    
    Retorna:
    coeficientes -- array com os coeficientes do polinômio de Newton
    """
    n = len(x_tab)
    coeficientes = np.zeros(n)
    diferenças = y_tab.copy()  # Inicializa com os valores y
    
    # Calcula as diferenças divididas iterativamente
    for ordem in range(1, n):
        for i in range(n - ordem):
            # Calcula a diferença dividida de ordem atual
            diferenças[i] = (diferenças[i + 1] - diferenças[i]) / (x_tab[i + ordem] - x_tab[i])
        coeficientes[ordem] = diferenças[0]
    
    # O primeiro coeficiente é simplesmente y[0]
    coeficientes[0] = y_tab[0]
    
    return coeficientes

# Achar a integral aproximada da original
def newton_cotes_integral(f, a, b, n):
    """
    Calcula a integral da função f(x) no intervalo [a, b] usando a fórmula de Newton-Cotes.
    
    Parâmetros:
    f -- função a ser integrada
    a -- limite inferior de integração
    b -- limite superior de integração
    n -- número de pontos (grau do polinômio interpolador + 1)
    
    Retorna:
    Aproximação da integral de f(x) de a até b
    """
    x_tab = np.linspace(a, b, n)  # Define pontos igualmente espaçados
    y_tab = f(x_tab)  # Avalia a função nesses pontos
    
    # Passo de integração
    h = (b - a) / (n - 1)
    
    # Coeficientes do polinômio de Newton
    coeficientes = FormaDeNewton(x_tab, y_tab)
    
    # Cálculo da integral aproximada
    integral = h * np.sum(coeficientes * y_tab)
    
    return integral

# Exemplo de chamada (pode remover ou adaptar conforme desejar)

f = lambda x: (x**3 - 4*x + 2)  # função para aproximar
a, b = 1, 3                     # intervalos
n = 5                           # grau 4 + 1 pontos

resultado = newton_cotes_integral(f, a, b, n)
print(f"Aproximação da integral de {a} até {b} = {resultado}")
