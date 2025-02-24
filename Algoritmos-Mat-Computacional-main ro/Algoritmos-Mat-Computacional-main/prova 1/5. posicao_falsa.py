# V V

from math import e

def posicao_falsa(a, b, e1, e2):
    # Regra do sinal: para existir raíz nesse intervalo, deve-se atender a esse critério
    if f(a) * f(b) >= 0:
        raise ValueError("Nesse intervalo não existe raíz")

    k = 1

    print(f"Valores iniciais: a = {a}, b = {b}")

    # Verificar se o intervalo é pequeno o suficiente (ou seja, se a precisão é alta)
    if abs(b - a) < e1:
        if abs(f(a)) < e2:
            return a
        elif abs(f(b)) < e2:
            return b
        else:
            return (a + b) / 2

    while True:
        # Calcula o ponto de posição falsa
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))

        # Verificar se o valor de f(x) é pequeno o suficiente
        if abs(f(x)) < e2:
            return x

        # Atualizar os limites do intervalo
        if f(a) * f(x) > 0:
            a = x
        else:
            b = x

        print(f"Iteração {k}: a{k} = {a}, b{k}, = {b}")

        # Critério de parada baseado no intervalo
        if abs(b - a) < e1:
            return x

        k += 1

# Exemplo:
def f(x):
    return e**(-2*x) - x**2

# intervalo:
a = 0
b = 2

# precisões:
e1 = 1e-6
e2 = 1e-6

print("Resultado:", posicao_falsa(a, b, e1, e2))