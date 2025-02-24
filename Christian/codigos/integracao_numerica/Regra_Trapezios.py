import numpy as np  # Importa a biblioteca NumPy, que é útil para operações matemáticas, como a função logaritmo

def calcular_area_trapezio(x0: float, x1: float, num_intervalos: int, funcao) -> float:
    """
    Calcula a área sob a curva definida por `funcao` no intervalo [x0, x1]
    utilizando a regra do trapézio com `num_intervalos` subintervalos.
    
    A regra do trapézio é um método numérico de aproximação de integrais. Ele basicamente aproxima a área sob a
    curva de uma função usando trapézios (ao invés de usar retângulos como na regra dos retângulos).

    Parâmetros:
    x0 (float): Limite inferior do intervalo.
    x1 (float): Limite superior do intervalo.
    num_intervalos (int): Número de subintervalos. O número de subintervalos deve ser inteiro e maior que 0.
    funcao (callable): Função a ser integrada. Esta função deve aceitar um valor numérico e retornar um valor numérico.

    Retorna:
    float: Aproximação da integral no intervalo dado. Caso `num_intervalos` seja menor ou igual a zero, retorna `None`.
    """
    
    # Verifica se o número de subintervalos é válido (deve ser maior que 0)
    if num_intervalos <= 0:
        print("Erro: O número de subintervalos deve ser maior que zero.")
        return None  # Retorna None em caso de erro
    
    # Calcula o tamanho do passo, ou seja, o comprimento de cada subintervalo.
    passo = (x1 - x0) / num_intervalos  # O passo é a distância entre dois pontos consecutivos no intervalo
    
    # Inicializa a lista de valores da função nos pontos relevantes.
    # Aqui, começa com o valor de f(x0) e f(x1), depois para os pontos intermediários (i variando de 1 a num_intervalos-1)
    
    valores_y = [funcao(x0)]  # f(x0) -> valor da função no limite inferior do intervalo (x0)
    
    # Agora, vamos calcular a função nos pontos intermediários (entre x0 e x1).
    # Usamos uma lista de compreensão para calcular a função para cada subintervalo.
    # O coeficiente 2 é usado para os pontos intermediários, porque o trapézio considera esses pontos duas vezes.
    
    valores_y += [2 * funcao(x0 + i * passo) for i in range(1, num_intervalos)]  # Calcula f(x_i) para 1 <= i <= num_intervalos-1, multiplicado por 2.
    
    # Adiciona o valor de f(x1), que é o limite superior do intervalo.
    valores_y.append(funcao(x1))  # f(x1) -> valor da função no limite superior do intervalo (x1)
    
    # Agora que temos todos os valores da função (incluindo os multiplicados por 2), aplicamos a fórmula do trapézio:
    # A fórmula é: área = (h / 2) * [f(x0) + 2 * (f(x1) + f(x2) + ... + f(xn-1)) + f(xn)]
    # Em termos de código: somamos todos os valores da função e multiplicamos pelo passo/2
    
    area_aproximada = (passo * 0.5) * sum(valores_y)  # A soma de todos os valores é multiplicada por (h / 2), onde h é o tamanho do passo
    
    # Retorna a área aproximada sob a curva, que é a integral numérica da função no intervalo [x0, x1]
    return area_aproximada

def funcao_exemplo(x: float) -> float:
    """
    Exemplo de função para integração: f(x) = x² * ln(x) + 1
    Esta é a função que será usada para o cálculo da integral. Você pode modificar esta função para integrar qualquer outra.
    
    Parâmetros:
    x (float): O valor de entrada em que a função será avaliada.

    Retorna:
    float: O valor de x² * ln(x) + 1 para o valor de x fornecido.
    """
    return (x**2) * np.log(x) + 1  # Calcula x² * ln(x) + 1

if __name__ == "__main__":  # Verifica se o código está sendo executado diretamente (não importado como módulo)
    # Exemplo de uso da função calcular_area_trapezio.
    # Vamos calcular a integral de f(x) = x² * ln(x) + 1 no intervalo [1.2, 1.4] com 2 subintervalos.
    
    resultado = calcular_area_trapezio(1.2, 1.4, 2, funcao_exemplo)  # Chama a função com o intervalo [1.2, 1.4] e 2 subintervalos
    
    # Exibe o resultado da área aproximada
    if resultado is not None:  # Verifica se o resultado não é None (ou seja, se não houve erro)
        print(f"Área aproximada: {resultado:.6f}")  # Imprime o valor da área aproximada com 6 casas decimais

      
      
      

# Explicação Detalhada
# 1. Função calcular_area_trapezio
# Essa função implementa a Regra do Trapézio, que é um método numérico simples e eficiente para aproximar integrais definidas. Ela divide o intervalo em pequenos subintervalos e aproxima a área sob a curva como a soma de áreas de trapézios.

