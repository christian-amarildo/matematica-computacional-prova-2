# V V

import math

def secante(x0, x1, e1, e2):
    if abs(f(x0)) < e1:
        return x0
    
    if abs(x1) < e1 or abs(x1- x0) < e2:
        return x1
    
    k = 1

    while True:
        x2 = x1 - (f(x1)/(f(x1) - f(x0))) * (x1 - x0)

        # Critério de parada: f(x2) < e1 ou x2-x1 < e2
        if abs(f(x2)) < e1 or abs(x2 - x1) < e2:
            return x2
        
        x0 = x1
        x1 = x2

        k += 1

def f(x):
    return math.e**(-x**2) - math.cos(x)

e1, e2 = 1e-6, 1e-6

x0 = 1.2
x1 = 2.2

print(secante(x0, x1, e1, e2))
