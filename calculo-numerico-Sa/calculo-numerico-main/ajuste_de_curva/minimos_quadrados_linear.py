# PODE-SE USAR PARA ALÉM DO INTERVALO DE X

def get_a(X: list, Y: list):
    n = len(X)
    x_quadratic = 0
    xy = 0
    x = 0
    y = 0
    for i in range(n):
        x_quadratic += X[i]**2
        xy += X[i]*Y[i]
        x += X[i]
        y += Y[i]
    
    numerator = (n*xy) - (x * y)
    denominator = (n*x_quadratic) - (x**2)
    result = numerator/denominator
    return result


def get_b(X: list, Y: list):
    n = len(X)
    x_quadratic = 0
    xy = 0
    x = 0
    y = 0
    for i in range(n):
        x_quadratic += X[i]**2
        xy += X[i]*Y[i]
        x += X[i]
        y += Y[i]
    
    numerator = (x * xy) - (y * x_quadratic)
    denominator = (x**2) - (n*x_quadratic)
    result = numerator/denominator
    return result


def minimos_quadrados_linear(X: list, Y: list, x):
    """
    É possível que os valores de a e b precisam mudar quando em situação de exponencial.
    Isto é identificado conforme a questão.
    """
    a = get_a(X, Y)
    b = get_b(X, Y) # Por exemplo, talvez tenhamos que fazer ln(b) para conseguir seu valor real
    print(f"a: {a}, b: {b}")
    result = a*x + b
    return result
