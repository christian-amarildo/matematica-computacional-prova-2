import numpy as np
import math
from achar_raiz import hunt_root

def newton_raphson(x0: float, max_iter: int, e: float, f = lambda x: ..., derivative = lambda x: ...):
    for _ in range(max_iter):
        if abs(f(x0)) < e:
            return x0
        
        if derivative(x0) == 0:
            raise f"A derivada de f(x) para este x = {x0} é zero..."
        
        x1 = x0 - (f(x0)/derivative(x0))
        
        if abs(f(x1)) < e or abs(x1 - x0) < e:
            x = x1
            return x
        
        x0 = x1
    
    raise "O método não convergiu..."


# EXEMPLO DE USO

# f = lambda x: (x**math.log(x)) + x**2 + x**3 * math.sin(x)
# deriv_f = lambda x: (2 * np.exp(np.log(x)**2) * np.log(x) / x) + 2*x + 3*x**2 * np.sin(x) + np.cos(x) * x**3
# intervalos = hunt_root(1, 20, f)

# for a, b in intervalos:
#     raiz = newton_raphson(a, 1000, 0.00001, f, deriv_f)
#     print(f"A raiz encontrada no intervalo [{a},{b}] é: {raiz}")
