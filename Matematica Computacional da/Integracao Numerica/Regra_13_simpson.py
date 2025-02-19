# Importa a biblioteca numpy, que será usada para funções matemáticas como a raiz quadrada.
import numpy as np

# Define a função que calcula a aproximação da integral usando a Regra 1/3 de Simpson.
def calcular_regra13simpson(x0: float, x1: float, num_intervalos: int, funcao) -> float:
    """
    Calcula a aproximação da integral definida usando a Regra 1/3 de Simpson.

    Parâmetros:
    x0 (float): Limite inferior da integral.
    x1 (float): Limite superior da integral.
    num_intervalos (int): Número de subintervalos (deve ser par).
    funcao (callable): Função a ser integrada.

    Retorna:
    float: Aproximação da integral ou None caso o número de subintervalos seja ímpar.
    """
    
    # Verifica se o número de subintervalos é ímpar. Caso seja, retorna um erro.
    if num_intervalos % 2 != 0:
        print("Erro: O número de subintervalos deve ser par.")  # Mensagem de erro caso o número de intervalos seja ímpar.
        return None  # Retorna None, pois a Regra 1/3 de Simpson só pode ser usada com número par de subintervalos.
    
    # Calcula o tamanho do passo (h), ou seja, o comprimento de cada subintervalo.
    h = (x1 - x0) / num_intervalos
    
    # Inicializa uma lista de valores para armazenar os resultados da função nos pontos relevantes (x0 é o primeiro).
    valores_y = [funcao(x0)]  # O primeiro valor é a função no limite inferior x0.
    
    # Loop para calcular os valores da função nos pontos internos (intermediários entre x0 e x1) e aplicar os coeficientes 4 e 2.
    for i in range(1, num_intervalos):
        x_i = x0 + (h * i)  # Calcula a posição do ponto x_i no intervalo.
        coeficiente = 4 if i % 2 == 1 else 2  # Se i for ímpar, usa o coeficiente 4; se for par, usa o coeficiente 2.
        valores_y.append(coeficiente * funcao(x_i))  # Adiciona o valor da função no ponto x_i multiplicado pelo coeficiente.

    # Adiciona o valor da função no limite superior x1.
    valores_y.append(funcao(x1))  # O último valor é a função no limite superior x1.
    
    # Aplica a fórmula da Regra 1/3 de Simpson para calcular a área aproximada da integral.
    area_aproximada = (h / 3) * sum(valores_y)  # Soma todos os valores calculados e multiplica por h/3.
    
    # Retorna o valor da integral aproximada.
    return area_aproximada

# Define uma função exemplo que será integrada. A função é f(x) = sqrt(x) + 1/x.
def funcao_exemplo(x: float) -> float:
    """
    Exemplo de função para integração: f(x) = sqrt(x) + 1/x
    """
    return np.sqrt(x) + 1/x  # Calcula e retorna o valor de f(x) = sqrt(x) + 1/x.

# Abaixo está a execução do código principal.
if __name__ == "__main__":
    # Exemplo de uso da função calcular_regra13simpson.
    # Calcula a integral de f(x) no intervalo [1.4, 1.8] usando 4 subintervalos.
    resultado = calcular_regra13simpson(1.4, 1.8, 4, funcao_exemplo)
    
    # Exibe o resultado da integral aproximada com 6 casas decimais.
    print(f"Área aproximada: {resultado:.6f}")
