

def falsa_posicao(f, a, b, tol=1e-3, max_iter=100):
    iteracoes = 0
    
    if (f(a) * f(b) > 0):
        return None, 0

    while iteracoes < max_iter:
        
        fa = f(a)
        fb = f(b)
        
        pontoMedio = (a*fb - b*fa) / (fb - fa)
        
        f_pontoMedio = f(pontoMedio)

        erro_absoluto = abs(b - a)
        erro_relativo = erro_absoluto / abs(b)

        print('| {:10} | {:<20} | {:<25} | {:<25} | {:<25} | {:<25}|'.format(iteracoes, pontoMedio, f(a), f(b), erro_absoluto, erro_relativo))

        if erro_relativo < tol:
            return pontoMedio, iteracoes
        
        if (fa * f_pontoMedio > 0):
            a = pontoMedio
        else:
            b = pontoMedio
        iteracoes += 1
    return pontoMedio, iteracoes



def f(x):
    return x**2 - 5


a = 2.0
b = 3.0

print("Método de Falsa Posição")
print('| {:^10} | {:^20} | {:^25} | {:^25} | {:^25} | {:^25}|'.format("iteracoes", "pontoMedio", "f(a)", "f(b)", "erro_absoluto", "erro_relativo"))

raiz, iteracoes = falsa_posicao(f, a, b)

print("Convergiu em ", iteracoes, " iterações para ", raiz)
