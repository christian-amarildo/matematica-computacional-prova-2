import numpy as np

def derivada_numerica(f, x, h=1e-5):
    """
    Calcula a derivada numérica de f(x) usando diferenças finitas.

    Parâmetros:
    f (função): A função f(x).
    x (float): O ponto onde a derivada será calculada.
    h (float): O tamanho do passo para a diferença finita.

    Retorna:
    float: A derivada numérica de f(x) no ponto x.
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def encontrar_pontos_criticos(f, intervalo, tol=1e-6, max_iter=1000):
    """
    Encontra os pontos críticos de uma função f(x) no intervalo dado.

    Parâmetros:
    f (função): A função f(x).
    intervalo (tuple): O intervalo (a, b) onde os pontos críticos serão buscados.
    tol (float): Tolerância para a convergência.
    max_iter (int): Número máximo de iterações.

    Retorna:
    list: Uma lista de pontos críticos (valores de x).
    """
    a, b = intervalo
    pontos_criticos = []

    # Divide o intervalo em pequenos subintervalos para buscar pontos críticos
    x_values = np.linspace(a, b, 1000000)
    for x in x_values:
        # Usa o método de Newton para encontrar onde f'(x) = 0
        x_atual = x
        for _ in range(max_iter):
            derivada = derivada_numerica(f, x_atual)
            if abs(derivada) < tol:
                pontos_criticos.append(x_atual)
                break
            # Atualiza x usando o método de Newton
            segunda_derivada = (derivada_numerica(f, x_atual + tol) - derivada_numerica(f, x_atual - tol)) / (2 * tol)
            if segunda_derivada == 0:
                break  # Evita divisão por zero
            x_atual = x_atual - derivada / segunda_derivada

    # Remove duplicatas e arredonda os valores
    pontos_criticos = np.unique(np.round(pontos_criticos, decimals=6))

    return pontos_criticos

# Exemplo de uso
def f(x):
    return x**3 - 3*x**2 + 2*x  # Função exemplo

intervalo = (-4, 4)  # Intervalo onde os pontos críticos serão buscados
pontos_criticos = encontrar_pontos_criticos(f, intervalo)
print("Pontos críticos:", pontos_criticos)