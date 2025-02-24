from math import e, log

def ha_raiz(funcao, limA, limB):
    if funcao(limA) * funcao(limB) < 0:
        return True
    return False

def tabela_sinais(funcao, limA, limB):
    passo = abs(limA - limB) / 100
    n = min(limA, limB)
    tabela = {}
    while n <= max(limA, limB):
        if funcao(n) > 0:
            tabela[n] = '+'
        else:
            tabela[n] = '-'
        n += passo
    return tabela

def tabela_raizes(funcao, limA, limB, iteracoes=1000):
    passo = abs(limA - limB) / iteracoes
    n = limA
    tabela = []
    while n <= limB:
        if ha_raiz(funcao, n, n + passo):
            tabela.append((n, n + passo))
        n += passo
    return tabela

def bisseccao(funcao, limA, limB, precisao = 0.1):
    meio = (limA + limB) / 2
    while abs(limA - limB) > precisao:
        if funcao(limA) * funcao(meio) < 0:
            limB = meio
        else:
            limA = meio
        meio = (limA + limB) / 2
    return meio

def posicao_falsa(funcao, limA, limB, precisao = 0.1):
    meio = (limA * funcao(limB) - limB * funcao(limA)) / (funcao(limB) - funcao(limA))
    while abs(limA - limB) > precisao:
        if funcao(limA) * funcao(meio) < 0:
            limB = meio
        else:
            limA = meio
        meio = (limA * funcao(limB) - limB * funcao(limA)) / (funcao(limB) - funcao(limA))
    return meio

def metodo_newton(funcao, derivada, raiz, precisao=0.1):
    iter_max = 100000

    raiz1 = raiz - (funcao(raiz) / derivada(raiz))
    i = 0
    while (abs(raiz1 - raiz) > precisao) or i < iter_max:
        raiz = raiz1 - (funcao(raiz1) / derivada(raiz1))
        raiz1 = raiz - (funcao(raiz) / derivada(raiz))
        i += 1
    return raiz

def encontrar_raizes(funcao, limA, limB, metodo, derivada=None, iteracoes=1000, precisao=0.1):
    # Encontra intervalos das raízes da função
    tabela = tabela_raizes(funcao, limA, limB, iteracoes)
    raizes = []
    for coords in tabela:
        match metodo:
            case 0:
                raizes.append(bisseccao(funcao, coords[0], coords[1], precisao))
            case 1:
                raizes.append(posicao_falsa(funcao, coords[0], coords[1], precisao))
            case 2:
                raizes.append(metodo_newton(funcao, derivada, coords[0], precisao))
    return raizes


def exemploA(x):
    return (x**3) - (9*x) + 3

def derivadaA(x):
    return 3*(x**2) - 9

def exemploB(x):
    if x >= 0:
        return x**(1/2) - (5 * (e ** -x))

def exemploC(x):
    if x > 0:
        return x * log(x, 10) - 1

print(encontrar_raizes(exemploA, -10, 10, 0, precisao=0.000001))
print(encontrar_raizes(exemploA, -10, 10, 1, precisao=0.000001))
print(encontrar_raizes(exemploA, -10, 10, 2, derivada=derivadaA, precisao=0.000001))
