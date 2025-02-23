

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):

    x = x0
    iteracoes = 0

    while iteracoes < max_iter:
        iteracoes += 1
        
        x_next = x - f(x) / df(x)

        erro_absoluto = abs(x_next - x)
        erro_relativo = erro_absoluto / abs(x_next)

        print('| {:10} | {:<20} | {:<25} | {:<25} | {:<25} | {:<25}|'.format(iteracoes, x_next, f(x_next), df(x_next), erro_absoluto, erro_relativo))

        if erro_relativo < tol:
            return x_next, iteracoes
        
        x = x_next
    
    return None, iteracoes



def f(x):
    return x**2 - 5

def df(x):
    return 2 * x


x0 = 1

print("Método de Newton-Raphson")
print('| {:10} | {:<20} | {:<25} | {:<25} | {:<25} | {:<25}|'.format("iteracoes", "x_next", "x_prev", "f(x)", "erro_absoluto", "erro_relativo"))

raiz, iteracoes = newton_raphson(f, df, x0, 1e-5)

if raiz is not None:
    print("Convergiu em ", iteracoes, " para ", raiz)
else:
    print("O método não convergiu após", iteracoes, "iterações.")

