import numpy as np

def regra_1terco_simpson(f, a, b):
    """
    Implementa a Regra de Simpson de 1/3 para aproximar integrais definidas.
    
    Parâmetros:
        f: função de dentro da integral a ser integrada
        a: limite inferior da integral
        b: limite superior da integral
        
    Retorna:
        Aproximação da integral usando a Regra de Simpson de 1/3
    """
    
    # achando o tamanho dos intervalos
    h = (b - a) / 2

    # achando o ponto médio
    pt_medio = a + h

    # Fórmula correta: h/3 * [f(a) + 4*f(pt_medio) + f(b)]
    I = h*(f(a) + 4*f(pt_medio) + f(b)) / 3
    # funciona tanto para casos lineares quanto não lineares

    return I

def f(x):
    """
    Caso de teste: x*e^x
    Função que está dentro da integral
    """
    return x*(np.e**x)

m = regra_1terco_simpson(f, 1.6, 2.0)

print(f"Resultado da regra de simpson: {m:.06f}")