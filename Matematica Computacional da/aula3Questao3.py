import math

def calcular_ex_série_taylor(x, n):
    # Calcula e^x pela série de Taylor até o termo n
    soma = 0
    for k in range(n+1):
        soma += (x**k) / math.factorial(k)
    return soma

def calcular_ex_negativo(x, n):
    # Caso de x negativo, calcula diretamente e^x e 1/e^x
    if x < 0:
        y = -x
        e_x_direto = calcular_ex_série_taylor(x, n)
        e_x_inverso = 1 / calcular_ex_série_taylor(y, n)
        return e_x_direto, e_x_inverso
    else:
        e_x_direto = calcular_ex_série_taylor(x, n)
        return e_x_direto, None
        


def calcular_ex_série_taylor_otimizada(x, n):
    soma = 1.0  # A soma começa com 1, que é o primeiro termo da série (k=0)
    termo = 1.0  # O primeiro termo também é 1 (x^0 / 0!)
    
    for k in range(1, n + 1):
        termo *= x / k  # Atualiza o termo como o anterior multiplicado por x/k
        soma += termo  # Soma o termo atual à soma
    
    return soma
print(calcular_ex_série_taylor_otimizada(15,100))



print("Um criterio de parada poderia ser por comparação com um valor escolido, quando o valor do termo se tornar menor que ele, o calculo para")