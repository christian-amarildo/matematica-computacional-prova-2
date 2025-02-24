import numpy as np  # Importa o pacote numpy, que é usado para operações numéricas, como a função np.sqrt

def calcular_regra13simpson(x0: float, x1: float, num_intervalos: int, funcao) -> float:
    """
    Calcula a aproximação da integral definida usando a Regra 1/3 de Simpson.

    A Regra 1/3 de Simpson é um método numérico de integração que pode ser usado para aproximar integrais de funções 
    contínuas e suaves. A regra utiliza uma aproximação polinomial quadrática para estimar a área sob a curva da função.

    Parâmetros:
    x0 (float): Limite inferior da integral.
    x1 (float): Limite superior da integral.
    num_intervalos (int): Número de subintervalos (deve ser par, ou seja, número de intervalos deve ser ímpar de pontos)
    funcao (callable): Função a ser integrada. Esta função deve aceitar um único valor como entrada e retornar um valor numérico.

    Retorna:
    float: Aproximação da integral ou None caso o número de subintervalos seja ímpar.
    """
    
    # Verificação: A Regra de Simpson 1/3 só pode ser aplicada se o número de intervalos for par.
    if num_intervalos % 2 != 0:
        print("Erro: O número de subintervalos deve ser par.")  # Imprime um erro caso o número de intervalos seja ímpar
        return None  # Retorna None em caso de erro
    
    # Calcula o tamanho do passo, ou seja, o comprimento de cada subintervalo.
    h = (x1 - x0) / num_intervalos  # h é a distância entre dois pontos consecutivos (subintervalos)

    # Inicializa a lista de valores de f(x) nos pontos relevantes. Começa com o valor de f(x0).
    valores_y = [funcao(x0)]  # Aqui, 'funcao(x0)' avalia a função no ponto x0 (limite inferior)

    # A seguir, faz-se a aplicação dos coeficientes 4 e 2 alternadamente nos pontos internos.
    # A regra de Simpson aplica um coeficiente de 4 para os pontos ímpares e 2 para os pares.
    for i in range(1, num_intervalos):  # Laço que vai de 1 até num_intervalos-1, cobrindo todos os pontos internos
        x_i = x0 + (h * i)  # Calcula o ponto x_i, que é um ponto dentro do intervalo [x0, x1]
        
        # A Regra de Simpson atribui um coeficiente de 4 para os índices ímpares e 2 para os pares.
        coeficiente = 4 if i % 2 == 1 else 2  # Se 'i' for ímpar, o coeficiente é 4; caso contrário, é 2
        
        # Calcula o valor da função nesse ponto e multiplica pelo coeficiente
        valores_y.append(coeficiente * funcao(x_i))  # Adiciona o valor de f(x_i) multiplicado pelo coeficiente

    # Agora, adicionamos o valor de f(x1), que é o limite superior da integral
    valores_y.append(funcao(x1))  # Adiciona f(x1) (limite superior) na lista de valores de f(x)

    # A fórmula da Regra 1/3 de Simpson é aplicada somando todos os valores de f(x) com os respectivos coeficientes.
    # Multiplicamos a soma por h/3 para obter a aproximação final da integral.
    area_aproximada = (h / 3) * sum(valores_y)  # Soma todos os termos e aplica a fórmula

    return area_aproximada  # Retorna a área aproximada calculada

# Função exemplo que será integrada.
def funcao_exemplo(x: float) -> float:
    """
    Exemplo de função para integração: f(x) = sqrt(x) + 1/x
    Esta função retorna o valor de sqrt(x) + 1/x para um dado x.

    Parâmetros:
    x (float): O valor de entrada no qual a função será avaliada.

    Retorna:
    float: Resultado de sqrt(x) + 1/x.
    """
    return np.sqrt(x) + 1/x  # Retorna a soma de sqrt(x) e 1/x

if __name__ == "__main__":  # Verifica se o código está sendo executado diretamente (não importado)
    # Exemplo de uso da função com a função funcao_exemplo
    # Vamos calcular a integral de sqrt(x) + 1/x no intervalo [1.4, 1.8] com 4 intervalos (número par)
    
    resultado = calcular_regra13simpson(1.4, 1.8, 4, funcao_exemplo)  # Chama a função de integração
    
    # Imprime o resultado da aproximação da integral
    if resultado is not None:  # Verifica se o resultado é válido
        print(f"Área aproximada: {resultado:.6f}")  # Exibe o valor da área aproximada com 6 casas decimais







