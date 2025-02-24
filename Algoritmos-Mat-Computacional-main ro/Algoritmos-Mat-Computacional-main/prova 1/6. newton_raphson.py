# V V

def newton_raphson(x0, e1, e2):
    # Verifica se o ponto inicial já é solução
    if abs(f(x0)) < e1:
        return x0 # retorna aproximação inicial
    
    k = 0  # Contador de iterações
    
    while True:
        # Verifica se a derivada é zero para evitar divisão por zero
        if df(x0) == 0:
            raise ValueError("A derivada é zero em x = {:.6f}. Método falhou.".format(x0))
        
        # Calcula a próxima iteração
        x1 = x0 - f(x0) / df(x0)
        
        # Critérios de parada: quando f(x1) < e1 ou x1 - x0 < e2
        if abs(f(x1)) < e1 or abs(x1 - x0) < e2:
            return x1  # Retorna a raiz encontrada
        
        # Atualiza x0 para a próxima iteração
        x0 = x1
        k += 1
    

# Exemplo:
def f(x):
    return x**2 - 2

def df(x):
    return 2*x

# precisões
e1, e2 = 1e-6, 1e-6

# chute inicial
x0 = 1

print(newton_raphson(x0, e1, e2))