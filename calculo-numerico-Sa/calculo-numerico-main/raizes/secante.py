import math
from achar_raiz import hunt_root


def secant(a: float, b: float, max_iter: int, e: float, f = lambda x: ...):
    if abs(f(a)) < e:
        x = a
        return x

    if abs(f(b)) < e or abs(b - a) < e:
        x = b
        return x

    for _ in range(max_iter):
        x = b - (f(b)/(f(b)-f(a)))*(b - a)
        if x < 0:
            print(x)

        if abs(f(x)) < e or abs(x - b) < e:
            return x
        
        a = b
        b = x

    return x


# EXEMPLO DE USO

# f = lambda x: (x**math.log(x)) + x**2 + x**3 * math.sin(x)
# intervalos = hunt_root(1, 20, f)

# for a, b in intervalos:
#     raiz = secant(a, b, 1000, 0.00001, f)
#     print(f"A raiz encontrada no intervalo [{a},{b}] é: {raiz}")