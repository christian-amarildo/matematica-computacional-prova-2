# V V V

def bisseccao(a, b, e):
    # Regra do sinal: para existir raíz nesse intervalo, deve-se atender a esse critério
    if f(a) * f(b) >= 0:
        raise ValueError("Nesse intervalo não existe raíz")

    i = 1
    ai = a
    bi = b

    print("Valores iniciais: a =", ai, "b =", bi, )

    while abs(bi - ai) > e: # critério de parada: quando a precisão bi - ai < 0
        xi = (ai + bi) / 2

        if f(ai) * f(xi) < 0:
            bi = xi
        else:
            ai = xi

        print(f"Iteração {i}: a{i} = {ai}, b{i} = {bi}, x{i} = {xi}")

        i += 1

    return (ai + bi)/2

# Exemplo:
def f(x):
    return x**3 - 3*x - 1

# intervalo
a = -1
b = 0

e = 0.15 # precisão

print(bisseccao(a, b, e))