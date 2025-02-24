import math
import numpy as np


# Função para verificar intervalos que podem conter raízes (pelo método da mudança de sinal)
def hunt_root(a: float, b: float, f = lambda x: ...):
    # Cria um objeto de polinômio usando o vetor de coeficientes fornecido
    intervals = []
    counter = 0  # Contador de raízes encontradas
    
    # Itera sobre os inteiros dentro do intervalo [a, b]
    for x in range(a, b + 1):
        # Verifica se o produto das funções em pontos consecutivos muda de sinal
        # Se f(x) * f(x + 1) < 0, significa que há uma mudança de sinal, indicando que há uma raiz entre x e x+1
        if f(x) * f(x + 1) < 0:
            # print(f"Tem raiz no intervalo [{x}, {x + 1}]")  # Imprime que há uma raiz no intervalo
            intervals.append((x, x+1))
            counter += 1  # Incrementa o contador de raízes encontradas
            # print(f"Não tem raiz no intervalo [{x}, {x + 1}]")  # Imprime que não há raiz no intervalo

    print(f"Há {counter} raizes no intervalo [{a}, {b}]")
    return intervals  # Retorna o número de raízes encontradas no intervalo


import numpy as np

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
    x_values = np.linspace(a, b, 1000)
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

intervalo = (-10, 10)  # Intervalo onde os pontos críticos serão buscados
pontos_criticos = encontrar_pontos_criticos(f, intervalo)
print("Pontos críticos:", pontos_criticos)


# DESCOMENTAR SE NO DESESPERO (outra hunt_root)
"""
# Função para encontrar a raiz de um intervalo usando o método da bisseção
def find_root(vetor: list, erro: float, menor_x: int = -10, maior_x: int = 10):
    # Cria o polinômio a partir do vetor de coeficientes
    f = np.poly1d(vetor)
    
    a = menor_x  # Limite inferior do intervalo
    b = maior_x  # Limite superior do intervalo
    p_medio = (a + b) / 2  # Calcula o ponto médio inicial
    contador = 0  # Inicializa o contador de iterações
    
    # Enquanto o valor absoluto da função no ponto médio for maior que o erro desejado
    while abs(f(p_medio)) > erro:
        # Se a função nos limites a e p_medio tiver sinais opostos, a raiz está entre a e p_medio
        if f(a) * f(p_medio) < 0:
            b = p_medio  # Ajusta o limite superior para o ponto médio
        else: 
            a = p_medio  # Caso contrário, ajusta o limite inferior para o ponto médio
        
        contador += 1  # Incrementa o contador de iterações
        p_medio = (a + b) / 2  # Recalcula o novo ponto médio

    print(f"A raiz do intervalo [{menor_x}, {maior_x}] é {p_medio}")  # Imprime a raiz encontrada

"""

# EXEMPLO DE USO
# intervals = hunt_root(1, 20, lambda x: (x**math.log(x)) + x**2 + x**3 * math.sin(x))
# print("intervalos: ", intervals)