# Parâmetros:
# x0 e x1: São os limites inferior e superior da integral. Ou seja, a integral será calculada no intervalo 
# [
# 𝑥
# 0
# ,
# 𝑥
# 1
# ]
# [x 
# 0
# ​
#  ,x 
# 1
# ​
#  ].

# num_intervalos: Número de subintervalos usados para dividir o intervalo 
# [
# 𝑥
# 0
# ,
# 𝑥
# 1
# ]
# [x 
# 0
# ​
#  ,x 
# 1
# ​
#  ]. Quanto maior o número de subintervalos, maior a precisão da aproximação.

# funcao: A função a ser integrada. Ela deve aceitar um valor 
# 𝑥
# x e retornar o valor de 
# 𝑓
# (
# 𝑥
# )
# f(x).

# Passo a Passo:
# Verificação do número de subintervalos:

# O número de subintervalos deve ser maior que zero. Caso contrário, a função retorna None.
# Cálculo do passo (passo):

# O passo é a distância entre dois pontos consecutivos no intervalo 
# [
# 𝑥
# 0
# ,
# 𝑥
# 1
# ]
# [x 
# 0
# ​
#  ,x 
# 1
# ​
#  ]. Ele é dado pela fórmula \text{passo} = \frac{x_1 - x_0}{\text{num_intervalos}}.
# Avaliação da função nos pontos relevantes:

# A lista valores_y armazena os valores da função 
# 𝑓
# (
# 𝑥
# )
# f(x) nos pontos 
# 𝑥
# 0
# x 
# 0
# ​
#  , 
# 𝑥
# 1
# x 
# 1
# ​
#   e nos pontos intermediários.
# O valor da função nos pontos intermediários (aqueles que não são 
# 𝑥
# 0
# x 
# 0
# ​
#   ou 
# 𝑥
# 1
# x 
# 1
# ​
#  ) é multiplicado por 2, pois a regra do trapézio atribui um peso maior a esses pontos.
# Cálculo da área:

# A fórmula da Regra do Trapézio é aplicada somando os valores de 
# 𝑓
# (
# 𝑥
# )
# f(x) com seus respectivos coeficientes. Depois, multiplicamos essa soma pelo passo / 2 para obter a área aproximada sob a curva.
# Retorno:

# A função retorna o valor da área aproximada, que é a integral numérica de 
# 𝑓
# (
# 𝑥
# )
# f(x) no intervalo 
# [
# 𝑥
# 0
# ,
# 𝑥
# 1
# ]
# [x 
# 0
# ​
#  ,x 
# 1
# ​
#  ].
# 2. Função funcao_exemplo
# Esta é uma função exemplo, que será utilizada para ilustrar o funcionamento do método. A função que estamos integrando é 
# 𝑓
# (
# 𝑥
# )
# =
# 𝑥
# 2
# ln
# ⁡
# (
# 𝑥
# )
# +
# 1
# f(x)=x 
# 2
#  ln(x)+1, mas você pode modificar essa função para calcular a integral de qualquer outra função matemática.

# Como modificar:
# Se quiser calcular a integral de uma função diferente, basta mudar o corpo da função funcao_exemplo. Por exemplo:
# python
# Copiar
# Editar
# def funcao(x: float) -> float:
#     return x**3 - 2*x + 4  # Exemplo de outra função
# 3. Como Usar o Código
# Passo 1: Defina a função que deseja integrar. A função deve aceitar um valor e retornar o valor de 
# 𝑓
# (
# 𝑥
# )
# f(x).
# Passo 2: Chame a função calcular_area_trapezio com os parâmetros desejados: limites 
# 𝑥
# 0
# x 
# 0
# ​
#  , 
# 𝑥
# 1
# x 
# 1
# ​
#  , número de subintervalos, e a função a ser integrada.
# Exemplo:

# python
# Copiar
# Editar
# resultado = calcular_area_trapezio(1.2, 1.4, 2, funcao_exemplo)
# Isso calculará a integral de 
# 𝑓
# (
# 𝑥
# )
# f(x) no intervalo de 1.2 a 1.4 usando 2 subintervalos.

# Considerações Finais:
# Precisão: A precisão do método depende do número de subintervalos. Quanto maior o número de subintervalos, mais precisa será a aproximação. No entanto, aumentar o número de subintervalos pode tornar o cálculo mais demorado.

# Extrapolação: Se você precisa de uma precisão muito alta, pode ser interessante usar métodos mais avançados ou aumentar o número de subintervalos, até que o erro de aproximação seja suficientemente pequeno.
