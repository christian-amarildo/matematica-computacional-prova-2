

def quase_newton(f, x0, x1, tol=1e-6, max_iter=100):
    x_prev = x0
    x = x1
    iteracoes = 0
    
    while iteracoes < max_iter:
        iteracoes += 1
        
        aproximacao_derivada = ( f(x + (x_prev - x)) - f(x) ) / (x_prev - x)
        x_next = x - f(x) / aproximacao_derivada

        erro_absoluto = abs(x_next - x)
        erro_relativo = erro_absoluto / abs(x_next)

        print('| {:10} | {:<20} | {:<25} | {:<25} | {:<25} | {:<25}|'.format(iteracoes, x_next, x_prev, f(x), erro_absoluto, erro_relativo))

        if erro_relativo < tol:
            return x_next, iteracoes
        
        x_prev = x
        x = x_next
        
    return None, iteracoes



def f(x):
    return x**2 - 5


x0 = 3.0
x1 = 1.0

print("Método de Quase-Newton")
print('| {:10} | {:<20} | {:<25} | {:<25} | {:<25} | {:<25}|'.format("iteracoes", "x_next", "x_prev", "f(x)", "erro_absoluto", "erro_relativo"))

raiz, iteracoes = quase_newton(f, x0, x1)

if raiz is not None:
    print("Convergiu em ", iteracoes, " para ", raiz)
else:
    print("O método não convergiu após", iteracoes, "iterações.")

