import numpy as np

def regra_dos_trapezios(f, a, b, h=1, quant_interv=1):
    """
    Implementa a regra dos trapézios para aproximar uma integral.
    
    Parâmetros:
        f: função a ser integrada
        a: limite inferior de integração
        b: limite superior de integração
        h: tamanho do intervalo (opcional)
        quant_interv: número de intervalos (opcional)
    """
    # Calcula o número de pontos baseado em quant_interv ou h
    n = max(int((b-a)/h), quant_interv)
    
    # Gera os pontos x
    x = np.linspace(a, b, n+1)
    
    # Calcula os valores da função
    y = f(x)
    
    # Aplica a regra dos trapézios
    integral = (x[1] - x[0]) * ((y[0] + y[-1])/2 + np.sum(y[1:-1]))
    
    return integral

def f(x):
    """
    Função exemplo para teste.
    Neste caso, uma função senoidal simples.
    """
    return np.sin(x)

# Exemplo de uso com diferentes números de intervalos
resultado_10 = regra_dos_trapezios(f, 0, np.pi, quant_interv=10)
resultado_100 = regra_dos_trapezios(f, 0, np.pi, quant_interv=100)
resultado_h01 = regra_dos_trapezios(f, 0, np.pi, h=0.1)

print(f"Aproximação com 10 intervalos: {resultado_10:.6f}")
print(f"Aproximação com 100 intervalos: {resultado_100:.6f}")
print(f"Aproximação com o tamanho do intervalo sendo 0,1: {resultado_h01:.6f}")