# Explicação Completa do Código
# 1. Função calcular_regra13simpson
# Esta função implementa o método Regra 1/3 de Simpson, que é uma técnica numérica de aproximação de integrais definidas. A regra se baseia na ideia de aproximar a função por um polinômio de segundo grau (parabólica) entre os pontos. A integral é então estimada pela soma das áreas dessas parábolas sobre os intervalos.

# Parâmetros:
# x0 e x1: São os limites da integral. O valor da integral será calculado no intervalo 
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

# num_intervalos: Número de subintervalos em que o intervalo 
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
#  ] será dividido. Para que a Regra de Simpson funcione corretamente, o número de subintervalos deve ser par.

# funcao: Uma função que deve ser passada como argumento, representando a função que se deseja integrar.

# Como Funciona:
# Verificação de subintervalos ímpares: A Regra 1/3 de Simpson exige que o número de subintervalos seja par. Caso contrário, um erro é gerado.

# Cálculo do passo (h): O passo h é a distância entre dois pontos consecutivos, ou seja, o comprimento de cada subintervalo.

# Avaliação da função nos pontos relevantes: O código calcula os valores da função nos pontos 
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
#   e nos pontos intermediários. Para os pontos internos, a função aplica os coeficientes 4 e 2 alternadamente:

# Coeficiente 4 para pontos ímpares.
# Coeficiente 2 para pontos pares.
# Aplicação da fórmula: O valor final da integral é calculado usando a fórmula da Regra de Simpson, onde a soma dos valores é multiplicada por 
# ℎ
# /
# 3
# h/3.

# Retorno: A função retorna a área aproximada sob a curva, ou seja, o valor da integral.

# 2. Função funcao_exemplo
# Essa função serve apenas como um exemplo de função que pode ser integrada. Ela retorna o valor de 
# 𝑥
# +
# 1
# 𝑥
# x
# ​
#  + 
# x
# 1
# ​
#   para um dado valor de 
# 𝑥
# x. Você pode modificar essa função para integrar qualquer outra função matemática, como 
# 𝑥
# 2
# x 
# 2
#  , 
# 𝑒
# 𝑥
# e 
# x
#  , ou funções trigonométricas.

# 3. Como Usar o Código
# Para usar o código, você só precisa definir o intervalo de integração, o número de subintervalos (certifique-se de que seja par), e passar a função a ser integrada. O código usa como exemplo a função 
# 𝑓
# (
# 𝑥
# )
# =
# 𝑥
# +
# 1
# 𝑥
# f(x)= 
# x
# ​
#  + 
# x
# 1
# ​
#   no intervalo de 
# 1.4
# 1.4 a 
# 1.8
# 1.8, com 4 subintervalos.

# Exemplo de uso:
# python
# Copiar
# Editar
# resultado = calcular_regra13simpson(1.4, 1.8, 4, funcao_exemplo)
# Isso calculará a integral da função no intervalo de 
# 1.4
# 1.4 a 
# 1.8
# 1.8 usando 4 subintervalos.

# 4. Modificações Possíveis
# Alterar a função a ser integrada: Para usar uma função diferente, basta definir outra função, como:

# python
# Copiar
# Editar
# def minha_funcao(x):
#     return x**2  # Exemplo de função que retorna x^2
# Alterar o número de subintervalos: Para obter uma maior precisão, você pode aumentar o número de subintervalos (certifique-se de que seja um número par). Por exemplo, para 10 subintervalos:

# python
# Copiar
# Editar
# resultado = calcular_regra13simpson(1.4, 1.8, 10, funcao_exemplo)
# Alterar os limites da integral: Basta modificar os valores de x0 e x1 para o intervalo desejado.

# 5. Considerações
# A precisão do método depende do número de subintervalos. Quanto maior o número de subintervalos, mais precisa será a aproximação.
# Se o número de subintervalos for muito baixo (como 2), o erro da aproximação pode ser maior.
# Com esses comentários, o código deve estar bem explicado para você entender como ele funciona, como usá-lo, e como modificar para diferentes casos. Se precisar de mais detalhes ou tiver outras dúvidas, fico à disposição!







