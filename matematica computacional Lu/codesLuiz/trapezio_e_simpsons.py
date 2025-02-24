import numpy as np
import matplotlib.pyplot as plt

def regra_trapezios(f, a, b, n):
   
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])
    return integral

def regra_simpson(f, a, b, n):
  
    if n % 2 == 1:
        raise ValueError("numero de subintervalos para a regra de Simpson.")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = (h / 3) * (y[0] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2]) + y[n])
    return integral

# exemplo de uso
f = lambda x: x**2  # função polinomial

a, b = 0, 2
n = 4  

integral_trapezios = regra_trapezios(f, a, b, n)
print("integral pela Regra dos Trapézios:", integral_trapezios)

integral_simpson = regra_simpson(f, a, b, n)
print("integral pela Regra de Simpson:", integral_simpson)