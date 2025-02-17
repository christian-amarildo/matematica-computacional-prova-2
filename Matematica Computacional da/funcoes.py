import math

# Funções para testar
def f1(x):
    return x**6 - math.sin(x) / math.sqrt(x + 5) + math.log(x + 2) - math.exp(x)

def f2(x):
    return x**7 / math.exp(x) + math.cos(x) - math.log(x + 3) + math.sqrt(x + 4)

def f3(x):
    return math.exp(x) - x**5 / math.log(x + 2) + math.sin(math.sqrt(x + 3)) - x**3

def f4(x):
    if x == -1:
        raise ValueError("Divisão por zero encontrada.")
    return math.sqrt(x**2 + 5) - math.exp(x) + math.log(x + 1) - math.sin(x) / (x**3 + 1)

def f5(x):
    return x**8 - math.cos(x) / math.sqrt(x + 6) + math.log(x + 4) - math.exp(math.sin(x))

# Testando uma das funções
x0 = 0.5  # Primeiro chute inicial
x1 = 1.0  # Segundo chute inicial
tol = 1e-6

try:
    raiz, iteracoes = secant_method(f1, x0, x1, tol)  # Substitua f1 por f2, f3, etc., para testar as outras
    print(f"A raiz encontrada é x = {raiz} após {iteracoes} iterações.")
    print(f"Verificação: f({raiz}) = {f1(raiz)}")
except ValueError as e:
    print(e)
