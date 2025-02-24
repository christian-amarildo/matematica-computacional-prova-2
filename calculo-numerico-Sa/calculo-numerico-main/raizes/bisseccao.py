import math
from achar_raiz import hunt_root


def bissection(a: float, b: float, max_iter: int, error: float, f = lambda x: ...):
    for _ in range(max_iter):
        midpoint = (a + b)/2
        check_signal = f(a) * f(midpoint)
        if check_signal < 0:
            b = midpoint
        elif check_signal > 0:
            a = midpoint
        else:
            return midpoint
        
        if abs(f(midpoint)) < error:
            return midpoint

    return midpoint


# EXEMPLO DE USO

# f = lambda x: (x**math.log(x)) + x**2 + x**3 * math.sin(x)
# intervalos = hunt_root(1, 20, f)

# for a, b in intervalos:
#     raiz = bissection(a, b, 1000, 0.00001, f)
#     print(f"A raiz encontrada no intervalo [{a},{b}] é: {raiz}")